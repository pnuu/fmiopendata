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

"""Test WMS capabilities parsing."""

import datetime as dt
from unittest import mock

import pytest

CAPABILITIES = """<?xml version="1.0" encoding="UTF-8"?>
<WMS_Capabilities xmlns="http://www.opengis.net/wms" version="1.3.0">
  <Capability>
    <Layer>
      <Title>All the layers</Title>
      <Layer queryable="1">
        <Name>Radar:test_dbzh</Name>
        <Title>Test radar reflectivity</Title>
        <Abstract>Reflectivity from a test radar</Abstract>
        <CRS>EPSG:3067</CRS>
        <CRS>CRS:84</CRS>
        <BoundingBox CRS="EPSG:3067" minx="1.0" miny="2.0" maxx="3.0" maxy="4.0"/>
        <Dimension name="time" units="ISO8601">%s</Dimension>
        <Dimension name="elevation" units="m">0.3,1.5</Dimension>
      </Layer>
    </Layer>
  </Capability>
</WMS_Capabilities>
"""
TIME_DIMENSION = "2026-09-01T00:00:00.000Z/2026-09-01T01:00:00.000Z/PT15M"


def _get_layer(time_dimension=TIME_DIMENSION):
    """Parse the test capabilities and return the only named layer in them."""
    from fmiopendata.wms import get_wms_layers

    with mock.patch("fmiopendata.wms.read_url",
                    return_value=CAPABILITIES % time_dimension):
        layers = get_wms_layers()

    assert list(layers) == ["Radar:test_dbzh"]

    return layers["Radar:test_dbzh"]


def test_layer_metadata():
    """Test that the layer metadata are collected."""
    layer = _get_layer()

    assert layer.name == "Radar:test_dbzh"
    assert layer.title == "Test radar reflectivity"
    assert layer.abstract == "Reflectivity from a test radar"
    # Only the EPSG coordinate reference systems are collected
    assert layer.crs == ["EPSG:3067"]
    assert len(layer.bbox) == 1
    assert layer.bbox[0]["minx"] == "1.0"
    assert layer.elevations == ["0.3", "1.5"]


def test_times():
    """Test the time dimension of a layer."""
    layer = _get_layer()

    assert layer.start_time == dt.datetime(2026, 9, 1, 0, 0)
    assert layer.end_time == dt.datetime(2026, 9, 1, 1, 0)
    assert layer.time_step == dt.timedelta(minutes=15)
    assert layer.time_step_str == "15 minute time step"

    times = layer.times
    assert times[0] == layer.start_time
    assert times[-1] == layer.end_time
    assert len(times) == 5
    assert list(layer.iter_times()) == times


def test_unhandled_time_step():
    """Test a time step that cannot be handled."""
    with pytest.warns(UserWarning, match="P1D"):
        layer = _get_layer(time_dimension="2026-09-01T00:00:00.000Z/2026-09-08T00:00:00.000Z/P1D")

    assert layer.time_step is None
    assert layer.time_step_str is None
    assert layer.times == []


def test_incomplete_layer():
    """Test a layer whose elements are missing their text and attributes."""
    from fmiopendata.wms import get_wms_layers

    capabilities = ("""<?xml version="1.0" encoding="UTF-8"?>
<WMS_Capabilities xmlns="http://www.opengis.net/wms" version="1.3.0">
  <Capability>
    <Layer>
      <Layer>
        <Name>Test:incomplete</Name>
        <Title>Incomplete layer</Title>
        <CRS/>
        <BoundingBox minx="1.0" miny="2.0" maxx="3.0" maxy="4.0"/>
        <Dimension units="m"/>
      </Layer>
    </Layer>
  </Capability>
</WMS_Capabilities>
""")
    with mock.patch("fmiopendata.wms.read_url", return_value=capabilities):
        layers = get_wms_layers()

    layer = layers["Test:incomplete"]
    assert layer.crs == []
    assert layer.bbox == []
    assert layer.elevations is None
    assert layer.times == []


def test_repr():
    """Test the printed form of a layer."""
    layer = _get_layer()

    assert repr(layer) == "Radar:test_dbzh - 15 minute time step, elevations: 0.3, 1.5"

    layer.elevations = None
    assert repr(layer) == "Radar:test_dbzh - 15 minute time step"

    layer.time_step_str = None
    assert repr(layer) == "Radar:test_dbzh - no timesteps"
