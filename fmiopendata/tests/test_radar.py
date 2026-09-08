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

import datetime as dt
import os
from unittest import mock

import numpy as np
import pytest


@pytest.mark.network
def test_single_vrad():
    """Test radar radial velocity."""
    from fmiopendata.radar import download_and_parse

    res = download_and_parse("fmi::radar::single::vrad")
    assert len(res.data) == len(res.times)

    data = res.data[0]
    # Check that only correct attributes are set
    assert data.time == res.times[0]
    assert data.max_velocity is not None
    assert data.elevation is not None
    assert data.etop_threshold is None
    _check_radar(data, name="vrad", unit="m/s", dtype=np.uint8)


@pytest.mark.xfail(raises=AssertionError, strict=True, reason="Broken WMS layer")
@pytest.mark.network
def test_single_dbz():
    """Test radar reflectivity dBZ."""
    from fmiopendata.radar import download_and_parse

    res = download_and_parse("fmi::radar::single::dbz")
    assert len(res.data) == len(res.times)

    data = res.data[0]
    # Check that only correct attributes are set
    assert data.time == res.times[0]
    assert data.max_velocity is None
    assert data.elevation is not None
    assert data.etop_threshold is None
    _check_radar(data, name="dbz", unit="dBZ", dtype=np.uint8)


@pytest.mark.xfail(raises=AssertionError, strict=True, reason="Broken WMS layer")
@pytest.mark.network
def test_single_hclass():
    """Test radar hydroclass."""
    from fmiopendata.radar import download_and_parse

    res = download_and_parse("fmi::radar::single::hclass")
    assert len(res.data) == len(res.times)

    data = res.data[0]
    # Check that only correct attributes are set
    assert data.time == res.times[0]
    assert data.max_velocity is None
    assert data.elevation is not None
    assert data.etop_threshold is None
    _check_radar(data, name="hclass", unit="Index", dtype=np.uint8)


@pytest.mark.network
def test_single_etop_20():
    """Test radar echo top height."""
    from fmiopendata.radar import download_and_parse

    res = download_and_parse("fmi::radar::single::etop_20")
    assert len(res.data) == len(res.times)

    data = res.data[0]
    # Check that only correct attributes are set
    assert data.time == res.times[0]
    assert data.max_velocity is None
    assert data.elevation is None
    assert data.etop_threshold is not None

    data = res.data[0]
    # Check that only correct attributes are set
    assert data.time == res.times[0]
    _check_radar(data, name="etop", unit="m", dtype=np.uint8)


@pytest.mark.network
def test_composite_dbz():
    """Test radar composite dBZ."""
    from fmiopendata.radar import download_and_parse

    res = download_and_parse("fmi::radar::composite::dbz")
    assert len(res.data) == len(res.times)

    data = res.data[0]
    # Check that only correct attributes are set
    assert data.time == res.times[0]
    assert data.max_velocity is None
    assert data.elevation is None
    assert data.etop_threshold is None
    _check_radar(data, name="dbz", unit="dBZ", dtype=np.uint8)


@pytest.mark.network
def test_composite_rr():
    """Test radar composite rain rate."""
    from fmiopendata.radar import download_and_parse

    res = download_and_parse("fmi::radar::composite::rr")
    assert len(res.data) == len(res.times)

    data = res.data[0]
    # Check that only correct attributes are set
    assert data.time == res.times[0]
    assert data.max_velocity is None
    assert data.elevation is None
    assert data.etop_threshold is None
    _check_radar(data, name="rr", unit="mm/h", dtype=np.uint16)


@pytest.mark.network
def test_composite_rr1h():
    """Test radar composite 1 hour accumulated rain rainfall."""
    from fmiopendata.radar import download_and_parse

    res = download_and_parse("fmi::radar::composite::rr1h")
    assert len(res.data) == len(res.times)

    data = res.data[0]
    # Check that only correct attributes are set
    assert data.time == res.times[0]
    assert data.max_velocity is None
    assert data.elevation is None
    assert data.etop_threshold is None
    _check_radar(data, name="rr1h", unit="mm", dtype=np.uint16)


@pytest.mark.network
def test_composite_rr12h():
    """Test radar composite 12 hour accumulated rain rainfall."""
    from fmiopendata.radar import download_and_parse

    res = download_and_parse("fmi::radar::composite::rr12h")
    assert len(res.data) == len(res.times)

    data = res.data[0]
    # Check that only correct attributes are set
    assert data.time == res.times[0]
    assert data.max_velocity is None
    assert data.elevation is None
    assert data.etop_threshold is None
    _check_radar(data, name="rr12h", unit="mm", dtype=np.uint16)


