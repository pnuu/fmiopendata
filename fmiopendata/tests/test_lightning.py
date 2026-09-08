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

"""Test lightning parsers."""

import pytest
from unittest import mock
import datetime as dt

import numpy as np

# Define a time period that has data
START_TIME = dt.datetime(2010, 8, 1, 12, 0, 0)
END_TIME = dt.datetime(2010, 8, 1, 12, 1, 0)
ARGS = ["starttime=" + START_TIME.isoformat(timespec="seconds") + "Z",
        "endtime=" + END_TIME.isoformat(timespec="seconds") + "Z"]


@pytest.mark.network
def test_lightning():
    """Test parsing lightning data."""
    from fmiopendata.lightning import download_and_parse

    # The "simple" format
    res = download_and_parse("fmi::observations::lightning::simple", args=ARGS)
    num = len(res.latitudes)
    assert num > 0
    assert num == len(res.longitudes) == len(res.times) == len(res.cloud_indicator)
    assert num == len(res.ellipse_major) == len(res.multiplicity) == len(res.peak_current)

    # Make sure the times are within the specified time frame
    start_time = min(res.times)
    end_time = max(res.times)
    assert start_time >= START_TIME
    assert end_time <= END_TIME

    # The multipoint coverage format
    res2 = download_and_parse("fmi::observations::lightning::multipointcoverage", args=ARGS)

    # The results should be identical
    assert np.all(res.latitudes == res2.latitudes)
    assert np.all(res.longitudes == res2.longitudes)
    assert np.all(res.times == res2.times)
    assert np.all(res.cloud_indicator == res2.cloud_indicator)
    assert np.all(res.ellipse_major == res2.ellipse_major)
    assert np.all(res.multiplicity == res2.multiplicity)
    assert np.all(res.peak_current == res2.peak_current)


@mock.patch("fmiopendata.lightning.ET")
@mock.patch("fmiopendata.lightning.read_url")
def test_unimplemented(read_url, ET):
    """Test lightning format that has not been implemented."""
    from fmiopendata.lightning import download_and_parse

    with pytest.raises(NotImplementedError):
        _ = download_and_parse("fmi::observations::lightning::nonexistent", args=ARGS)


def test_no_data():
    """Test that missing data is handled properly."""
    from fmiopendata.lightning import Lightning

    empty_xml = "<xml></xml>"
    # "::simple" data
    obs = Lightning(empty_xml, "simple")
    _check_lightning_empty(obs)

    # "::multipointcoverage" data
    obs = Lightning(empty_xml, "multipointcoverage")
    _check_lightning_empty(obs)


def _check_lightning_empty(obs):
    np.testing.assert_equal(obs.latitudes, np.array([]))
    np.testing.assert_equal(obs.longitudes, np.array([]))
    np.testing.assert_equal(obs.times, np.array([]))
    np.testing.assert_equal(obs.multiplicity, np.array([], dtype=np.uint8))
    np.testing.assert_equal(obs.peak_current, np.array([]))
    np.testing.assert_equal(obs.cloud_indicator, np.array([], dtype=np.uint8))
    np.testing.assert_equal(obs.ellipse_major, np.array([]))


SIMPLE_MEMBER = """  <wfs:member>
    <BsWfs:BsWfsElement gml:id="BsWfsElement.%d.%d">
      <BsWfs:Time>%s</BsWfs:Time>
      <BsWfs:Location><gml:Point><gml:pos>%s</gml:pos></gml:Point></BsWfs:Location>
      <BsWfs:ParameterName>%s</BsWfs:ParameterName>
      <BsWfs:ParameterValue>%s</BsWfs:ParameterValue>
    </BsWfs:BsWfsElement>
  </wfs:member>
"""
SIMPLE_HEADER = """<?xml version="1.0" encoding="UTF-8"?>
<wfs:FeatureCollection xmlns:wfs="http://www.opengis.net/wfs/2.0"
                       xmlns:BsWfs="http://xml.fmi.fi/schema/wfs/2.0"
                       xmlns:gml="http://www.opengis.net/gml/3.2">
"""


def _simple_xml(flashes):
    """Build a "simple" format document out of (flash id, time, position, parameters)."""
    members = []
    for flash_id, tim, position, parameters in flashes:
        for i, (name, value) in enumerate(parameters):
            members.append(SIMPLE_MEMBER % (flash_id, i + 1, tim, position, name, value))

    return SIMPLE_HEADER + "".join(members) + "</wfs:FeatureCollection>"


def test_simple_stays_aligned():
    """Test that a repeated or missing parameter does not shift the arrays."""
    from fmiopendata.lightning import Lightning

    xml = _simple_xml([
        # The service repeats the multiplicity of the first flash
        (1, "2010-08-01T12:00:00Z", "60.1 24.9",
         [("multiplicity", "3"), ("peak_current", "-12.5"), ("cloud_indicator", "0"),
          ("ellipse_major", "1.5"), ("multiplicity", "3")]),
        # ...and leaves out the ellipse of the second one
        (2, "2010-08-01T12:00:30Z", "61.1 25.9",
         [("multiplicity", "1"), ("peak_current", "8.0"), ("cloud_indicator", "1")]),
    ])

    obs = Lightning(xml, "simple")

    np.testing.assert_allclose(obs.latitudes, [60.1, 61.1])
    np.testing.assert_allclose(obs.longitudes, [24.9, 25.9])
    assert list(obs.times) == [dt.datetime(2010, 8, 1, 12, 0, 0),
                               dt.datetime(2010, 8, 1, 12, 0, 30)]
    np.testing.assert_allclose(obs.multiplicity, [3, 1])
    np.testing.assert_allclose(obs.peak_current, [-12.5, 8.0])
    np.testing.assert_allclose(obs.cloud_indicator, [0, 1])
    # The flash the service gave no ellipse for has no ellipse, and the other one is
    # still where it belongs
    np.testing.assert_allclose(obs.ellipse_major, [1.5, np.nan])
