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
        fid.write("<li>Earliest: %s</li>" % dt.datetime.strftime(layer.start_time, TIME_FORMAT))
        fid.write("<li>Latest: %s</li>" % dt.datetime.strftime(layer.end_time, TIME_FORMAT))
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
        fid.write("<h1>Available WMS layers in FMI open data.</h1>")
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


def write_title_md(fid, layer):
    """Write title of the layer in markdown."""
    fid.write("## %s\n\n" % layer.title)


def write_abstract_md(fid, layer):
    """Write abstract of the layer in markdown."""
    if layer.abstract:
        fid.write("%s\n\n" % layer.abstract)


def write_name_md(fid, layer):
    """Write name of the layer in markdown."""
    fid.write("* Layer ID: `%s`\n" % layer.name)


def write_bbox_md(fid, layer):
    """Write bounding boxes and CRSs available for the layer in markdown."""
    if layer.bbox:
        fid.write("* Bounding boxes:\n")
        for bbox in layer.bbox:
            fid.write("    * %s\n" % bbox['CRS'])
            fid.write("        * X min: %s\n" % bbox['minx'])
            fid.write("        * X max: %s\n" % bbox['maxx'])
            fid.write("        * Y min: %s\n" % bbox['miny'])
            fid.write("        * Y max: %s\n" % bbox['maxy'])


def write_times_md(fid, layer):
    """Write earliest and latest times, and time step for the layer in markdown."""
    if layer.time_step_str:
        fid.write("* Available times:\n")
        fid.write("    * Earliest: %s\n" % dt.datetime.strftime(layer.start_time, TIME_FORMAT))
        fid.write("    * Latest: %s\n" % dt.datetime.strftime(layer.end_time, TIME_FORMAT))
        fid.write("    * %s\n" % layer.time_step_str)


def write_elevations_md(fid, layer):
    """Write available elevations for the layer in markdown."""
    if layer.elevations:
        fid.write("* Elevations:\n")
        for elev in layer.elevations:
            fid.write("    * %s\n" % elev)


def write_md(fname, layers):
    """Save markdown page showing the WMS layers."""
    with open(fname, 'w') as fid:
        fid.write("# Available WMS layers in FMI open data.\n\n")
        for key in sorted(layers):
            layer = layers[key]
            write_title_md(fid, layer)
            write_abstract_md(fid, layer)
            write_name_md(fid, layer)
            write_bbox_md(fid, layer)
            write_times_md(fid, layer)
            write_elevations_md(fid, layer)
            fid.write("\n\n")


def main():
    """Run the script."""
    try:
        fname = sys.argv[1]
    except IndexError:
        fname = "wms.html"

    layers = get_wms_layers()
    if fname.endswith("html"):
        write_html(fname, layers)
    else:
        write_md(fname, layers)


if __name__ == "__main__":
    main()
