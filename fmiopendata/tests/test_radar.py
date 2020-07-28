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

import numpy as np

from fmiopendata.radar import download_and_parse


def test_vrad():
    """Test radar radial velocity."""
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

    # Calibrate the data
    data.calibrate()
    assert data.data.dtype == np.float64
    assert data.data.max() <= data.max_velocity

    # Check the area mask
    area_mask = data.get_area_mask()
    # Corners are always masked
    assert area_mask[0, 0, 0] == True
    # Not everything should be masked
    assert np.sum(area_mask) < area_mask.size

    # Check the data mask
    data_mask = data.get_data_mask()
    # The corners should not be masked in this case
    assert data_mask[0, 0, 0] == False
    # There ought to be some masked data (no wind detected)
    assert np.sum(data_mask) > 0


def test_dbz():
    """Test radar reflectivity dBZ."""
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

    # Calibrate the data
    data.calibrate()
    assert data.data.dtype == np.float64

    # Check the area mask
    area_mask = data.get_area_mask()
    # Corners are always masked
    assert area_mask[0, 0, 0] == True
    # Not everything should be masked
    assert np.sum(area_mask) < area_mask.size

    # Check the data mask
    data_mask = data.get_data_mask()
    # The corners should not be masked in this case
    assert data_mask[0, 0, 0] == False
    # There ought to be some masked data (no rain detected)
    assert np.sum(data_mask) > 0


def test_hclass():
    """Test radar hydroclass."""
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

    # Calibrate the data
    data.calibrate()
    assert data.data.dtype == np.float64

    # Check the area mask
    area_mask = data.get_area_mask()
    # Corners are always masked
    assert area_mask[0, 0, 0] == True
    # Not everything should be masked
    assert np.sum(area_mask) < area_mask.size

    # Check the data mask
    data_mask = data.get_data_mask()
    # The corners should not be masked in this case
    assert data_mask[0, 0, 0] == False
    # There ought to be some masked data (no hydrometeors detected)
    assert np.sum(data_mask) > 0


def test_etop_20():
    """Test radar hydroclass."""
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

    # Calibrate the data
    data.calibrate()
    assert data.data.dtype == np.float64

    # Check the area mask
    area_mask = data.get_area_mask()
    # Corners are always masked
    assert area_mask[0, 0, 0] == True
    # Not everything should be masked
    assert np.sum(area_mask) < area_mask.size

    # Check the data mask
    data_mask = data.get_data_mask()
    # The corners should not be masked in this case
    assert data_mask[0, 0, 0] == False
    # There ought to be some masked data (no clouds detected)
    assert np.sum(data_mask) > 0
