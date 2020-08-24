# -*- coding: utf-8 -*-
#
# Copyright (c) Panu Lahtinen
#
# Author(s):
#
#   Panu Lahtinen <pnuu+git@iki.fi>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import datetime as dt
import xml.etree.ElementTree as ET
import tempfile
import sys
if sys.version_info < (3, 6):
    from collections import OrderedDict as dict

import rasterio
import numpy as np

from fmiopendata import wfs
from fmiopendata.utils import read_url

TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

meta_cache = dict()


def get_meta(meta_url):
    """Get metadata from *meta_url*."""
    meta = meta_cache.get(meta_url)
    if meta is None:
        meta = ET.fromstring(read_url(meta_url))
        meta_cache[meta_url] = meta
    return meta


class Radar(object):
    """Container for Radar data."""

    def __init__(self):
        """Initialize class."""
        self.time = None
        self._gain = None
        self._offset = None
        self.elevation = None
        self.etop_threshold = None
        self.projection = None
        self.max_velocity = None
        self.url = None
        self.data = None
        self._dtype = None
        self.name = None
        self.label = None
        self.unit = None

    def download(self):
        """Download the data."""
        if self.data is None:
            with tempfile.NamedTemporaryFile() as fid:
                data = read_url(self.url)
                if len(data) < 10e3 and "ServiceException" in str(data):
                    msg = "WMS returned an exception: %s" % str(data)
                    raise ValueError(msg)
                fid.write(data)
                img = rasterio.open(fid.name)
                self.projection = img.crs.wkt
                self.data = img.read()
                self._dtype = self.data.dtype

    def get_area_mask(self):
        """Get a mask for areas outside the detection range."""
        self.download()
        if self.data.dtype == np.uint8:
            value = 255
        elif self.data.dtype == np.uint16:
            value = 65535
        else:
            if self._dtype == np.uint8:
                max_val = 255
            else:
                max_val = 65535
            value = max_val * self._gain + self._offset
        return self.data == value

    def get_data_mask(self):
        """Get a mask for invalid data."""
        self.download()
        if self.data.dtype in (np.uint8, np.uint16):
            value = 0
        else:
            value = 0 * self._gain + self._offset
        return self.data == value

    def calibrate(self):
        """Calibrate the data."""
        self.download()
        if self._gain:
            self.data = self.data * self._gain
            self.data += self._offset


class ParseRadar(object):
    """Parse radar data."""

    def __init__(self, xml):
        """Initialize class."""
        self._xml = ET.fromstring(xml)
        self.data = []
        self.times = []
        self._parse()

    def _parse(self):
        """Parse XML."""
        for member in self._xml.findall(wfs.WFS_MEMBER):
            radar = Radar()
            times = member.findall(wfs.GML_TIME_INSTANT)
            tim = dt.datetime.strptime(times[0].findtext(wfs.GML_TIME_POSITION),
                                       TIME_FORMAT)
            radar.time = tim
            self.times.append(tim)
            for parameter in member.findall(wfs.OM_PARAMETER):
                val = float(parameter.findtext(wfs.GML_MEASURE))
                name = parameter.find(wfs.OM_NAME).attrib[wfs.LINK]
                if "linearTransformationGain" in name:
                    radar._gain = val
                elif "linearTransformationOffset" in name:
                    radar._offset = val
                elif "reflectivityTreshold" in name:
                    radar.etop_threshold = val
                elif "elevationAngle" in name:
                    radar.elevation = val
                elif "maxVel" in name:
                    radar.max_velocity = val
            radar.name = member.find(wfs.SWE_DATA_RECORD).find(wfs.SWE_FIELD).attrib["name"]
            meta_url = member.find(wfs.SWE_DATA_RECORD).find(wfs.SWE_FIELD).attrib[wfs.LINK]
            meta = get_meta(meta_url)
            radar.unit = meta.find(wfs.OMOP_UOM).attrib["uom"]
            radar.label = meta.findtext(wfs.OMOP_LABEL)
            radar.url = member.findtext(wfs.GML_FILE_REFERENCE)
            radar.projection = radar.url.split('srs=')[-1].split('&')[0]
            self.data.append(radar)


def download_and_parse(query_id, args=None):
    """Download and parse the given stored query."""
    url = wfs.STORED_QUERY_URL + query_id
    if args:
        url = url + "&" + "&".join(args)
    xml = read_url(url)
    return ParseRadar(xml)