@pytest.mark.network
def test_composite_rr24h():
    """Test radar composite 24 hour accumulated rain rainfall."""
    from fmiopendata.radar import download_and_parse

    res = download_and_parse("fmi::radar::composite::rr24h")
    assert len(res.data) == len(res.times)

    data = res.data[0]
    # Check that only correct attributes are set
    assert data.time == res.times[0]
    assert data.max_velocity is None
    assert data.elevation is None
    assert data.etop_threshold is None
    _check_radar(data, name="rr24h", unit="mm", dtype=np.uint16)


@mock.patch("fmiopendata.radar.ParseRadar")
@mock.patch("fmiopendata.radar.read_url")
def test_args(read_url, ParseRadar):
    """Test that arguments are passed properly."""
    from fmiopendata.radar import download_and_parse

    res = download_and_parse("foo", args=["a=1", "b=2"])
    del res
    assert read_url.call_args[0][0].endswith("=foo&a=1&b=2")


def _check_radar(data, name=None, unit=None, dtype=None):
    """Check the common parts of radar products."""
    # Check that only correct attributes are set
    assert data.label is not None
    assert data.name == name
    assert data.projection is not None
    assert data.unit == unit
    assert data.url is not None
    assert data.data is None
    assert data._gain is not None
    assert data._offset is not None

    # Download the data
    data.download()
    assert data.data is not None
    assert data.data.dtype == dtype

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


RADAR_XML = """<?xml version="1.0" encoding="UTF-8"?>
<wfs:FeatureCollection xmlns:wfs="http://www.opengis.net/wfs/2.0"
                       xmlns:gml="http://www.opengis.net/gml/3.2"
                       xmlns:om="http://www.opengis.net/om/2.0"
                       xmlns:swe="http://www.opengis.net/swe/2.0"
                       xmlns:xlink="http://www.w3.org/1999/xlink">
  <wfs:member>
    <gml:TimeInstant gml:id="time1">
      <gml:timePosition>2026-09-08T12:00:00Z</gml:timePosition>
    </gml:TimeInstant>
    %s
    <swe:DataRecord>
      <swe:field name="dbz" xlink:href="https://opendata.fmi.fi/meta?observableProperty=radar&amp;param=dbz"/>
    </swe:DataRecord>
    <gml:fileReference>https://openwms.fmi.fi/geoserver/wms?service=WMS&amp;layers=Radar:suomi_dbz&amp;srs=EPSG:3067&amp;time=2026-09-08T12:00:00Z</gml:fileReference>
  </wfs:member>
</wfs:FeatureCollection>
"""
PARAMETERS = """
    <om:parameter>
      <om:NamedValue>
        <om:name xlink:href="http://xml.fmi.fi/inspire/process/value/linearTransformationGain"/>
        <gml:Measure>0.5</gml:Measure>
      </om:NamedValue>
    </om:parameter>
    <om:parameter>
      <om:NamedValue>
        <om:name xlink:href="http://xml.fmi.fi/inspire/process/value/linearTransformationOffset"/>
        <gml:Measure>-32.0</gml:Measure>
      </om:NamedValue>
    </om:parameter>
    <om:parameter>
      <om:NamedValue>
        <om:name xlink:href="http://xml.fmi.fi/inspire/process/value/elevationAngle"/>
        <gml:Measure>0.3</gml:Measure>
      </om:NamedValue>
    </om:parameter>
"""
META_XML = """<?xml version="1.0" encoding="UTF-8"?>
<omop:ObservableProperty xmlns:omop="http://inspire.ec.europa.eu/schemas/omop/2.9">
  <omop:label>Reflectivity factor</omop:label>
  <omop:uom uom="dBZ"/>
</omop:ObservableProperty>
"""


def _geotiff(values, dtype):
    """Write a small GeoTIFF into memory and give back its bytes."""
    from rasterio.io import MemoryFile
    from rasterio.transform import from_origin

    values = np.array(values, dtype=dtype)
    with MemoryFile() as memfile:
        with memfile.open(driver="GTiff", height=values.shape[0], width=values.shape[1],
                          count=1, dtype=dtype, crs="EPSG:3067",
                          transform=from_origin(0.0, 0.0, 1000.0, 1000.0)) as dataset:
            dataset.write(values, 1)
        return memfile.read()


# 255 is outside the detection range, 0 is "nothing detected"
COUNTS = [[255, 0, 10],
          [0, 20, 30],
          [40, 50, 255]]


def _parse_radar(parameters=PARAMETERS):
    """Parse the test document and return the only dataset in it."""
    import defusedxml.ElementTree as ET

    from fmiopendata.radar import ParseRadar

    with mock.patch("fmiopendata.radar.read_cached_xml", return_value=ET.fromstring(META_XML)):
        res = ParseRadar(RADAR_XML % parameters)

    assert len(res.data) == len(res.times) == 1

    return res.data[0]


