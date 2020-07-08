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


class MultiPoint(object):
    """Class for holding multipoint data."""

    def __init__(self, xml):
        """Initialize class."""
        self._xml = ET.fromstring(xml)
        self.data = {}
        self.location_metadata = {}
        self._location2name = {}
        self._type2obs = {}
        self._parse()

    def _parse(self):
        """Parse data."""
        for point in self._xml.findall(wfs.GML_POINT):
            fmisid = int(point.attrib[wfs.GML_ID].split('-')[-1])
            name = point.findtext(wfs.GML_NAME)
            location = tuple(float(p) for p in point.findtext(wfs.GML_POS).split())
            self.location_metadata[name] = {"fmisid": fmisid,
                                            "latitude": location[0],
                                            "longitude": location[1]
                                            }
            self._location2name[location] = name

        positions = np.fromstring(self._xml.findtext(wfs.GMLCOV_POSITIONS), dtype=float, sep=" ")
        latitudes = positions[::3]
        longitudes = positions[1::3]
        times = np.array([dt.datetime.fromtimestamp(t) for t in positions[2::3]])
        measurements = np.fromstring(self._xml.find(wfs.GML_DOUBLE_OR_NIL_REASON_TUPLE_LIST).text, dtype=float, sep=" ")
        for field in self._xml.findall(wfs.SWE_FIELD):
            typ = field.attrib["name"]
            url = field.attrib[wfs.LINK]
            root = ET.fromstring(read_url(url))
            name = root.findtext(wfs.OMOP_LABEL)
            try:
                units = root.find(wfs.OMOP_UOM).attrib["uom"]
            except AttributeError:
                units = ''
            self._type2obs[typ] = {"name": name, "units": units}
        measurements = np.reshape(measurements, (len(times), len(self._type2obs)))

        for i, tim in enumerate(times):
            if tim not in self.data:
                self.data[tim] = {}
            loc = (latitudes[i], longitudes[i])
            name = self._location2name[loc]
            self.data[tim][name] = {}
            for j, key in enumerate(self._type2obs.keys()):
                self.data[tim][name][self._type2obs[key]["name"]] = {"value": measurements[i, j],
                                                                     "units": self._type2obs[key]["units"]
                                                                     }


def download_and_parse(query_id, args=None):
    """Download and parse the given stored query."""
    url = wfs.STORED_QUERY_URL + query_id
    if args:
        url = url + "&" + "&".join(args)
    xml = read_url(url)
    return MultiPoint(xml)
