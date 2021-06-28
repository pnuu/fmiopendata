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

START_TIME = dt.datetime(2020, 7, 7, 12, 0, 0)
START_TIME_OLD = dt.datetime(1969, 7, 7)
END_TIME = dt.datetime(2020, 7, 7, 12, 5, 0)
END_TIME_OLD = dt.datetime(1969, 7, 17)

ARGS = ["bbox=24,59,26,61",
        "starttime=" + START_TIME.isoformat(timespec="seconds") + "Z",
        "endtime=" + END_TIME.isoformat(timespec="seconds") + "Z"]
ARGS_OLD = ["bbox=24,59,26,61",
            "starttime=" + START_TIME_OLD.isoformat(timespec="seconds") + "Z",
            "endtime=" + END_TIME_OLD.isoformat(timespec="seconds") + "Z"]
ARGS_TIMESERIES = ["bbox=24,59,26,61", "timeseries=True"]


def test_multipoint_mareograph_default():
    """Test multipoint coverage parser for default query of mareograph data."""
    from fmiopendata.multipoint import download_and_parse

    res = download_and_parse("fmi::observations::mareograph::multipointcoverage")
    _verify_multipoint_common(res)


def _verify_multipoint_common(res):
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


def test_multipoint_weather():
    """Test multipoint coverage parser for weather station data."""
    from fmiopendata.multipoint import download_and_parse

    res = download_and_parse("fmi::observations::weather::multipointcoverage",
                             args=ARGS)
    _verify_multipoint_common(res)

    # Make sure the times are within the specified time frame
    start_time = min(res.data.keys())
    end_time = max(res.data.keys())
    assert start_time >= START_TIME
    assert end_time <= END_TIME


def test_old_multipoint_daily_weather():
    """Test multipoint coverage parser for daily weather station data for pre-1970s."""
    from fmiopendata.multipoint import download_and_parse

    res = download_and_parse("fmi::observations::weather::daily::multipointcoverage",
                             args=ARGS_OLD)
    # Make sure the times are within the specified time frame
    start_time = min(res.data.keys())
    end_time = max(res.data.keys())
    assert start_time >= START_TIME_OLD
    assert end_time <= END_TIME_OLD


def test_multipoint_weather_timeseries():
    """Test multipoint coverage parser for weather station data in timeseries mode."""
    from fmiopendata.multipoint import download_and_parse

    res = download_and_parse("fmi::observations::weather::multipointcoverage",
                             args=ARGS_TIMESERIES)

    for loc in res.location_metadata:
        assert "fmisid" in res.location_metadata[loc]
        assert "latitude" in res.location_metadata[loc]
        assert "longitude" in res.location_metadata[loc]

    for loc in res.data:
        len_times = len(res.data[loc]["times"])
        for measurement in res.data[loc]:
            if measurement == "times":
                continue
            assert len(res.data[loc][measurement]["values"]) == len_times
            assert "unit" in res.data[loc][measurement]


def test_multipoint_radionuclide():
    """Test multipoint coverage parser for radionuclide data."""
    from fmiopendata.multipoint import download_and_parse

    res = download_and_parse("stuk::observations::air::radionuclide-activity-concentration::latest::multipointcoverage",
                             args=ARGS)
    _verify_multipoint_common(res)
