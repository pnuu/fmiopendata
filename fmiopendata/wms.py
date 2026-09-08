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
import re
import warnings

import defusedxml.ElementTree as ET

from fmiopendata.utils import read_url

WMS_BASE = "https://openwms.fmi.fi/geoserver/wms?request=GetCapabilities"
WMS_LAYERS = './/{http://www.opengis.net/wms}Layer'
TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
STEP_UNITS = {"H": "hour", "M": "minute", "S": "second"}


def get_wms_cababilities():
    """Get cababilities from WMS."""
    return read_url(WMS_BASE)


class WMSLayer(object):
    """Class for holding WMS layer information."""

    def __init__(self, layer):
        """Initialize layer."""
        self._layer = layer
        self.name = None
        self.title = None
        self.abstract = None
        self.crs = []
        self.bbox = []
        self.start_time = None
        self.end_time = None
        self.time_step = None
        self.elevations = None
        self.time_step_str = None
        self._parse_layer(layer)

    @property
    def times(self):
        """All the times the layer is available for.

        The capabilities can advertise years of data at a one minute step, so the
        times are generated when they are asked for rather than while the layers are
        being listed.  Use iter_times() to go through them one at a time.
        """
        return list(self.iter_times())

    def iter_times(self):
        """Iterate over the times the layer is available for."""
        if self.time_step is None:
            return
        time_stamp = self.start_time
        while time_stamp <= self.end_time:
            yield time_stamp
            time_stamp += self.time_step

    def __repr__(self):
        """Print WMS layer info."""
        if self.time_step_str is None:
            return self.name + " - no timesteps"
        if self.elevations is None:
            return self.name + " - " + self.time_step_str
        return self.name + " - " + self.time_step_str + ", elavations: " + ', '.join(self.elevations)

    def _get_times(self, txt):
        """Get the time range the layer is available for."""
        start_time, end_time, step = txt.split('/')
        self.time_step, self.time_step_str = _parse_step(step)
        if self.time_step is None:
            return
        self.start_time = dt.datetime.strptime(start_time, TIME_FORMAT)
        self.end_time = dt.datetime.strptime(end_time, TIME_FORMAT)

    def _parse_layer(self, layer):
        for itm2 in list(layer):
            if "Name" in itm2.tag:
                self.name = itm2.text
            elif "Title" in itm2.tag:
                self.title = itm2.text
            elif "Abstract" in itm2.tag:
                self.abstract = itm2.text
            elif "CRS" in itm2.tag and "EPSG" in itm2.text:
                self.crs.append(itm2.text)
            elif "}BoundingBox" in itm2.tag and ("EPSG" in itm2.attrib['CRS'] or "CRS" in itm2.attrib['CRS']):
                self.bbox.append(itm2.attrib)
            elif "Dimension" in itm2.tag and itm2.attrib["name"] == "time":
                self._get_times(itm2.text)
            elif "Dimension" in itm2.tag and itm2.attrib["name"] == "elevation":
                self.elevations = itm2.text.split(',')


def _parse_step(step):
    """Get the length of the ISO 8601 duration *step*, and a description of it.

    Only the plain forms the service uses, such as "PT15M", are understood; anything
    else is reported and left alone rather than being cut apart character by
    character until something that looks like a unit comes out.
    """
    match = re.match(r"^PT(\d+)([HMS])$", step.strip())
    if match is None:
        warnings.warn("Cannot handle the time step %s" % step)
        return None, None

    amount = int(match.group(1))
    unit = STEP_UNITS[match.group(2)]

    return dt.timedelta(**{unit + "s": amount}), "%d %s time step" % (amount, unit)


def get_wms_layers():
    """Get WMS layer info."""
    xml = read_url(WMS_BASE)
    root = ET.fromstring(xml)

    layers = root.findall(WMS_LAYERS)

    res = dict()
    for itm in layers:
        layer = WMSLayer(itm)
        if layer.name is not None:
            res[layer.name] = layer

    return res
