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

"""Test radar parsers."""

import mock

import numpy as np


def test_single_vrad():
    """Test radar radial velocity."""
    from fmiopendata.radar import download_and_parse

    res = download_and_parse("fmi::radar::single::vrad")
    assert len(res.data) == len(res.times)

    data = res.data[0]
    # Check that only correct attributes are set
    assert data.label is not None
    assert data.max_velocity is not None
    assert data.elevation is not None
    assert data.name == "vrad"
    assert data.projection is not None
    assert data.time == res.times[0]
    assert data.unit == "m/s"
    assert data.url is not None
    assert data.etop_threshold is None
    assert data.data is None
    assert data._gain is not None
    assert data._offset is not None

    # Download the data
    data.download()
    assert data.data is not None
    assert data.data.dtype == np.uint8

    # Check the area mask before calibration
    area_mask = data.get_area_mask()
    # Corners are always masked
    assert area_mask[0, 0, 0]
    # Not everything should be masked
    assert np.sum(area_mask) < area_mask.size

    # Check the data mask before calibration
    data_mask = data.get_data_mask()
    # The corners should not be masked in this case
    assert not data_mask[0, 0, 0]
    # There ought to be some masked data (no wind detected)
    assert np.sum(data_mask) > 0

    # Calibrate the data
    data.calibrate()
    assert data.data.dtype == np.float64
    assert data.data.max() <= data.max_velocity

    # Check the area mask after calibration
    area_mask2 = data.get_area_mask()
    # Corners are always masked
    assert area_mask2[0, 0, 0]
    # Not everything should be masked
    assert np.sum(area_mask2) < area_mask2.size
    assert np.all(area_mask == area_mask2)

    # Check the data mask after calibration
    data_mask2 = data.get_data_mask()
    # The corners should not be masked in this case
    assert not data_mask2[0, 0, 0]
    # There ought to be some masked data (no wind detected)
    assert np.sum(data_mask2) > 0
    assert np.all(area_mask == area_mask2)


def test_single_dbz():
    """Test radar reflectivity dBZ."""
    from fmiopendata.radar import download_and_parse

    res = download_and_parse("fmi::radar::single::dbz")
    assert len(res.data) == len(res.times)

    data = res.data[0]
    # Check that only correct attributes are set
    assert data.label is not None
    assert data.max_velocity is None
    assert data.elevation is not None
    assert data.name == "dbz"
    assert data.projection is not None
    assert data.time == res.times[0]
    assert data.unit == "dBZ"
    assert data.url is not None
    assert data.etop_threshold is None
    assert data.data is None
    assert data._gain is not None
    assert data._offset is not None

    # Download the data
    data.download()
    assert data.data is not None
    assert data.data.dtype == np.uint8

    # Check the area mask before calibration
    area_mask = data.get_area_mask()
    # Corners are always masked
    assert area_mask[0, 0, 0]
    # Not everything should be masked
    assert np.sum(area_mask) < area_mask.size

    # Check the data mask before calibration
    data_mask = data.get_data_mask()
    # The corners should not be masked in this case
    assert not data_mask[0, 0, 0]
    # There ought to be some masked data (no rain detected)
    assert np.sum(data_mask) > 0

    # Calibrate the data
    data.calibrate()
    assert data.data.dtype == np.float64

    # Check the area mask after calibration
    area_mask2 = data.get_area_mask()
    # Corners are always masked
    assert area_mask2[0, 0, 0]
    # Not everything should be masked
    assert np.sum(area_mask2) < area_mask2.size
    assert np.all(area_mask == area_mask2)

    # Check the data mask after calibration
    data_mask2 = data.get_data_mask()
    # The corners should not be masked in this case
    assert not data_mask2[0, 0, 0]
    # There ought to be some masked data (no rain detected)
    assert np.sum(data_mask2) > 0
    assert np.all(data_mask == data_mask2)


