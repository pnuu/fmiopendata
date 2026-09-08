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
from fmiopendata.multipoint import parse_names_and_units
from fmiopendata.utils import read_url

TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
STATION_NAME = "http://xml.fmi.fi/namespace/locationcode/name"


class Mast(object):
    """Class for holding mast data.

    A mast measures the same parameters at several heights, so each measurement is a
    profile rather than a single value.  The service describes one parameter of one
    mast at one time per member of the response.
    """

    def __init__(self, xml):
        """Initialize the class."""
        self._xml = ET.fromstring(xml)
        self.data = dict()
        self.location_metadata = dict()
        self._parse()

    def _parse(self):
        """Parse mast data."""
        members = self._xml.findall(namespaces.WFS_MEMBER)
        if not members:
            warnings.warn("No observations found", stacklevel=2)
            return

        for member in members:
            self._parse_member(member)

    def _parse_member(self, member):
        """Parse one profile of one parameter."""
        name = _get_station_name(member)
        if name is None:
            warnings.warn("Skipping a profile that names no mast", stacklevel=3)
            return

        self._parse_location_metadata(member, name)

        time = dt.datetime.strptime(member.findtext(namespaces.GML_TIME_POSITION), TIME_FORMAT)
        heights = np.fromstring(member.findtext(namespaces.GMLCOV_POSITIONS), dtype=float, sep=" ")
        values = np.fromstring(member.findtext(namespaces.GML_DOUBLE_OR_NIL_REASON_TUPLE_LIST),
                               dtype=float, sep=" ")
        if heights.size != values.size:
            warnings.warn("The %s profile from %s at %s has %d heights but %d values, "
                          "skipping it" % (_get_parameter(member), name, time,
                                           heights.size, values.size), stacklevel=3)
            return

        for observed in parse_names_and_units(member).values():
            self.data.setdefault(time, dict()).setdefault(name, dict())[observed["name"]] = {
                "heights": heights,
                "values": values,
                "unit": observed["units"],
            }

    def _parse_location_metadata(self, member, name):
        """Parse the position of the mast."""
        if name in self.location_metadata:
            return

        point = member.find(namespaces.GML_POINT)
        if point is None:
            return

        position = [float(value) for value in point.findtext(namespaces.GML_POS).split()]
        metadata = dict({"fmisid": int(point.attrib[namespaces.GML_ID].split('-')[-1]),
                         "latitude": position[0],
                         "longitude": position[1],
                         })
        if len(position) > 2:
            # The height of the foot of the mast, the profile heights are above it
            metadata["altitude"] = position[2]
        self.location_metadata[name] = metadata


def _get_station_name(member):
    """Get the name of the mast the *member* describes."""
    for element in member.findall(namespaces.GML_NAME):
        if element.attrib.get("codeSpace") == STATION_NAME:
            return element.text

    return None


def _get_parameter(member):
    """Get the name of the parameter the *member* describes, as the service gives it."""
    field = member.find(namespaces.SWE_FIELD)

    return field.attrib.get("name") if field is not None else None


def download_and_parse(query_id, args=None):
    """Download and parse the given stored query."""
    url = wfs.STORED_QUERY_URL + query_id
    if args:
        url = url + "&" + "&".join(args)
    xml = read_url(url)

    return Mast(xml)
