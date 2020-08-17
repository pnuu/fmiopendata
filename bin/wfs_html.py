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

import xml.etree.ElementTree as ET

import sys

from fmiopendata import wfs
from fmiopendata.utils import read_url


def write_title(fid, query):
    """Write title of the query."""
    fid.write("<h2>%s</h2>" % query["title"])


def write_name(fid, name):
    """Write name of the query."""
    fid.write("<li>Query ID: %s</li>" % name)


def write_return_type(fid, query):
    """Write return type of the query."""
    fid.write("<li>Query return type: %s</li>" % query["return_type"])


def write_params(fid, query_id):
    """Write available query parameters."""
    xml = ET.fromstring(read_url(wfs.STORED_QUERY_URL + query_id))
    fid.write("<li>Data fields (used with 'param=' item in the url):</li>")
    fid.write("<ul>")
    for param in xml.find(wfs.SWE_DATA_RECORD).getchildren():
        fid.write("<li>%s</li>" % param.attrib["name"])
    fid.write("</ul>")


def write_html(fname, queries):
    """Save HTML page showing the WFS stored queries."""
    with open(fname, 'w') as fid:
        fid.write("<html><body>")
        fid.write("<h1>Available WFS stored queries in FMI open data.</hi>")
        for key in sorted(queries):
            query = queries[key]
            write_title(fid, query)
            fid.write("<ul>")
            write_name(fid, key)
            write_return_type(fid, query)
            if "grid" in key:
                write_params(fid, key)
            fid.write("</ul>")
        fid.write("</body></html>")


def main():
    """Run the script."""
    try:
        fname = sys.argv[1]
    except IndexError:
        fname = "wfs.html"

    queries = wfs.get_stored_queries()
    write_html(fname, queries)


if __name__ == "__main__":
    main()
