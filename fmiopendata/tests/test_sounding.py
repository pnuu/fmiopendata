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

from unittest import mock


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


@mock.patch("fmiopendata.sounding.ParseSoundings")
@mock.patch("fmiopendata.sounding.read_url")
def test_args(read_url, ParseSoundings):
    """Test that arguments are passed properly."""
    from fmiopendata.sounding import download_and_parse

    res = download_and_parse("foo", args=["a=1", "b=2"])
    del res
    assert read_url.mock_calls[0].endswith("=foo&a=1&b=2")
