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

from fmiopendata import wfs
from fmiopendata.utils import read_url

TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

meta_cache = {}


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
        self.gain = None
        self.offset = None
        self.elevation = None
        self.threshold = None
        self.projection = None
        self.max_velocity = None
        self.url = None
        self.data = None
        self.name = None
        self.label = None
        self.unit = None

    def download(self):
        """Download the data."""
        raise NotImplementedError("Downloading not implemented.")

    def calibrate(self):
        """Calibrate the data."""
        if self.data is None:
            self.download()
        self.data *= self.gain
        self.data += self.offset


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
                val = float(parameter.findall(wfs.GML_MEASURE)[0].text)
                name = parameter.findall(wfs.OM_NAME)[0].attrib[wfs.LINK]
                if "linearTransformationGain" in name:
                    radar.gain = val
                elif "linearTransformationOffset" in name:
                    radar.offset = val
                elif "reflectivityTreshold" in name:
                    radar.threshold = val
                elif "elevationAngle" in name:
                    radar.elevation = val
                elif "maxVel" in name:
                    radar.max_velocity = val
            radar.name = member.find(wfs.SWE_DATA_RECORD).find(wfs.SWE_FIELD).attrib["name"]
            meta_url = member.find(wfs.SWE_DATA_RECORD).find(wfs.SWE_FIELD).attrib[wfs.LINK]
            meta = get_meta(meta_url)
            radar.unit = meta.find(wfs.OMOP_UOM).attrib["uom"]
            radar.label = meta.find(wfs.OMOP_LABEL).text
            radar.url = member.find(wfs.GML_FILE_REFERENCE).text
            radar.projection = radar.url.split('srs=')[-1].split('&')[0]
            self.data.append(radar)


def download_and_parse(query_id, args=None):
    """Download and parse the given stored query."""
    url = wfs.STORED_QUERY_URL + query_id
    if args:
        url = url + "&" + "&".join(args)
    xml = read_url(url)
    return ParseRadar(xml)
