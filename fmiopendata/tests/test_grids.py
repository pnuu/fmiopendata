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
import gc
import os
import shutil
from unittest import mock

import numpy as np
import pytest

# Small box around Helsinki, only temperature
ARGS = ["bbox=24,59,26,61", "parameters=temperature"]


@pytest.mark.network
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

    # Another call to .parse() and .download() does not fetch or parse anything again
    with mock.patch("fmiopendata.grid.download_to_file") as download_to_file:
        data.parse()
        data.download()
    download_to_file.assert_not_called()

    # Only a parser for "grib" format has been implemented
    earliest = min(res.data.keys())
    data = res.data[earliest]
    # Fake the URL
    data.url = "format=netcdf"
    with pytest.raises(NotImplementedError):
        data.parse()


GRID_XML = """<?xml version="1.0" encoding="UTF-8"?>
<wfs:FeatureCollection xmlns:wfs="http://www.opengis.net/wfs/2.0"
                       xmlns:gml="http://www.opengis.net/gml/3.2">
  <wfs:member>
    <gml:timePosition>2026-09-08T12:00:00Z</gml:timePosition>
    <gml:beginPosition>2026-09-08T12:00:00Z</gml:beginPosition>
    <gml:endPosition>2026-09-11T06:00:00Z</gml:endPosition>
    <gml:fileReference>https://opendata.fmi.fi/download?producer=test&amp;format=grib2</gml:fileReference>
  </wfs:member>
</wfs:FeatureCollection>
"""
MISSING_VALUE = 9999.0


def _write_grib(fname, messages=(("2t", 2),)):
    """Write a small GRIB2 file, one message per (short name, level) given."""
    import eccodes

    with open(fname, "wb") as fid:
        for i, (short_name, level) in enumerate(messages):
            handle = eccodes.codes_grib_new_from_samples("regular_ll_sfc_grib2")
            eccodes.codes_set(handle, "Ni", 4)
            eccodes.codes_set(handle, "Nj", 3)
            eccodes.codes_set(handle, "latitudeOfFirstGridPointInDegrees", 62.0)
            eccodes.codes_set(handle, "longitudeOfFirstGridPointInDegrees", 24.0)
            eccodes.codes_set(handle, "latitudeOfLastGridPointInDegrees", 60.0)
            eccodes.codes_set(handle, "longitudeOfLastGridPointInDegrees", 27.0)
            eccodes.codes_set(handle, "iDirectionIncrementInDegrees", 1.0)
            eccodes.codes_set(handle, "jDirectionIncrementInDegrees", 1.0)
            eccodes.codes_set(handle, "shortName", short_name)
            eccodes.codes_set(handle, "level", level)
            eccodes.codes_set(handle, "dataDate", 20260908)
            eccodes.codes_set(handle, "dataTime", 1200)
            eccodes.codes_set(handle, "bitmapPresent", 1)
            eccodes.codes_set(handle, "missingValue", MISSING_VALUE)
            values = np.arange(12, dtype=float) + 270.0 + i
            # One point the model has no value for
            values[5] = MISSING_VALUE
            eccodes.codes_set_values(handle, values)
            eccodes.codes_write(handle, fid)
            eccodes.codes_release(handle)

    return fname


def _get_grid(tmp_path, messages=(("2t", 2),)):
    """Parse the test document and give back its only grid, with the data downloaded."""
    from fmiopendata.grid import ParseGrids

    res = ParseGrids(GRID_XML)
    grid = res.data[dt.datetime(2026, 9, 8, 12, 0)]

    grib = _write_grib(str(tmp_path / "test.grib2"), messages=messages)

    def fake_download(url, fname):
        shutil.copyfile(grib, fname)
        return fname, {}

    with mock.patch("fmiopendata.grid.download_to_file", side_effect=fake_download):
        grid.parse()

    return grid


def test_grid_metadata():
    """Test the metadata of a grid, which arrive before the data do."""
    from fmiopendata.grid import ParseGrids

    res = ParseGrids(GRID_XML)

    grid = res.data[dt.datetime(2026, 9, 8, 12, 0)]
    assert grid.init_time == dt.datetime(2026, 9, 8, 12, 0)
    assert grid.start_time == dt.datetime(2026, 9, 8, 12, 0)
    assert grid.end_time == dt.datetime(2026, 9, 11, 6, 0)
    assert grid.url.endswith("format=grib2")
    # Nothing has been downloaded yet
    assert not grid.data
    assert grid.latitudes is None


def test_grib_parsing(tmp_path):
    """Test parsing a GRIB file without downloading one."""
    grid = _get_grid(tmp_path)

    valid_time = dt.datetime(2026, 9, 8, 12, 0)
    assert list(grid.data) == [valid_time]
    assert list(grid.data[valid_time]) == [2]

    dataset = grid.data[valid_time][2]["2 metre temperature"]
    assert dataset["units"] == "K"
    assert dataset["data"].shape == (3, 4) == grid.latitudes.shape == grid.longitudes.shape
    # The value the model does not have is not the number the file carries for it
    assert np.isnan(dataset["data"][1, 1])
    assert not np.any(dataset["data"] == MISSING_VALUE)
    np.testing.assert_allclose(dataset["data"][0], [270.0, 271.0, 272.0, 273.0])
    np.testing.assert_allclose(grid.latitudes[:, 0], [62.0, 61.0, 60.0])


def test_temporary_file_is_removed(tmp_path):
    """Test that a grid cleans up the file it downloaded for itself."""
    grid = _get_grid(tmp_path)
    fname = grid._fname
    assert os.path.exists(fname)

    del grid
    gc.collect()

    assert not os.path.exists(fname)


def test_downloading_to_another_file(tmp_path):
    """Test that the data are not quietly left where they already are."""
    grid = _get_grid(tmp_path)

    with pytest.raises(ValueError, match="already been downloaded"):
        grid.download(str(tmp_path / "elsewhere.grib2"))


def test_delete_file_without_a_download():
    """Test cleaning up a grid that was never downloaded."""
    from fmiopendata.grid import Grid

    Grid().delete_file()


def test_unsupported_format():
    """Test a data format there is no parser for."""
    from fmiopendata.grid import Grid

    grid = Grid()
    grid.url = "https://opendata.fmi.fi/download?producer=test&format=netcdf"
    with pytest.raises(NotImplementedError, match="netcdf"):
        grid.parse()

    # A URL that says nothing about the format is named as it is
    grid.url = "https://gribby.example.com/download?producer=test"
    with pytest.raises(NotImplementedError, match="gribby.example.com"):
        grid.parse()


def test_messages_that_share_a_key(tmp_path):
    """Test two messages that would land on the same name, level and time."""
    with pytest.warns(UserWarning, match="Several 2 metre temperature messages"):
        grid = _get_grid(tmp_path, messages=(("2t", 2), ("2t", 2)))

    level = grid.data[dt.datetime(2026, 9, 8, 12, 0)][2]
    # Neither message is lost, and the later one says what it is
    assert sorted(level) == ["2 metre temperature",
                             "2 metre temperature (heightAboveGround, instant)"]
    np.testing.assert_allclose(level["2 metre temperature"]["data"][0, 0], 270.0)
    np.testing.assert_allclose(
        level["2 metre temperature (heightAboveGround, instant)"]["data"][0, 0], 271.0)