def test_radar_metadata():
    """Test the metadata of a radar dataset."""
    data = _parse_radar()

    assert data.time == dt.datetime(2026, 9, 8, 12, 0)
    assert data.name == "dbz"
    assert data.label == "Reflectivity factor"
    assert data.unit == "dBZ"
    assert data.elevation == 0.3
    assert data.etop_threshold is None
    assert data.max_velocity is None
    # Before the image is downloaded the projection is the one it is requested in
    assert data.projection == "EPSG:3067"
    assert data.projection_wkt is None
    assert data.data is None


def test_small_image_is_read_completely():
    """Test that an image smaller than the file buffer is not read as an empty file."""
    data = _parse_radar()
    image = _geotiff(COUNTS, np.uint8)
    # Well below the buffer an unflushed write would sit in
    assert len(image) < 8192

    with mock.patch("fmiopendata.radar.read_url", return_value=image):
        data.download()

    np.testing.assert_array_equal(data.data[0], COUNTS)
    assert "3067" in data.projection_wkt
    assert data.projection == "EPSG:3067"


def _download_recording_temporary_files(data, names, image=None):
    """Download *data*, recording in *names* the temporary files it goes through."""
    import tempfile

    real_mkstemp = tempfile.mkstemp

    def recording_mkstemp(*args, **kwargs):
        fid, fname = real_mkstemp(*args, **kwargs)
        names.append(fname)
        return fid, fname

    if image is None:
        image = _geotiff(COUNTS, np.uint8)
    with mock.patch("tempfile.mkstemp", side_effect=recording_mkstemp), \
            mock.patch("fmiopendata.radar.read_url", return_value=image):
        data.download()


def test_the_image_file_is_cleaned_up():
    """Test that reading the image leaves nothing behind."""
    data = _parse_radar()

    names = []
    _download_recording_temporary_files(data, names)

    assert len(names) == 1
    assert not os.path.exists(names[0])
    np.testing.assert_array_equal(data.data[0], COUNTS)


def test_the_image_file_is_cleaned_up_after_a_failure():
    """Test that a failure to read the image does not leave the file behind."""
    data = _parse_radar()

    names = []
    with mock.patch("fmiopendata.radar.rasterio.open", side_effect=RuntimeError("no")):
        with pytest.raises(RuntimeError):
            _download_recording_temporary_files(data, names)

    assert len(names) == 1
    assert not os.path.exists(names[0])


def test_calibration_and_masks():
    """Test that the masks hold before and after calibration, which happens once."""
    data = _parse_radar()
    with mock.patch("fmiopendata.radar.read_url", return_value=_geotiff(COUNTS, np.uint8)):
        data.download()

    area_mask = data.get_area_mask()
    data_mask = data.get_data_mask()
    np.testing.assert_array_equal(area_mask[0], np.array(COUNTS) == 255)
    np.testing.assert_array_equal(data_mask[0], np.array(COUNTS) == 0)

    data.calibrate()
    np.testing.assert_allclose(data.data[0], np.array(COUNTS) * 0.5 - 32.0)
    # The masks find the same pixels once the data are physical values
    np.testing.assert_array_equal(data.get_area_mask(), area_mask)
    np.testing.assert_array_equal(data.get_data_mask(), data_mask)

    # Calibrating again would turn the data into nonsense, so it does nothing
    calibrated = data.data.copy()
    data.calibrate()
    np.testing.assert_array_equal(data.data, calibrated)


def test_missing_calibration():
    """Test a dataset that gives a gain but no offset."""
    gain_only = PARAMETERS.split("<om:parameter>")[1]
    data = _parse_radar(parameters="<om:parameter>" + gain_only)
    with mock.patch("fmiopendata.radar.read_url", return_value=_geotiff(COUNTS, np.uint8)):
        data.download()

    with pytest.warns(UserWarning, match="only one of the linear transformation"):
        data.calibrate()

    # The counts are left alone, and the masks still work on them
    np.testing.assert_array_equal(data.data[0], COUNTS)
    np.testing.assert_array_equal(data.get_area_mask()[0], np.array(COUNTS) == 255)


def test_dataset_without_a_time():
    """Test that a dataset without a measurement time is skipped."""
    from fmiopendata.radar import ParseRadar

    xml = """<wfs:FeatureCollection xmlns:wfs="http://www.opengis.net/wfs/2.0">
               <wfs:member/>
             </wfs:FeatureCollection>"""
    with pytest.warns(UserWarning, match="no measurement time"):
        res = ParseRadar(xml)

    assert res.data == []
    assert res.times == []


def test_service_exception():
    """Test that an exception from the WMS is not read as an image."""
    data = _parse_radar()
    exception = (b"<?xml version='1.0'?><ServiceExceptionReport>"
                 b"<ServiceException code='InvalidDimensionValue'/></ServiceExceptionReport>")

    with mock.patch("fmiopendata.radar.read_url", return_value=exception):
        with pytest.raises(ValueError, match="WMS returned an exception"):
            data.download()
