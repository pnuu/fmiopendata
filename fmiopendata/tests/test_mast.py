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

"""Test mast profile parsing."""

import datetime as dt

import numpy as np
import pytest

MEMBER = """  <wfs:member>
    <omso:ProfileObservation>
      <gml:name codeSpace="http://xml.fmi.fi/namespace/locationcode/name">Espoo Latokaski</gml:name>
      <gml:name codeSpace="http://xml.fmi.fi/namespace/locationcode/wmo">2838</gml:name>
      <gml:TimeInstant><gml:timePosition>%(time)s</gml:timePosition></gml:TimeInstant>
      <gml:Point gml:id="point-1-101000" srsDimension="3">
        <gml:pos>60.17771 24.64009 44</gml:pos>
      </gml:Point>
      <gmlcov:positions>%(heights)s</gmlcov:positions>
      <gml:doubleOrNilReasonTupleList>%(values)s</gml:doubleOrNilReasonTupleList>
      <swe:DataRecord>
        <swe:field name="%(parameter)s">
          <swe:Quantity>
            <swe:label>%(label)s</swe:label>
            <swe:uom code="%(unit)s"/>
          </swe:Quantity>
        </swe:field>
      </swe:DataRecord>
    </omso:ProfileObservation>
  </wfs:member>
"""
HEADER = """<?xml version="1.0" encoding="UTF-8"?>
<wfs:FeatureCollection xmlns:wfs="http://www.opengis.net/wfs/2.0"
                       xmlns:omso="http://inspire.ec.europa.eu/schemas/omso/3.0"
                       xmlns:gml="http://www.opengis.net/gml/3.2"
                       xmlns:gmlcov="http://www.opengis.net/gmlcov/1.0"
                       xmlns:swe="http://www.opengis.net/swe/2.0">
"""
TIME = dt.datetime(2026, 9, 8, 20, 20)
TEMPERATURE = dict(time="2026-09-08T20:20:00Z", heights="2.0 26.0 49.0",
                   values="15.8 15.6 15.5", parameter="TA",
                   label="Air temperature", unit="degC")
WIND_SPEED = dict(TEMPERATURE, values="3.1 4.6 5.2", parameter="WS",
                  label="Wind speed", unit="m/s")


def _mast_xml(*members):
    """Build a mast response out of the given members."""
    return HEADER + "".join(MEMBER % member for member in members) + "</wfs:FeatureCollection>"


def test_mast_parsing():
    """Test parsing the profiles of a mast."""
    from fmiopendata.mast import Mast

    res = Mast(_mast_xml(TEMPERATURE, WIND_SPEED))

    assert list(res.data) == [TIME]
    station = res.data[TIME]["Espoo Latokaski"]
    assert sorted(station) == ["Air temperature", "Wind speed"]

    temperature = station["Air temperature"]
    np.testing.assert_allclose(temperature["heights"], [2.0, 26.0, 49.0])
    np.testing.assert_allclose(temperature["values"], [15.8, 15.6, 15.5])
    assert temperature["unit"] == "degC"
    np.testing.assert_allclose(station["Wind speed"]["values"], [3.1, 4.6, 5.2])

    assert res.location_metadata["Espoo Latokaski"] == {"fmisid": 101000,
                                                        "latitude": 60.17771,
                                                        "longitude": 24.64009,
                                                        "altitude": 44.0}


def test_profile_of_the_wrong_length():
    """Test a profile with a value missing."""
    from fmiopendata.mast import Mast

    broken = dict(TEMPERATURE, values="15.8 15.6")
    with pytest.warns(UserWarning, match="3 heights but 2 values"):
        res = Mast(_mast_xml(broken, WIND_SPEED))

    # The profile that does line up is kept
    assert sorted(res.data[TIME]["Espoo Latokaski"]) == ["Wind speed"]


def test_no_data():
    """Test a response with no observations in it."""
    from fmiopendata.mast import Mast

    with pytest.warns(UserWarning, match="No observations found"):
        res = Mast("<xml></xml>")

    assert res.data == {}
    assert res.location_metadata == {}


@pytest.mark.network
def test_mast_download():
    """Test downloading and parsing the mast observations."""
    from fmiopendata.wfs import download_stored_query

    res = download_stored_query("fmi::observations::weather::mast::multipointcoverage")

    assert res.data
    latest = max(res.data)
    assert isinstance(latest, dt.datetime)

    for station, parameters in res.data[latest].items():
        assert station in res.location_metadata
        for profile in parameters.values():
            assert profile["heights"].size == profile["values"].size
            assert profile["heights"].size > 1
            assert isinstance(profile["unit"], str)
