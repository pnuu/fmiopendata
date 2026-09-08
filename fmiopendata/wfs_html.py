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

"""List the WFS stored queries available in FMI open data."""

import sys

import defusedxml.ElementTree as ET

from fmiopendata import namespaces, wfs
from fmiopendata.utils import read_url

# The parameters that can be asked for with the "parameters" argument
PROPERTIES_URL = "https://opendata.fmi.fi/meta?observableProperty=observation&language=eng"
OMOP_OBSERVABLE_PROPERTY = ".//{http://inspire.ec.europa.eu/schemas/omop/2.9}ObservableProperty"
# The queries whose data are calibrated, and whose coefficients are worth listing
CALIBRATED_QUERIES = "fmi::radar"


def get_text(xml, path):
    """Get the stripped text of the first *path* match in *xml*, empty if there is none."""
    text = xml.findtext(path)
    if text is None:
        return ""
    return text.strip()


def get_description(query_id):
    """Get the description of the stored query *query_id*."""
    return ET.fromstring(read_url(wfs.BASE_URL + "DescribeStoredQueries&storedquery_id=" + query_id))


def get_observable_properties():
    """Get every parameter that can be named in a "parameters" argument."""
    xml = ET.fromstring(read_url(PROPERTIES_URL))

    properties = []
    for prop in xml.findall(OMOP_OBSERVABLE_PROPERTY):
        uom = prop.find(namespaces.OMOP_UOM)
        properties.append({"id": prop.attrib.get(namespaces.GML_ID, ""),
                           "label": get_text(prop, namespaces.OMOP_LABEL),
                           "unit": uom.attrib.get("uom", "") if uom is not None else ""})

    return sorted(properties, key=lambda prop: prop["id"])


def get_calibration(query_id):
    """Get how the datasets of *query_id* are calibrated.

    The coefficients are not part of the query description: they come with the data,
    so the query itself has to be asked.  Only the metadata are read, no images are
    downloaded.  Reading them needs the radar parser, so a package without its
    dependencies simply gets nothing to write.
    """
    if not query_id.startswith(CALIBRATED_QUERIES):
        return []
    try:
        from fmiopendata.radar import download_and_parse
    except ImportError:
        return []

    try:
        datasets = download_and_parse(query_id).data
    except Exception:  # noqa: B902  the catalogue is worth more than one query
        return []

    calibrations = []
    for dataset in datasets:
        calibration = {"name": dataset.name,
                       "label": dataset.label,
                       "unit": dataset.unit,
                       "function": _calibration_function(dataset)}
        if calibration not in calibrations:
            calibrations.append(calibration)

    return calibrations


def _calibration_function(dataset):
    """Describe how the raw counts of *dataset* become physical values."""
    gain, offset = dataset._gain, dataset._offset
    if not gain or offset is None:
        return None

    return "y = %s * x %s %s" % (gain, "-" if offset < 0 else "+", abs(offset))


def write_title(fid, query):
    """Write title of the query."""
    fid.write("<h2>%s</h2>" % query["title"])


def write_description(fid, query_id):
    """Write available query parameters."""
    xml = get_description(query_id)
    fid.write("<p>")
    fid.write(get_text(xml, namespaces.WFS_ABSTRACT))
    fid.write("</p>")
    fid.write("<ul>")
    fid.write("<li>Query ID: %s</li>" % query_id)
    fid.write("<li>Available arguments:</li>")
    fid.write("<ul>")
    params = xml.findall(namespaces.WFS_PARAMETER)
    for param in params:
        fid.write("<li>%s (%s)</li>" % (param.attrib["name"], param.attrib.get("type", "")))
        fid.write("<ul>")
        fid.write("<li>%s</li>" % get_text(param, namespaces.WFS_TITLE))
        fid.write("<li>%s</li>" % get_text(param, namespaces.WFS_ABSTRACT))
        fid.write("</ul>")
    fid.write("</ul>")
    write_calibration(fid, query_id)
    fid.write("</ul>")


def write_calibration(fid, query_id):
    """Write how the values of the datasets are calibrated."""
    calibrations = get_calibration(query_id)
    if not calibrations:
        return

    fid.write("<li>Calibration:</li>")
    fid.write("<ul>")
    for calibration in calibrations:
        fid.write("<li>%s (%s)</li>" % (calibration["name"], calibration["label"]))
        fid.write("<ul>")
        fid.write("<li>Calibrated unit: %s</li>" % calibration["unit"])
        if calibration["function"]:
            fid.write("<li>Calibration: %s</li>" % calibration["function"])
        fid.write("</ul>")
    fid.write("</ul>")


def write_properties(fid, properties):
    """Write the parameters that can be named in a "parameters" argument."""
    fid.write("<h2>Available parameters</h2>")
    fid.write("<p>Parameters that can be named in the <code>parameters</code> "
              "argument of the queries that have one.  Not every parameter is "
              "available from every query.</p>")
    fid.write("<table border='1'>")
    fid.write("<tr><th>ID</th><th>Description</th><th>Unit</th></tr>")
    for prop in properties:
        fid.write("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" %
                  (prop["id"], prop["label"], prop["unit"]))
    fid.write("</table>")


def write_html(fname, queries):
    """Save HTML page showing the WFS stored queries."""
    with open(fname, 'w') as fid:
        fid.write("<html><body>")
        fid.write("<h1>Available WFS stored queries in FMI open data.</h1>")
        for key in sorted(queries):
            query = queries[key]
            write_title(fid, query)
            write_description(fid, key)
        write_properties(fid, get_observable_properties())
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
        write_properties_md(fid, get_observable_properties())


def write_description_md(fid, query_id):
    """Write available query parameters in markdown."""
    xml = get_description(query_id)
    fid.write(get_text(xml, namespaces.WFS_ABSTRACT))
    fid.write("\n\n")
    fid.write("* Query ID: `%s`\n" % query_id)
    fid.write("* Available arguments:\n")
    params = xml.findall(namespaces.WFS_PARAMETER)
    for param in params:
        fid.write("    * %s (%s)\n" % (param.attrib["name"], param.attrib.get("type", "")))
        fid.write("        * %s\n" % get_text(param, namespaces.WFS_TITLE))
        fid.write("        * %s\n" % get_text(param, namespaces.WFS_ABSTRACT))
    write_calibration_md(fid, query_id)
    fid.write("\n\n")


def write_calibration_md(fid, query_id):
    """Write how the values of the datasets are calibrated, in markdown."""
    calibrations = get_calibration(query_id)
    if not calibrations:
        return

    fid.write("* Calibration:\n")
    for calibration in calibrations:
        fid.write("    * %s (%s)\n" % (calibration["name"], calibration["label"]))
        fid.write("        * Calibrated unit: %s\n" % calibration["unit"])
        if calibration["function"]:
            fid.write("        * Calibration: %s\n" % calibration["function"])


def write_properties_md(fid, properties):
    """Write the parameters that can be named in a "parameters" argument, in markdown."""
    fid.write("# Available parameters\n\n")
    fid.write("Parameters that can be named in the `parameters` argument of the queries\n"
              "that have one.  Not every parameter is available from every query.\n\n")
    fid.write("| ID | Description | Unit |\n")
    fid.write("| --- | --- | --- |\n")
    for prop in properties:
        fid.write("| `%s` | %s | %s |\n" % (prop["id"], prop["label"], prop["unit"]))


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