def test_single_hclass():
    """Test radar hydroclass."""
    from fmiopendata.radar import download_and_parse

    res = download_and_parse("fmi::radar::single::hclass")
    assert len(res.data) == len(res.times)

    data = res.data[0]
    # Check that only correct attributes are set
    assert data.label is not None
    assert data.max_velocity is None
    assert data.elevation is not None
    assert data.name == "hclass"
    assert data.projection is not None
    assert data.time == res.times[0]
    assert data.unit == "Index"
    assert data.url is not None
    assert data.etop_threshold is None
    assert data.data is None
    assert data._gain is not None
    assert data._offset is not None

    # Download the data
    data.download()
    assert data.data is not None
    assert data.data.dtype == np.uint8

    # Check the area mask before calibraion
    area_mask = data.get_area_mask()
    # Corners are always masked
    assert area_mask[0, 0, 0]
    # Not everything should be masked
    assert np.sum(area_mask) < area_mask.size

    # Check the data mask before calibraion
    data_mask = data.get_data_mask()
    # The corners should not be masked in this case
    assert not data_mask[0, 0, 0]
    # There ought to be some masked data (no hydrometeors detected)
    assert np.sum(data_mask) > 0

    # Calibrate the data
    data.calibrate()
    assert data.data.dtype == np.float64

    # Check the area mask after calibration
    area_mask2 = data.get_area_mask()
    # Corners are always masked
    assert area_mask2[0, 0, 0]
    # Not everything should be masked
    assert np.sum(area_mask2) < area_mask2.size
    assert np.all(area_mask == area_mask2)

    # Check the data mask after calibraion
    data_mask2 = data.get_data_mask()
    # The corners should not be masked in this case
    assert not data_mask2[0, 0, 0]
    # There ought to be some masked data (no hydrometeors detected)
    assert np.sum(data_mask2) > 0
    assert np.all(data_mask == data_mask2)


def test_single_etop_20():
    """Test radar hydroclass."""
    from fmiopendata.radar import download_and_parse

    res = download_and_parse("fmi::radar::single::etop_20")
    assert len(res.data) == len(res.times)

    data = res.data[0]
    # Check that only correct attributes are set
    assert data.label is not None
    assert data.max_velocity is None
    assert data.elevation is None
    assert data.name == "etop"
    assert data.projection is not None
    assert data.time == res.times[0]
    assert data.unit == "m"
    assert data.url is not None
    assert data.etop_threshold is not None
    assert data.data is None
    assert data._gain is not None
    assert data._offset is not None

    # Download the data
    data.download()
    assert data.data is not None
    assert data.data.dtype == np.uint8

    # Check the area mask before calibration
    area_mask = data.get_area_mask()
    # Corners are always masked
    assert area_mask[0, 0, 0]
    # Not everything should be masked
    assert np.sum(area_mask) < area_mask.size

    # Check the data mask before calibration
    data_mask = data.get_data_mask()
    # The corners should not be masked in this case
    assert not data_mask[0, 0, 0]
    # There ought to be some masked data (no clouds detected)
    assert np.sum(data_mask) > 0

    # Calibrate the data
    data.calibrate()
    assert data.data.dtype == np.float64

    # Check the area mask after calibration
    area_mask2 = data.get_area_mask()
    # Corners are always masked
    assert area_mask2[0, 0, 0]
    # Not everything should be masked
    assert np.sum(area_mask2) < area_mask2.size
    assert np.all(area_mask == area_mask2)

    # Check the data mask after calibration
    data_mask2 = data.get_data_mask()
    # The corners should not be masked in this case
    assert not data_mask2[0, 0, 0]
    # There ought to be some masked data (no clouds detected)
    assert np.sum(data_mask2) > 0
    assert np.all(data_mask == data_mask2)


def test_composite_dbz():
    """Test radar composite dBZ."""
    from fmiopendata.radar import download_and_parse

    res = download_and_parse("fmi::radar::composite::dbz")
    assert len(res.data) == len(res.times)

    data = res.data[0]
    # Check that only correct attributes are set
    assert data.label is not None
    assert data.max_velocity is None
    assert data.elevation is None
    assert data.name == "dbz"
    assert data.projection is not None
    assert data.time == res.times[0]
    assert data.unit == "dBZ"
    assert data.url is not None
    assert data.etop_threshold is None
    assert data.data is None
    assert data._gain is not None
    assert data._offset is not None

    # Download the data
    data.download()
    assert data.data is not None
    assert data.data.dtype == np.uint8

    # Check the area mask before calibration
    area_mask = data.get_area_mask()
    # Corners are always masked
    assert area_mask[0, 0, 0]
    # Not everything should be masked
    assert np.sum(area_mask) < area_mask.size

    # Check the data mask before calibration
    data_mask = data.get_data_mask()
    # The corners should not be masked in this case
    assert not data_mask[0, 0, 0]
    # There ought to be some masked data (no rain detected)
    assert np.sum(data_mask) > 0

    # Calibrate the data
    data.calibrate()
    assert data.data.dtype == np.float64

    # Check the area mask after calibration
    area_mask2 = data.get_area_mask()
    # Corners are always masked
    assert area_mask2[0, 0, 0]
    # Not everything should be masked
    assert np.sum(area_mask2) < area_mask2.size
    assert np.all(area_mask == area_mask2)

    # Check the data mask after calibration
    data_mask2 = data.get_data_mask()
    # The corners should not be masked in this case
    assert not data_mask2[0, 0, 0]
    # There ought to be some masked data (no rain detected)
    assert np.sum(data_mask2) > 0
    assert np.all(data_mask == data_mask2)


