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
import sys
if sys.version_info < (3, 6):
    from collections import OrderedDict as dict

from fmiopendata.utils import read_url

WMS_BASE = "https://openwms.fmi.fi/geoserver/wms?request=GetCapabilities"
WMS_LAYERS = './/{http://www.opengis.net/wms}Layer'
TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"


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
        self.times = []
        self.elevations = None
        self.time_step_str = None
        self._parse_layer(layer)

    def __repr__(self):
        """Print WMS layer info."""
        if self.time_step_str is None:
            return self.name + " - no timesteps"
        if self.elevations is None:
            return self.name + " - " + self.time_step_str
        return self.name + " - " + self.time_step_str + ", elavations: " + ', '.join(self.elevations)

    def _get_times(self, txt):
        """Get timestamps."""
        start_time, end_time, step = txt.split('/')
        start_time = dt.datetime.strptime(start_time, TIME_FORMAT)
        end_time = dt.datetime.strptime(end_time, TIME_FORMAT)
        step = step.strip('PT')
        if step[-1] == 'H':
            tstep = dt.timedelta(hours=int(step[:-1]))
            self.time_step_str = step[:-1] + " hour time step"
        elif step[-1] == 'M':
            tstep = dt.timedelta(minutes=int(step[:-1]))
            self.time_step_str = step[:-1] + " minute time step"
        elif step[-1] == 'S':
            tstep = dt.timedelta(seconds=int(step[:-1]))
            self.time_step_str = step[:-1] + " second time step"
        else:
            return

        time_stamp = start_time
        while time_stamp <= end_time:
            self.times.append(time_stamp)
            time_stamp += tstep

    def _parse_layer(self, layer):
        for itm2 in layer.getchildren():
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
