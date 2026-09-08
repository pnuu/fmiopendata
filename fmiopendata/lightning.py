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
import warnings

import defusedxml.ElementTree as ET

import numpy as np

from fmiopendata import namespaces, wfs
from fmiopendata.utils import epoch_to_datetime, read_url

TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
# Parameters of both formats, and the type the "simple" format presents them in
PARAMETERS = {"multiplicity": np.uint8,
                     "peak_current": None,
                     "cloud_indicator": np.uint8,
                     "ellipse_major": None,
                     }
# Attributes holding the flash locations and times, which a field must not replace
RESERVED_ATTRIBUTES = ("latitudes", "longitudes", "times")


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

        Each flash is described by several members, one per parameter, so the
        members are collected per flash before the arrays are built.  That way a
        parameter that is missing or repeated for a flash cannot shift the other
        parameters out of step with the locations.

        """
        flashes = dict()
        for member in self._xml.findall(namespaces.WFS_MEMBER):
            flash_id = _get_flash_id(member)
            if flash_id not in flashes:
                flashes[flash_id] = {
                    "time": dt.datetime.strptime(member.findtext(namespaces.WFS_TIME), TIME_FORMAT),
                    "location": [float(p) for p in member.findtext(namespaces.GML_POS).split()],
                }
            param = member.findtext(namespaces.WFS_PARAMETER_NAME)
            if param in PARAMETERS:
                flashes[flash_id][param] = float(member.findtext(namespaces.WFS_PARAMETER_VALUE))

        if not flashes:
            warnings.warn("No observations found")

        self.latitudes = np.array([flash["location"][0] for flash in flashes.values()])
        self.longitudes = np.array([flash["location"][1] for flash in flashes.values()])
        self.times = np.array([flash["time"] for flash in flashes.values()])
        for param, dtype in PARAMETERS.items():
            setattr(self, param, _collect_parameter(flashes, param, dtype))

    def _parse_multipoint(self):
        """Parse lightning data.

        Version for fmi::observations::lightning::multipointcoverage query.

        """
        positions_txt = self._xml.findtext(namespaces.GMLCOV_POSITIONS)
        data_txt = self._xml.findtext(namespaces.GML_DOUBLE_OR_NIL_REASON_TUPLE_LIST)
        if positions_txt is None or data_txt is None:
            warnings.warn("No observations found")
            self._set_empty_observations()
            return
        positions = np.fromstring(positions_txt, dtype=float, sep=" ")
        self.latitudes = positions[::3]
        self.longitudes = positions[1::3]
        times = positions[2::3]
        self.times = np.array([epoch_to_datetime(t) for t in times])

        data = np.fromstring(data_txt, dtype=float, sep=" ")
        fields = [f.attrib['name'] for f in self._xml.findall(namespaces.SWE_FIELD)]
        for i, field in enumerate(fields):
            if field in RESERVED_ATTRIBUTES:
                warnings.warn("Ignoring field %s, it would replace the flash "
                              "locations or times" % field)
                continue
            if field not in PARAMETERS:
                warnings.warn("Unknown lightning field %s, it is available as .%s" %
                              (field, field))
            setattr(self, field, data[i::len(fields)])

    def _set_empty_observations(self):
        self.latitudes = np.array([])
        self.longitudes = np.array([])
        self.times = np.array([])
        self.multiplicity = np.array([], dtype=np.uint8)
        self.peak_current = np.array([])
        self.cloud_indicator = np.array([], dtype=np.uint8)
        self.ellipse_major = np.array([])


def _collect_parameter(flashes, param, dtype):
    """Collect the values of *param* from *flashes*, one per flash.

    A flash the service did not give the parameter for gets a NaN, which also means
    the array cannot be presented as an integer type in that case.
    """
    values = np.array([flash.get(param, np.nan) for flash in flashes.values()], dtype=float)
    if dtype is not None and not np.isnan(values).any():
        values = values.astype(dtype)
    return values


def _get_flash_id(member):
    # <BsWfs:BsWfsElement gml:id="BsWfsElement.921.1">
    bs_wfs_element = member.find(namespaces.WFS_BS_WFS_ELEMENT)
    # "BsWfsElement.921.1"
    full_id = bs_wfs_element.attrib[namespaces.GML_ID]
    # 921
    flash_id = int(full_id.split(".")[1])

    return flash_id


def download_and_parse(query_id, args=None):
    """Download and parse the given stored query."""
    url = wfs.STORED_QUERY_URL + query_id
    if args:
        url = url + "&" + "&".join(args)
    xml = read_url(url)
    return Lightning(xml, _get_mode(query_id))


def _get_mode(query_id):
    """Get the format the stored query *query_id* returns.

    The format is matched anywhere in the query id, so that a qualifier after it
    does not hide it.  An unrecognised query id is passed on as it is, for Lightning
    to reject with a message naming it.
    """
    lowered = query_id.lower()
    for mode in ("multipointcoverage", "simple"):
        if mode in lowered:
            return mode
    return query_id.split("::")[-1]