def _check_rr(data, name=None, unit=None):
    """Check the rr products."""
    # Check that only correct attributes are set
    assert data.label is not None
    assert data.max_velocity is None
    assert data.elevation is None
    assert data.name == name
    assert data.projection is not None
    assert data.unit == unit
    assert data.url is not None
    assert data.etop_threshold is None
    assert data.data is None
    assert data._gain is not None
    assert data._offset is not None

    # Download the data
    data.download()
    assert data.data is not None
    assert data.data.dtype == np.uint16

    # Check the area mask before calibration
    area_mask = data.get_area_mask()
    # Corners are always masked
    assert area_mask[0, 0, 0]
    # Not everything should be masked
    assert np.sum(area_mask) < area_mask.size

    # Check the data mask before calibration
    data_mask = data.get_data_mask()
    # The corners should not be masked in this case
    assert not data_mask[0, 0, 0]
    # There ought to be some masked data (no rain detected)
    assert np.sum(data_mask) > 0

    # Calibrate the data
    data.calibrate()
    assert data.data.dtype == np.float64

    # Check the area mask after calibration
    area_mask2 = data.get_area_mask()
    # Corners are always masked
    assert area_mask2[0, 0, 0]
    # Not everything should be masked
    assert np.sum(area_mask2) < area_mask2.size
    assert np.all(area_mask == area_mask2)

    # Check the data mask after calibration
    data_mask2 = data.get_data_mask()
    # The corners should not be masked in this case
    assert not data_mask2[0, 0, 0]
    # There ought to be some masked data (no rain detected)
    assert np.sum(data_mask2) > 0
    assert np.all(data_mask == data_mask2)


def test_composite_rr():
    """Test radar composite rain rate."""
    from fmiopendata.radar import download_and_parse

    res = download_and_parse("fmi::radar::composite::rr")
    assert len(res.data) == len(res.times)

    data = res.data[0]
    assert data.time == res.times[0]

    _check_rr(data, name="rr", unit="mm/h")


def test_composite_rr1h():
    """Test radar composite 1 hour accumulated rain rainfall."""
    from fmiopendata.radar import download_and_parse

    res = download_and_parse("fmi::radar::composite::rr1h")
    assert len(res.data) == len(res.times)

    data = res.data[0]
    assert data.time == res.times[0]

    _check_rr(data, name="rr1h", unit="mm")


def test_composite_rr12h():
    """Test radar composite 12 hour accumulated rain rainfall."""
    from fmiopendata.radar import download_and_parse

    res = download_and_parse("fmi::radar::composite::rr12h")
    assert len(res.data) == len(res.times)

    data = res.data[0]
    assert data.time == res.times[0]

    _check_rr(data, name="rr12h", unit="mm")


def test_composite_rr24h():
    """Test radar composite 24 hour accumulated rain rainfall."""
    from fmiopendata.radar import download_and_parse

    res = download_and_parse("fmi::radar::composite::rr24h")
    assert len(res.data) == len(res.times)

    data = res.data[0]
    assert data.time == res.times[0]

    _check_rr(data, name="rr24h", unit="mm")


@mock.patch("fmiopendata.radar.ParseRadar")
@mock.patch("fmiopendata.radar.read_url")
def test_args(read_url, ParseRadar):
    """Test that arguments are passed properly."""
    from fmiopendata.radar import download_and_parse

    res = download_and_parse("foo", args=["a=1", "b=2"])
    del res
    assert read_url.mock_calls[0].endswith("=foo&a=1&b=2")
