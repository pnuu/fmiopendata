#!/usr/bin/env python
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

import sys
import datetime as dt

from fmiopendata.wms import get_wms_layers

TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"


def write_title(fid, layer):
    """Write title of the layer."""
    fid.write("<h2>%s</h2>" % layer.title)


def write_abstract(fid, layer):
    """Write abstract of the layer."""
    if layer.abstract:
        fid.write("<p>%s</p>" % layer.abstract)


def write_name(fid, layer):
    """Write name of the layer."""
    fid.write("<li>Layer ID: %s</li>" % layer.name)


def write_bbox(fid, layer):
    """Write bounding boxes and CRSs available for the layer."""
    if layer.bbox:
        fid.write("<li>Bounding boxes:</li>")
        fid.write("<ul>")
        bboxes = layer.bbox
        for bbox in bboxes:
            fid.write("<li>%s</li>" % bbox['CRS'])
            fid.write("<ul>")
            fid.write("<li>X min: %s</li>" % bbox['minx'])
            fid.write("<li>X max: %s</li>" % bbox['maxx'])
            fid.write("<li>Y min: %s</li>" % bbox['miny'])
            fid.write("<li>Y max: %s</li>" % bbox['maxy'])
            fid.write("</ul>")
        fid.write("</ul>")


def write_times(fid, layer):
    """Write earliest and latest times, and time step for the layer."""
    if layer.time_step_str:
        fid.write("<li>Available times:</li>")
        fid.write("<ul>")
        fid.write("<li>Earliest: %s</li>" % dt.datetime.strftime(min(layer.times), TIME_FORMAT))
        fid.write("<li>Latest: %s</li>" % dt.datetime.strftime(max(layer.times), TIME_FORMAT))
        fid.write("<li>%s</li>" % layer.time_step_str)
        fid.write("</ul>")


def write_elevations(fid, layer):
    """Write available elevations for the layer."""
    if layer.elevations:
        fid.write("<li>Elevations:</li>")
        fid.write("<ul>")
        for elev in layer.elevations:
            fid.write("<li>%s</li>" % elev)
        fid.write("</ul>")


def write_html(fname, layers):
    """Save HTML page showing the WMS layers."""
    with open(fname, 'w') as fid:
        fid.write("<html><body>")
        fid.write("<h1>Available WMS layers in FMI open data.</hi>")
        for key in sorted(layers):
            layer = layers[key]
            write_title(fid, layer)
            write_abstract(fid, layer)
            fid.write("<ul>")
            write_name(fid, layer)
            write_bbox(fid, layer)
            write_times(fid, layer)
            write_elevations(fid, layer)
            fid.write("</ul>")
        fid.write("</body></html>")


def main():
    """Run the script."""
    try:
        fname = sys.argv[1]
    except IndexError:
        fname = "wms.html"

    layers = get_wms_layers()
    write_html(fname, layers)


if __name__ == "__main__":
    main()
