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


def write_description(fid, query_id):
    """Write available query parameters."""
    xml = ET.fromstring(read_url(wfs.BASE_URL + "DescribeStoredQueries&storedquery_id=" + query_id))
    fid.write("<p>")
    fid.write(xml.findtext(wfs.WFS_ABSTRACT).strip())
    fid.write("</p>")
    fid.write("<ul>")
    fid.write("<li>Query ID: %s</li>" % query_id)
    fid.write("<li>Available arguments:</li>")
    fid.write("<ul>")
    params = xml.findall(wfs.WFS_PARAMETER)
    for i, param in enumerate(params):
        fid.write("<li>%s</li>" % param.attrib["name"])
        fid.write("<ul>")
        param_title = param.findtext(wfs.WFS_TITLE)
        fid.write("<li>%s</li>" % param_title)
        param_abstract = param.findtext(wfs.WFS_ABSTRACT).strip()
        fid.write("<li>%s</li>" % param_abstract)
        fid.write("</ul>")
    fid.write("</ul>")
    fid.write("</ul>")
    fid.write("</ul>")


def write_html(fname, queries):
    """Save HTML page showing the WFS stored queries."""
    with open(fname, 'w') as fid:
        fid.write("<html><body>")
        fid.write("<h1>Available WFS stored queries in FMI open data.</hi>")
        for key in sorted(queries):
            query = queries[key]
            write_title(fid, query)
            write_description(fid, key)
        fid.write("</body></html>")


def write_title_md(fid, query):
    """Write title of the query."""
    fid.write("## %s\n\n" % query["title"])


def write_md(fname, queries):
    """Save markdown page showing the WFS stored queries in markdown."""
    with open(fname, 'w') as fid:
        fid.write("# Available WFS stored queries in FMI open data.\n\n")
        for key in sorted(queries):
            query = queries[key]
            write_title_md(fid, query)
            write_description_md(fid, key)


def write_description_md(fid, query_id):
    """Write available query parameters in markdown."""
    xml = ET.fromstring(read_url(wfs.BASE_URL + "DescribeStoredQueries&storedquery_id=" + query_id))
    fid.write(xml.findtext(wfs.WFS_ABSTRACT).strip())
    fid.write("\n\n")
    fid.write("* Query ID: `%s`\n" % query_id)
    fid.write("* Available arguments:\n")
    params = xml.findall(wfs.WFS_PARAMETER)
    for i, param in enumerate(params):
        fid.write("    * %s\n" % param.attrib["name"])
        param_title = param.findtext(wfs.WFS_TITLE)
        fid.write("        * %s\n" % param_title)
        param_abstract = param.findtext(wfs.WFS_ABSTRACT).strip()
        fid.write("        * %s\n" % param_abstract)
    fid.write("\n\n")


def main():
    """Run the script."""
    try:
        fname = sys.argv[1]
    except IndexError:
        fname = "wfs.html"

    queries = wfs.get_stored_queries()
    if fname.endswith("html"):
        write_html(fname, queries)
    else:
        write_md(fname, queries)


if __name__ == "__main__":
    main()
