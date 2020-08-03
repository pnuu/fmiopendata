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

"""Test multipoint coverage parsers."""

import datetime as dt


ARGS = ["bbox=24,59,26,61",
        "starttime=2020-07-07T12:00:00Z",
        "endtime=2020-07-07T12:05:00Z"]


def test_multipoint_weather():
    """Test multipoint coverage parser for weather station data."""
    from fmiopendata.multipoint import download_and_parse

    res = download_and_parse("fmi::observations::weather::multipointcoverage",
                             args=ARGS)
    latest = max(res.data.keys())
    assert isinstance(latest, dt.datetime)
    data = res.data[latest]

    # Take the first location by alphabetic name
    loc = min(data.keys())
    assert isinstance(loc, str)
    loc_data = data[loc]

    # Every measurement should have a value and unit
    for measurement in loc_data.keys():
        assert "value" in loc_data[measurement]
        assert "units" in loc_data[measurement]

    # Check that location metadata are available
    meta = res.location_metadata[loc]
    assert isinstance(meta["fmisid"], int)
    assert isinstance(meta["latitude"], float)
    assert isinstance(meta["longitude"], float)


def test_multipoint_radionuclide():
    """Test multipoint coverage parser for radionuclide data."""
    from fmiopendata.multipoint import download_and_parse

    res = download_and_parse("stuk::observations::air::radionuclide-activity-concentration::latest::multipointcoverage",
                             args=ARGS)

    latest = max(res.data.keys())
    assert isinstance(latest, dt.datetime)
    data = res.data[latest]

    # Take the first location by alphabetic name
    loc = min(data.keys())
    assert isinstance(loc, str)
    loc_data = data[loc]

    # Every measurement should have a value and unit
    for measurement in loc_data.keys():
        assert "value" in loc_data[measurement]
        assert "units" in loc_data[measurement]

    # Check that location metadata are available
    meta = res.location_metadata[loc]
    assert isinstance(meta["fmisid"], int)
    assert isinstance(meta["latitude"], float)
    assert isinstance(meta["longitude"], float)
