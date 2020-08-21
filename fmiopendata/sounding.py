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

import xml.etree.ElementTree as ET
import datetime as dt

import numpy as np

from fmiopendata import wfs
from fmiopendata.utils import read_url

TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
FIELD_NAMES = {"PAP_PT1S_AVG": "pressures",
               "WSP_PT1S_AVG": "wind_speeds",
               "WDP_PT1S_AVG": "wind_directions",
               "TAP_PT1S_AVG": "temperatures",
               "TDP_PT1S_AVG": "dew_points",
               }


class Sounding(object):
    """Class for holding a single sounding."""

    def __init__(self):
        """Initialize sounding."""
        self.name = None
        self.id = None
        self.nominal_time = None
        self.start_time = None
        self.end_time = None
        self.lats = None
        self.lons = None
        self.altitudes = None
        self.times = None
        self.pressures = None
        self.temperatures = None
        self.dew_points = None
        self.wind_speeds = None
        self.wind_directions = None


class ParseSoundings(object):
    """Collect sounding data."""

    def __init__(self, xml):
        """Initialize sounding collector."""
        self._xml = ET.fromstring(xml)
        self.soundings = []
        self._parse()

    def _parse(self):
        """Parse sounding data."""
        for member in self._xml.findall(wfs.WFS_MEMBER):
            sounding = Sounding()
            for name in member.findall(wfs.GML_NAME):
                try:
                    if name.attrib["codeSpace"] == "http://xml.fmi.fi/namespace/locationcode/wmo":
                        sounding.id = name.text
                    elif name.attrib["codeSpace"] == "http://xml.fmi.fi/namespace/locationcode/name":
                        sounding.name = name.text
                except KeyError:
                    continue

            sounding.nominal_time = dt.datetime.strptime(member.findtext(wfs.GML_TIME_POSITION), TIME_FORMAT)
            sounding.start_time = dt.datetime.strptime(member.findtext(wfs.GML_BEGIN_POSITION), TIME_FORMAT)
            sounding.end_time = dt.datetime.strptime(member.findtext(wfs.GML_END_POSITION), TIME_FORMAT)

            positions = np.fromstring(member.findtext(wfs.GMLCOV_POSITIONS), dtype=float, sep=" ")
            sounding.lats = positions[::4]
            sounding.lons = positions[1::4]
            sounding.altitudes = positions[2::4]
            times = positions[3::4]
            sounding.times = np.array([dt.datetime.utcfromtimestamp(t) for t in times])

            data = np.fromstring(member.findtext(wfs.GML_DOUBLE_OR_NIL_REASON_TUPLE_LIST), dtype=float, sep=" ")
            fields = member.findall(wfs.SWE_FIELD)
            for i, field in enumerate(fields):
                setattr(sounding, FIELD_NAMES[field.attrib["name"]], data[i::len(fields)])

            self.soundings.append(sounding)


def download_and_parse(query_id, args=None):
    """Download and parse the given stored query."""
    url = wfs.STORED_QUERY_URL + query_id
    if args:
        url = url + "&" + "&".join(args)
    xml = read_url(url)
    return ParseSoundings(xml)
