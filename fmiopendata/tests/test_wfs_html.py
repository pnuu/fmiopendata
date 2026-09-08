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

"""Test the WFS catalogue writer."""

import io
from unittest import mock

PROPERTIES = """<?xml version="1.0" encoding="UTF-8"?>
<omop:ObservablePropertyCollection xmlns:omop="http://inspire.ec.europa.eu/schemas/omop/2.9"
                                   xmlns:gml="http://www.opengis.net/gml/3.2">
  <omop:component>
    <omop:ObservableProperty gml:id="t2m">
      <omop:label>Air temperature</omop:label>
      <omop:uom uom="degC"/>
    </omop:ObservableProperty>
  </omop:component>
  <omop:component>
    <omop:ObservableProperty gml:id="aero_pt1s_avg">
      <omop:label>AERO-telegram</omop:label>
    </omop:ObservableProperty>
  </omop:component>
</omop:ObservablePropertyCollection>
"""


def test_get_observable_properties():
    """Test reading the parameters a query can be asked for."""
    from fmiopendata.wfs_html import get_observable_properties

    with mock.patch("fmiopendata.wfs_html.read_url", return_value=PROPERTIES):
        properties = get_observable_properties()

    # Sorted by id, and a property without a unit is still listed
    assert properties == [{"id": "aero_pt1s_avg", "label": "AERO-telegram", "unit": ""},
                          {"id": "t2m", "label": "Air temperature", "unit": "degC"}]


def test_write_properties_md():
    """Test the parameter table of the markdown catalogue."""
    from fmiopendata.wfs_html import write_properties_md

    fid = io.StringIO()
    write_properties_md(fid, [{"id": "t2m", "label": "Air temperature", "unit": "degC"}])

    lines = fid.getvalue().strip().split("\n")
    assert lines[0] == "# Available parameters"
    assert lines[-2] == "| --- | --- | --- |"
    assert lines[-1] == "| `t2m` | Air temperature | degC |"


def test_calibration_function():
    """Test how a calibration is described."""
    from fmiopendata.wfs_html import _calibration_function

    dataset = mock.Mock(_gain=0.5, _offset=-32.0)
    assert _calibration_function(dataset) == "y = 0.5 * x - 32.0"

    dataset = mock.Mock(_gain=0.01, _offset=0.5)
    assert _calibration_function(dataset) == "y = 0.01 * x + 0.5"

    # A dataset that is not calibrated has no function to describe
    assert _calibration_function(mock.Mock(_gain=None, _offset=None)) is None
    assert _calibration_function(mock.Mock(_gain=0.5, _offset=None)) is None


def test_calibration_of_an_uncalibrated_query():
    """Test that only the calibrated queries are asked for their coefficients."""
    from fmiopendata.wfs_html import get_calibration

    with mock.patch("fmiopendata.wfs_html.read_url") as read_url:
        assert get_calibration("fmi::observations::weather::multipointcoverage") == []

    read_url.assert_not_called()


def test_write_calibration_md():
    """Test how a calibration is written into the markdown catalogue."""
    from fmiopendata.wfs_html import write_calibration_md

    calibration = [{"name": "dbz", "label": "Radar reflectivity", "unit": "dBZ",
                    "function": "y = 0.5 * x - 32.0"}]
    fid = io.StringIO()
    with mock.patch("fmiopendata.wfs_html.get_calibration", return_value=calibration):
        write_calibration_md(fid, "fmi::radar::composite::dbz")

    assert fid.getvalue() == ("* Calibration:\n"
                              "    * dbz (Radar reflectivity)\n"
                              "        * Calibrated unit: dBZ\n"
                              "        * Calibration: y = 0.5 * x - 32.0\n")
