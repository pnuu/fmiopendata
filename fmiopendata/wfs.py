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

from importlib import import_module

import defusedxml.ElementTree as ET

from fmiopendata.utils import read_url


BASE_URL = "https://opendata.fmi.fi/wfs?service=WFS&request="
STORED_QUERY_URL = "https://opendata.fmi.fi/wfs?service=WFS&version=2.0.0&request=getFeature&storedquery_id="

# The parser of a stored query is chosen by the first of these patterns that the
# query id contains.  The order matters: sounding and lightning queries are also
# served as multipoint coverages, so the specific formats are looked for first.
PARSERS = (("radar", "fmiopendata.radar"),
           ("sounding", "fmiopendata.sounding"),
           ("lightning", "fmiopendata.lightning"),
           ("grid", "fmiopendata.grid"),
           ("multipointcoverage", "fmiopendata.multipoint"),
           )

GML_BEGIN_POSITION = ".//{http://www.opengis.net/gml/3.2}beginPosition"
GML_DOUBLE_OR_NIL_REASON_TUPLE_LIST = ".//{http://www.opengis.net/gml/3.2}doubleOrNilReasonTupleList"
GML_END_POSITION = ".//{http://www.opengis.net/gml/3.2}endPosition"
GML_FILE_REFERENCE = ".//{http://www.opengis.net/gml/3.2}fileReference"
GML_ID = "{http://www.opengis.net/gml/3.2}id"
GML_IDENTIFIER = ".//{http://www.opengis.net/gml/3.2}identifier"
GML_MEASURE = ".//{http://www.opengis.net/gml/3.2}Measure"
GML_NAME = ".//{http://www.opengis.net/gml/3.2}name"
GML_POINT = ".//{http://www.opengis.net/gml/3.2}Point"
GML_POS = ".//{http://www.opengis.net/gml/3.2}pos"
GML_TIME_INSTANT = ".//{http://www.opengis.net/gml/3.2}TimeInstant"
GML_TIME_POSITION = ".//{http://www.opengis.net/gml/3.2}timePosition"
GMLCOV_POSITIONS = ".//{http://www.opengis.net/gmlcov/1.0}positions"
LINK = "{http://www.w3.org/1999/xlink}href"
OM_NAME = ".//{http://www.opengis.net/om/2.0}name"
OM_PARAMETER = ".//{http://www.opengis.net/om/2.0}parameter"
OMOP_LABEL = ".//{http://inspire.ec.europa.eu/schemas/omop/2.9}label"
OMOP_UOM = ".//{http://inspire.ec.europa.eu/schemas/omop/2.9}uom"
SWE_DATA_RECORD = ".//{http://www.opengis.net/swe/2.0}DataRecord"
SWE_FIELD = ".//{http://www.opengis.net/swe/2.0}field"
SWE_LABEL = ".//{http://www.opengis.net/swe/2.0}label"
SWE_UOM = ".//{http://www.opengis.net/swe/2.0}uom"
WFS_ABSTRACT = ".//{http://www.opengis.net/wfs/2.0}Abstract"
WFS_ABSTRACT_ELEMENT = "{http://www.opengis.net/wfs/2.0}Abstract"
WFS_BS_WFS_ELEMENT = ".//{http://xml.fmi.fi/schema/wfs/2.0}BsWfsElement"
WFS_MEMBER = ".//{http://www.opengis.net/wfs/2.0}member"
WFS_PARAMETER = ".//{http://www.opengis.net/wfs/2.0}Parameter"
WFS_PARAMETER_NAME = ".//{http://xml.fmi.fi/schema/wfs/2.0}ParameterName"
WFS_PARAMETER_VALUE = ".//{http://xml.fmi.fi/schema/wfs/2.0}ParameterValue"
WFS_RETURN_FEATURE_TYPE = ".//{http://www.opengis.net/wfs/2.0}ReturnFeatureType"
WFS_STORED_QUERY = ".//{http://www.opengis.net/wfs/2.0}StoredQuery"
WFS_TIME = ".//{http://xml.fmi.fi/schema/wfs/2.0}Time"
WFS_TITLE = ".//{http://www.opengis.net/wfs/2.0}Title"
WFS_TITLE_ELEMENT = "{http://www.opengis.net/wfs/2.0}Title"


def get_req_xml(req):
    """Get request XML for *req*."""
    return read_url(BASE_URL + req)


def get_capabilities():
    """Get WFS cababilities."""
    xml = get_req_xml("getCapabilities")

    return xml


def _get_text(element, tag):
    """Get the stripped text of the first child of *element* with the given *tag*."""
    text = element.findtext(tag)
    if text is None:
        return None
    return text.strip()


def _is_by_id_query(query_id):
    """Tell whether *query_id* returns one identified data set instead of a search."""
    return "ById" in query_id


def get_stored_queries():
    """Get stored queries."""
    queries = get_req_xml("ListStoredQueries")
    res = dict()
    root = ET.fromstring(queries)
    queries = root.findall(WFS_STORED_QUERY)
    for query in queries:
        name = query.attrib['id']
        if _is_by_id_query(name):
            continue
        title = query.findtext(WFS_TITLE)
        return_type = query.findtext(WFS_RETURN_FEATURE_TYPE)
        res[name] = dict({'title': title, 'return_type': return_type})

    return res


def get_stored_query_descriptions():
    """Get stored query descriptions."""
    descriptions = get_req_xml("DescribeStoredQueries")
    res = dict()
    root = ET.fromstring(descriptions)
    for f in root:
        if _is_by_id_query(f.attrib['id']):
            continue
        res[f.attrib['id']] = dict({'title': _get_text(f, WFS_TITLE_ELEMENT),
                                    'description': _get_text(f, WFS_ABSTRACT_ELEMENT)})

    return res


def download_stored_query(query_id, args=None):
    """Download and parse a stored query."""
    download_and_parse = _get_parser(query_id)

    return download_and_parse(query_id, args=args)


def _get_parser(query_id):
    """Get the download and parse function for the stored query *query_id*.

    The parser modules are imported only when they are needed, so that the optional
    dependencies of the radar and grid parsers stay optional.
    """
    lowered = query_id.lower()
    for pattern, module_name in PARSERS:
        if pattern in lowered:
            return import_module(module_name).download_and_parse

    raise NotImplementedError("No parser available for %s" % query_id)
