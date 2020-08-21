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


class Lightning(object):
    """Class for holding lightning data."""

    def __init__(self, xml, mode):
        """Initialize the class."""
        self._xml = ET.fromstring(xml)
        self.latitudes = None
        self.longitudes = None
        self.times = None
        self.multiplicity = None
        self.peak_current = None
        self.cloud_indicator = None
        self.ellipse_major = None
        if mode == "simple":
            self._parse_simple()
        elif mode == "multipointcoverage":
            self._parse_multipoint()
        else:
            raise NotImplementedError("No parser for %s" % mode)

    def _parse_simple(self):
        """Parse lightning data.

        Version for fmi::observations::lightning::simple query.

        """
        lats, lons, times = [], [], []
        multiplicity, peak_current, cloud_indicator, ellipse_major = [], [], [], []
        for member in self._xml.findall(wfs.WFS_MEMBER):
            tim = dt.datetime.strptime(member.findtext(wfs.WFS_TIME), TIME_FORMAT)
            lat, lon = [float(p) for p in member.findtext(wfs.GML_POS).split()]
            if not lats or (lat != lats[-1] and lon != lons[-1]):
                lats.append(lat)
                lons.append(lon)
                times.append(tim)
            param = member.findtext(wfs.WFS_PARAMETER_NAME)
            val = member.findtext(wfs.WFS_PARAMETER_VALUE)
            if param == "multiplicity":
                multiplicity.append(int(val))
            elif param == "peak_current":
                peak_current.append(float(val))
            elif param == "cloud_indicator":
                cloud_indicator.append(int(val))
            elif param == "ellipse_major":
                ellipse_major.append(float(val))
        self.latitudes = np.array(lats)
        self.longitudes = np.array(lons)
        self.times = np.array(times)
        self.multiplicity = np.array(multiplicity).astype(np.uint8)
        self.peak_current = np.array(peak_current)
        self.cloud_indicator = np.array(cloud_indicator).astype(np.uint8)
        self.ellipse_major = np.array(ellipse_major)

    def _parse_multipoint(self):
        """Parse lightning data.

        Version for fmi::observations::lightning::multipointcoverage query.

        """
        positions = np.fromstring(self._xml.findtext(wfs.GMLCOV_POSITIONS), dtype=float, sep=" ")
        self.latitudes = positions[::3]
        self.longitudes = positions[1::3]
        times = positions[2::3]
        self.times = np.array([dt.datetime.utcfromtimestamp(t) for t in times])

        data = np.fromstring(self._xml.findtext(wfs.GML_DOUBLE_OR_NIL_REASON_TUPLE_LIST), dtype=float, sep=" ")
        fields = [f.attrib['name'] for f in self._xml.findall(wfs.SWE_FIELD)]
        for i, field in enumerate(fields):
            vals = data[i::len(fields)]
            setattr(self, field, vals)


def download_and_parse(query_id, args=None):
    """Download and parse the given stored query."""
    url = wfs.STORED_QUERY_URL + query_id
    if args:
        url = url + "&" + "&".join(args)
    xml = read_url(url)
    mode = query_id.split("::")[-1]
    return Lightning(xml, mode)
