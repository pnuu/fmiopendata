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
import tempfile
import warnings

import defusedxml.ElementTree as ET

import rasterio
import numpy as np

from fmiopendata import namespaces, wfs
from fmiopendata.utils import read_cached_xml, read_url

TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


def get_meta(meta_url):
    """Get metadata from *meta_url*."""
    return read_cached_xml(meta_url)


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
        self.projection_wkt = None
        self.max_velocity = None
        self.url = None
        self.data = None
        self._dtype = None
        self._calibrated = False
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
                # The image is read back through the file name, so make sure the
                # data have actually reached the file before it is opened
                fid.flush()
                with rasterio.open(fid.name) as img:
                    self.projection_wkt = img.crs.wkt
                    self.data = img.read()
                    self._dtype = self.data.dtype

    def get_area_mask(self):
        """Get a mask for areas outside the detection range."""
        self.download()
        return self.data == self._value_of(self._raw_area_value())

    def get_data_mask(self):
        """Get a mask for invalid data."""
        self.download()
        return self.data == self._value_of(0)

    def _raw_area_value(self):
        """Get the raw count that marks an area outside the detection range."""
        if not np.issubdtype(self._dtype, np.integer):
            raise ValueError("Cannot tell which value marks the area outside the "
                             "detection range in %s data" % self._dtype)
        return np.iinfo(self._dtype).max

    def _can_calibrate(self):
        """Tell whether the data can be turned into physical values."""
        return bool(self._gain) and self._offset is not None

    def _value_of(self, raw_value):
        """Get the value a raw count has in the data as it is now."""
        if not (self._calibrated and self._can_calibrate()):
            return raw_value
        return raw_value * self._gain + self._offset

    def calibrate(self):
        """Calibrate the data.

        Calling this again does nothing: applying the gain and offset a second time
        would turn the data into plausible looking nonsense.
        """
        self.download()
        if self._calibrated:
            return
        if self._can_calibrate():
            self.data = self.data * self._gain
            self.data += self._offset
        elif self._gain is not None or self._offset is not None:
            warnings.warn("The dataset gives only one of the linear transformation "
                          "gain and offset, leaving the data as they are")
        self._calibrated = True


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
        for member in self._xml.findall(namespaces.WFS_MEMBER):
            radar = Radar()
            times = member.findall(namespaces.GML_TIME_INSTANT)
            if not times:
                warnings.warn("Skipping a radar dataset that has no measurement time")
                continue
            tim = dt.datetime.strptime(times[0].findtext(namespaces.GML_TIME_POSITION),
                                       TIME_FORMAT)
            radar.time = tim
            self.times.append(tim)
            for parameter in member.findall(namespaces.OM_PARAMETER):
                val = float(parameter.findtext(namespaces.GML_MEASURE))
                name = parameter.find(namespaces.OM_NAME).attrib[namespaces.LINK]
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
            radar.name = member.find(namespaces.SWE_DATA_RECORD).find(namespaces.SWE_FIELD).attrib["name"]
            meta_url = member.find(namespaces.SWE_DATA_RECORD).find(namespaces.SWE_FIELD).attrib[namespaces.LINK]
            meta = get_meta(meta_url)
            radar.unit = meta.find(namespaces.OMOP_UOM).attrib["uom"]
            radar.label = meta.findtext(namespaces.OMOP_LABEL)
            radar.url = member.findtext(namespaces.GML_FILE_REFERENCE)
            # The CRS the image is requested in; the WKT description of the same
            # projection is filled in from the image itself when it is downloaded
            radar.projection = radar.url.split('srs=')[-1].split('&')[0]
            self.data.append(radar)


def download_and_parse(query_id, args=None):
    """Download and parse the given stored query."""
    url = wfs.STORED_QUERY_URL + query_id
    if args:
        url = url + "&" + "&".join(args)
    xml = read_url(url)
    return ParseRadar(xml)
