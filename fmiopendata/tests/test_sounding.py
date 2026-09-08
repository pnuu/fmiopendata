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

"""Test sounding parser."""

import datetime as dt
from unittest import mock

import numpy as np
import pytest


@pytest.mark.network
def test_sounding():
    """Test sounding parser."""
    from fmiopendata.sounding import download_and_parse

    res = download_and_parse("fmi::observations::weather::sounding::multipointcoverage")

    snd = res.soundings[0]
    assert isinstance(snd.name, str)
    assert snd.id is not None
    assert snd.nominal_time is not None
    assert snd.start_time is not None
    assert snd.end_time is not None
    num = len(snd.lons)
    assert num == len(snd.lats) == len(snd.altitudes) == len(snd.times)
    assert num == len(snd.pressures) == len(snd.temperatures) == len(snd.dew_points)
    assert num == len(snd.wind_speeds) == len(snd.wind_directions)
    assert num == len(snd.relative_humidities) == len(snd.absolute_humidities)


@mock.patch("fmiopendata.sounding.ParseSoundings")
@mock.patch("fmiopendata.sounding.read_url")
def test_args(read_url, ParseSoundings):
    """Test that arguments are passed properly."""
    from fmiopendata.sounding import download_and_parse

    res = download_and_parse("foo", args=["a=1", "b=2"])
    del res
    assert read_url.call_args[0][0].endswith("=foo&a=1&b=2")


def test_no_data():
    """Test that missing data is handled properly."""
    from fmiopendata.sounding import ParseSoundings

    empty_xml = "<xml></xml>"

    obs = ParseSoundings(empty_xml)
    _check_soundings_empty(obs)


def _check_soundings_empty(obs):
    assert obs.soundings == []


SOUNDING = """<?xml version="1.0" encoding="UTF-8"?>
<wfs:FeatureCollection xmlns:wfs="http://www.opengis.net/wfs/2.0"
                       xmlns:gml="http://www.opengis.net/gml/3.2"
                       xmlns:gmlcov="http://www.opengis.net/gmlcov/1.0"
                       xmlns:swe="http://www.opengis.net/swe/2.0">
  <wfs:member>
    <gml:name codeSpace="http://xml.fmi.fi/namespace/locationcode/wmo">02963</gml:name>
    <gml:name codeSpace="http://xml.fmi.fi/namespace/locationcode/name">Jokioinen</gml:name>
    <gml:timePosition>2026-09-08T00:00:00Z</gml:timePosition>
    <gml:beginPosition>2026-09-08T00:01:00Z</gml:beginPosition>
    <gml:endPosition>2026-09-08T00:30:00Z</gml:endPosition>
    <gmlcov:positions>60.8 23.5 100.0 1788847200 60.9 23.6 200.0 1788847260</gmlcov:positions>
    <gml:doubleOrNilReasonTupleList>%s</gml:doubleOrNilReasonTupleList>
    <swe:DataRecord>
      <swe:field name="PAP_PT1S_AVG"/>
      <swe:field name="%s"/>
    </swe:DataRecord>
  </wfs:member>
</wfs:FeatureCollection>
"""
MEASUREMENTS = "994.3 12.1 980.0 11.0"


def test_parsing():
    """Test parsing a sounding without downloading one."""
    from fmiopendata.sounding import ParseSoundings

    res = ParseSoundings(SOUNDING % (MEASUREMENTS, "TAP_PT1S_AVG"))

    snd = res.soundings[0]
    assert snd.name == "Jokioinen"
    assert snd.id == "02963"
    assert snd.nominal_time == dt.datetime(2026, 9, 8)
    np.testing.assert_allclose(snd.lats, [60.8, 60.9])
    np.testing.assert_allclose(snd.altitudes, [100.0, 200.0])
    np.testing.assert_allclose(snd.pressures, [994.3, 980.0])
    np.testing.assert_allclose(snd.temperatures, [12.1, 11.0])


def test_more_measurements_than_locations():
    """Test a sounding whose measurements and locations do not match."""
    from fmiopendata.sounding import ParseSoundings

    with pytest.warns(UserWarning, match="2 locations but 3 measurement levels"):
        res = ParseSoundings(SOUNDING % (MEASUREMENTS + " 900.0 9.0", "TAP_PT1S_AVG"))

    snd = res.soundings[0]
    # The measurements that have a location are kept, and they stay aligned with it
    assert len(snd.pressures) == len(snd.temperatures) == len(snd.lats) == 2
    np.testing.assert_allclose(snd.pressures, [994.3, 980.0])


def test_unknown_field():
    """Test a sounding that has a field the library does not know."""
    from fmiopendata.sounding import ParseSoundings

    with pytest.warns(UserWarning, match="Unknown sounding field XYZ_PT1S_AVG"):
        res = ParseSoundings(SOUNDING % (MEASUREMENTS, "XYZ_PT1S_AVG"))

    snd = res.soundings[0]
    # The known field is still where it belongs, and the unknown one is not lost
    np.testing.assert_allclose(snd.pressures, [994.3, 980.0])
    np.testing.assert_allclose(snd.xyz_pt1s_avg, [12.1, 11.0])
