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

"""Test grid parsers."""

import datetime as dt
import os
import time

import pytest

# Small box around Helsinki, only temperature
ARGS = ["bbox=24,59,26,61", "parameters=temperature"]


def test_grid():
    """Test parsing grid data."""
    from fmiopendata.grid import download_and_parse

    res = download_and_parse("fmi::forecast::harmonie::surface::grid", args=ARGS)
    assert res.data is not None

    # Take the latest model run
    latest = max(res.data.keys())
    assert isinstance(latest, dt.datetime)
    data = res.data[latest]

    # No data has been downloaded
    assert not data.data
    assert data.latitudes is None
    assert data.longitudes is None

    # Some metadata should be available
    assert data.init_time == latest
    assert isinstance(data.start_time, dt.datetime)
    assert isinstance(data.end_time, dt.datetime)
    assert data.url is not None

    # Download and parse the data, delete the file
    data.parse(delete=True)
    assert not os.path.exists(data._fname)

    init_time = min(data.data.keys())
    assert isinstance(init_time, dt.datetime)
    init_data = data.data[init_time]

    # Only 2 metre temperature should be available
    assert len(init_data) == 1
    assert 2 in init_data
    assert len(init_data[2]) == 1
    t2m = init_data[2]["2 metre temperature"]
    assert "data" in t2m
    assert "units" in t2m

    shp = t2m["data"].shape
    assert shp == data.longitudes.shape == data.latitudes.shape

    # Another call to .download() and .parse() should be near instantaneous, as nothing is done
    tic = time.time()
    data.parse()
    toc = time.time()
    assert toc - tic < 1e-3

    tic = time.time()
    data.download()
    toc = time.time()
    assert toc - tic < 1e-3

    # Only a parser for "grib" format has been implemented
    earliest = min(res.data.keys())
    data = res.data[earliest]
    # Fake the URL
    data.url = "format=netcdf"
    with pytest.raises(NotImplementedError):
        data.parse()
