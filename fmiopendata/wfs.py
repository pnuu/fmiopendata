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
if sys.version_info < (3, 6):
    from collections import OrderedDict as dict

from fmiopendata.utils import read_url


BASE_URL = "http://opendata.fmi.fi/wfs?service=WFS&request="
STORED_QUERY_URL = "http://opendata.fmi.fi/wfs?service=WFS&version=2.0.0&request=getFeature&storedquery_id="

GML_BEGIN_POSITION = ".//{http://www.opengis.net/gml/3.2}beginPosition"
GML_DOUBLE_OR_NIL_REASON_TUPLE_LIST = ".//{http://www.opengis.net/gml/3.2}doubleOrNilReasonTupleList"
GML_END_POSITION = ".//{http://www.opengis.net/gml/3.2}endPosition"
GML_FILE_REFERENCE = ".//{http://www.opengis.net/gml/3.2}fileReference"
GML_ID = "{http://www.opengis.net/gml/3.2}id"
GML_IDENTIFIER = "{http://www.opengis.net/gml/3.2}identifier"
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
WFS_MEMBER = ".//{http://www.opengis.net/wfs/2.0}member"
WFS_PARAMETER = ".//{http://www.opengis.net/wfs/2.0}Parameter"
WFS_PARAMETER_NAME = ".//{http://xml.fmi.fi/schema/wfs/2.0}ParameterName"
WFS_PARAMETER_VALUE = ".//{http://xml.fmi.fi/schema/wfs/2.0}ParameterValue"
WFS_RETURN_FEATURE_TYPE = ".//{http://www.opengis.net/wfs/2.0}ReturnFeatureType"
WFS_STORED_QUERY = ".//{http://www.opengis.net/wfs/2.0}StoredQuery"
WFS_TIME = ".//{http://xml.fmi.fi/schema/wfs/2.0}Time"
WFS_TITLE = ".//{http://www.opengis.net/wfs/2.0}Title"


def get_req_xml(req):
    """Get request XML for *req*."""
    return read_url(BASE_URL + req)


def get_capabilities():
    """Get WFS cababilities."""
    xml = get_req_xml("getCapabilities")

    return xml


def get_stored_queries():
    """Get stored queries."""
    queries = get_req_xml("ListStoredQueries")
    res = dict()
    root = ET.fromstring(queries)
    queries = root.findall(WFS_STORED_QUERY)
    for query in queries:
        name = query.attrib['id']
        if "ById" in name:
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
    for f in root.getchildren():
        if f.attrib['id'] == 'GetDataSetById':
            continue
        f_ch = f.getchildren()
        desc = dict({'title': f_ch[0].text.strip(),
                     'description': f_ch[1].text.strip()})
        res[f.attrib['id']] = desc

    return res


def download_stored_query(query_id, args=None):
    """Download and parse a stored query."""
    if "radar" in query_id.lower():
        from fmiopendata.radar import download_and_parse
    elif "sounding" in query_id.lower():
        from fmiopendata.sounding import download_and_parse
    elif "lightning" in query_id.lower():
        from fmiopendata.lightning import download_and_parse
    elif "grid" in query_id.lower():
        from fmiopendata.grid import download_and_parse
    elif "multipointcoverage" in query_id.lower():
        from fmiopendata.multipoint import download_and_parse
    else:
        raise NotImplementedError("No parser available for %s" % query_id)

    return download_and_parse(query_id, args=args)