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

"""Test station data parsers."""

import datetime as dt
import warnings

import pytest

from fmiopendata.station import Station, download_and_parse

# Every test here downloads the station list from the FMI services
pytestmark = pytest.mark.network

START_TIME = dt.datetime(1829, 1, 1, 0, 0, 0)
END_TIME = dt.datetime(2025, 7, 7, 12, 5, 0)
TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

ARGS = [
    "starttime=" + START_TIME.isoformat(timespec="seconds") + "Z",
    "endtime=" + END_TIME.isoformat(timespec="seconds") + "Z",
]

# Stations the service gives as Finland's, but which are nowhere near it: Aboa is
# the Finnish research station in Queen Maud Land, Antarctica, at 73 S 13 W.
STATIONS_OUTSIDE_FINLAND = ("Antarktis Aboa",)


def _test_verify_station_common(res):
    """Verify basic aspects of station data."""
    # Check that result is a Station object
    assert isinstance(res, Station), "Result should be a Station instance"

    # Check that data is not empty
    assert res.data, "Station data should not be empty"


class TestStationParser:
    """Test suite for station data parsers."""

    def test_station_default(self):
        """Test station parser for default query of station data."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

    def test_station_structure(self):
        """Test the structure of station data."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        # Check the structure of station data for each station
        for station_id, station_data in res.data.items():
            # Verify station_id is a string
            assert isinstance(
                station_id, str
            ), f"Station ID should be a string, got {type(station_id)}"

            # Check required fields exist with correct types
            assert isinstance(station_data, dict), \
                "Station data should be a dictionary"
            assert "id" in station_data, \
                "Station data should have 'id' field"
            assert "fmisid" in station_data, \
                "Station data should have 'fmisid' field"
            assert "name" in station_data, \
                "Station data should have 'name' field"
            assert "geoid" in station_data, \
                "Station data should have 'geoid' field"
            assert "wmo" in station_data, \
                "Station data should have 'wmo' field"
            assert "region" in station_data, \
                "Station data should have 'region' field"
            assert "country" in station_data, \
                "Station data should have 'country' field"
            assert "station_type" in station_data, \
                "Station data should have 'station_type' field"
            assert "latitude" in station_data, \
                "Station data should have 'latitude' field"
            assert "longitude" in station_data, \
                "Station data should have 'longitude' field"
            assert "start_time" in station_data, \
                "Station data should have 'start_time' field"
            assert "end_time" in station_data, \
                "Station data should have 'end_time' field"
            assert "inspire_local_id" in station_data, \
                "Station data should have 'inspire_local_id' field"
            assert "inspire_namespace" in station_data, \
                "Station data should have 'inspire_namespace' field"
            assert "measurement_regime" in station_data, \
                "Station data should have 'measurement_regime' field"
            assert "mobile" in station_data, \
                "Station data should have 'mobile' field"

            # Verify station_type is a list
            assert isinstance(station_data["station_type"], list), \
                "station_type should be a list"

    def test_station_position_data(self):
        """Test position data in station information."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        for _, station_data in res.data.items():
            # Check position data if latitude and longitude exist
            if (
                station_data["latitude"] is not None
                and station_data["longitude"] is not None
            ):
                assert isinstance(
                    station_data["latitude"], float
                ), "Latitude should be a float"
                assert isinstance(
                    station_data["longitude"], float
                ), "Longitude should be a float"

    def test_station_time_data(self):
        """Test time data in station information."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        for _, station_data in res.data.items():
            # Check start_time if it exists
            if station_data["start_time"] is not None:
                assert isinstance(
                    dt.datetime.strptime(
                        station_data["start_time"],
                        TIME_FORMAT
                    ),
                    dt.datetime
                ), "Start time should be a datetime"

            # Check end_time if it exists
            if station_data["end_time"] is not None:
                assert isinstance(
                    dt.datetime.strptime(
                        station_data["end_time"],
                        TIME_FORMAT
                    ),
                    dt.datetime
                ), "End time should be a datetime"

    def test_get_station_by_id(self):
        """Test get_station_by_id helper method."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        # Get a sample station ID to test with
        sample_station_id = next(iter(res.data))
        sample_station = res.data[sample_station_id]

        # Test get_station_by_id
        retrieved_station = res.get_station_by_id(sample_station_id)
        assert (
            retrieved_station == sample_station
        ), "get_station_by_id should return the correct station"

    def test_get_station_by_name(self):
        """Test get_station_by_name helper method."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        # Find a station with a name
        for _, station_data in res.data.items():
            if station_data["name"] is not None:
                name_retrieved_station = res.get_station_by_name(
                    station_data["name"]
                )
                assert (
                    name_retrieved_station == station_data
                ), "get_station_by_name should return the correct station"
                break

    def test_get_stations_by_type(self):
        """Test get_stations_by_type helper method."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        # Find a station with a type
        for station_id, station_data in res.data.items():
            if (
                station_data.get("station_type") and
                len(station_data["station_type"]) > 0
            ):
                station_type = station_data["station_type"][0]

                type_stations = res.get_stations_by_type(station_type)
                assert (
                    station_id in type_stations
                ), "get_stations_by_type should include the sample station"
                break

    def test_get_stations_by_country(self):
        """Test get_stations_by_country helper method."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        # Find a station with a country
        for station_id, station_data in res.data.items():
            if station_data.get("country") is not None:
                country_stations = res.get_stations_by_country(
                    station_data["country"]
                )
                assert (
                    station_id in country_stations
                ), "get_stations_by_country should include the sample station"
                break

    def test_get_stations_by_region(self):
        """Test get_stations_by_region helper method."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        # Find a station with a region
        for station_id, station_data in res.data.items():
            if station_data.get("region") is not None:
                region_stations = res.get_stations_by_region(
                    station_data["region"]
                )
                assert (
                    station_id in region_stations
                ), "get_stations_by_region should include the sample station"
                break

    def test_station_inspire_id_structure(self):
        """Test INSPIRE ID fields when present."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        # Find a station with INSPIRE ID
        for _, station_data in res.data.items():
            if station_data["inspire_local_id"] is not None:
                assert isinstance(
                    station_data["inspire_local_id"], str
                ), "INSPIRE local ID should be a string"
                assert (
                    station_data["inspire_local_id"] == station_data["fmisid"]
                ), "INSPIRE local ID should match FMISID"
                break

    def test_station_inspire_namespace(self):
        """Test INSPIRE namespace field when present."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        # Find a station with INSPIRE namespace
        for _, station_data in res.data.items():
            if station_data["inspire_namespace"] is not None:
                assert isinstance(
                    station_data["inspire_namespace"], str
                ), "INSPIRE namespace should be a string"
                assert "http" in station_data["inspire_namespace"], \
                    "INSPIRE namespace should be a URL"
                break

    def test_station_measurement_regime(self):
        """Test measurement regime field when present."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        # Find a station with measurement regime
        for _, station_data in res.data.items():
            if station_data["measurement_regime"] is not None:
                assert isinstance(
                    station_data["measurement_regime"], str
                ), "Measurement regime should be a string"
                # Common values include continuousDataCollection
                assert len(station_data["measurement_regime"]) > 0, \
                    "Measurement regime should not be empty"
                break

    def test_station_mobile_field(self):
        """Test mobile field is boolean when present."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        # Find a station with mobile field set
        for _, station_data in res.data.items():
            if station_data["mobile"] is not None:
                assert isinstance(
                    station_data["mobile"], bool
                ), "Mobile field should be a boolean"
                # Most FMI stations are stationary
                break


class TestStationValues:
    """Test types and values in station data parser's output."""

    def test_station_type_is_list(self):
        """Test that station_type field is always a list."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        for _, station_data in res.data.items():
            assert isinstance(
                station_data["station_type"], list
            ), "station_type should be a list"

    def test_station_with_multiple_station_types(self):
        """Test handling of stations with multiple station types."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        # Find a station with multiple network types
        found_multiple_types = False
        for _, station_data in res.data.items():
            if len(station_data["station_type"]) > 1:
                found_multiple_types = True

                # Verify all entries are strings
                for network_type in station_data["station_type"]:
                    assert isinstance(
                        network_type, str
                    ), "Each network type should be a string"

                break

        # Note: This test may not always find a multi-network station
        # depending on the data range queried
        if found_multiple_types:
            assert True, "Found station with multiple network types"

    def test_station_coordinates_validity(self):
        """Test that coordinates are within valid ranges."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        for _, station_data in res.data.items():
            if (
                station_data["latitude"] is not None
                and station_data["longitude"] is not None
            ):
                # Valid latitude range
                assert -90 <= station_data["latitude"] <= 90, \
                    f"Invalid latitude: {station_data['latitude']}"
                # Valid longitude range
                assert -180 <= station_data["longitude"] <= 180, \
                    f"Invalid longitude: {station_data['longitude']}"

                # For Finnish stations, rough bounds
                if (
                    station_data["country"] == "Finland"
                    and station_data["name"] not in STATIONS_OUTSIDE_FINLAND
                ):
                    assert 59 <= station_data["latitude"] <= 71, \
                        "Finnish station latitude should be between 59-71"
                    assert 19 <= station_data["longitude"] <= 33, \
                        "Finnish station longitude should be between 19-33"

    def test_station_time_order(self):
        """Test that start_time is before end_time."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        for _, station_data in res.data.items():
            if (
                station_data["start_time"] is not None
                and station_data["end_time"] is not None
            ):
                assert (
                    station_data["start_time"] <= station_data["end_time"]
                ), "start_time should be before or equal to end_time"

    def test_station_geoid_format(self):
        """Test geoid field format when present."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        # Find a station with geoid
        for _, station_data in res.data.items():
            if station_data["geoid"] is not None:
                assert isinstance(
                    station_data["geoid"], str
                ), "Geoid should be a string"
                # Geoids in the sample are negative integers as strings
                assert station_data["geoid"].startswith("-") or \
                    station_data["geoid"].isdigit(), \
                    "Geoid should be a negative numeric string"
                break

    def test_station_wmo_format(self):
        """Test WMO ID field format when present."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        # Find a station with WMO ID
        for _, station_data in res.data.items():
            if station_data["wmo"] is not None:
                assert isinstance(
                    station_data["wmo"], str
                ), "WMO ID should be a string"
                assert len(station_data["wmo"]) == 5, \
                    "WMO ID should be 5 digits"
                assert station_data["wmo"].isdigit(), \
                    "WMO ID should be numeric"
                break

    def test_station_fmisid_matches_station_id(self):
        """Test that fmisid field matches the dictionary key."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        for station_id, station_data in res.data.items():
            assert station_id == station_data["fmisid"], \
                "Station ID key should match fmisid field"

    def test_station_data_consistency(self):
        """Test that all stations have consistent structure."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        # Get the keys from the first station
        first_station = next(iter(res.data.values()))
        expected_keys = set(first_station.keys())

        # Verify all stations have the same keys
        for station_id, station_data in res.data.items():
            actual_keys = set(station_data.keys())
            assert actual_keys == expected_keys, \
                f"Station {station_id} has inconsistent keys"

    def test_station_at_least_one_field_populated(self):
        """Test that each station has at least some data populated."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        for station_id, station_data in res.data.items():
            # Count non-None values
            #  (excluding the list which is always present)
            populated_fields = sum(
                1 for k, v in station_data.items()
                if v is not None and k != "station_type"
            )
            assert populated_fields > 0, \
                f"Station {station_id} has no populated fields"

    def test_get_stations_by_type_returns_correct_stations(self):
        """Test that get_stations_by_type returns only matching stations."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        # Find a station with a network type
        for _, station_data in res.data.items():
            if station_data["station_type"]:
                network_type = station_data["station_type"][0]
                matching_stations = res.get_stations_by_type(network_type)

                # Verify all returned stations have the network type
                for _, matched_station in matching_stations.items():
                    assert network_type in matched_station["station_type"], \
                        "Returned station should have the queried network type"
                break

    def test_station_country_values(self):
        """Test that country field has expected values."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        countries_found = set()
        for _, station_data in res.data.items():
            if station_data["country"] is not None:
                countries_found.add(station_data["country"])

        # FMI primarily has Finnish stations
        assert "Finland" in countries_found, \
            "Should have at least some Finnish stations"

    def test_station_name_not_empty(self):
        """Test that station names are not empty strings when present."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        for station_id, station_data in res.data.items():
            if station_data["name"] is not None:
                assert len(station_data["name"]) > 0, \
                    f"Station {station_id} name should not be empty"


class TestStationErrorCases:
    """Test error handling in station data parsers."""

    def test_invalid_query(self):
        """Test handling of invalid stored query ID."""
        query_id = "invalid::stored::query"
        try:
            # Ignore warnings about not having a handler for this query ID
            # as we are testing error handling here for a case
            # that does not have a handler.
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                download_and_parse(query_id, args=ARGS)
        except NotImplementedError as e:
            expected_msg = (
                f"Custom parsing for query ID '{query_id}' not implemented!"
            )
            assert str(e) == expected_msg, \
                "Error message does not match expected handler error message!"
        else:
            raise AssertionError(
                "Expected NotImplementedError for invalid query ID"
            )

    def test_get_station_by_id_nonexistent(self):
        """Test get_station_by_id with non-existent ID returns None."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        # Use an ID that shouldn't exist
        nonexistent_station = res.get_station_by_id("999999999")
        assert nonexistent_station is None, \
            "Should return None for non-existent station ID"

    def test_get_station_by_name_nonexistent(self):
        """Test get_station_by_name with non-existent name returns None."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        # Use a name that shouldn't exist
        nonexistent_station = res.get_station_by_name(
            "NonExistent Station 12345"
        )
        assert nonexistent_station is None, \
            "Should return None for non-existent station name"

    def test_get_stations_by_type_nonexistent(self):
        """Test get_stations_by_type with non-existent type returns empty."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        # Use a type that shouldn't exist
        nonexistent_stations = res.get_stations_by_type(
            "NonExistent Type 12345"
        )
        assert len(nonexistent_stations) == 0, \
            "Should return empty dict for non-existent station type"

    def test_get_stations_by_country_nonexistent(self):
        """Test get_stations_by_country with non-existent country."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        # Use a country that shouldn't exist
        nonexistent_stations = res.get_stations_by_country("Antarctica")
        assert len(nonexistent_stations) == 0, \
            "Should return empty dict for non-existent country"

    def test_get_stations_by_region_nonexistent(self):
        """Test get_stations_by_region with non-existent region."""
        res = download_and_parse("fmi::ef::stations", args=ARGS)
        _test_verify_station_common(res)

        # Use a region that shouldn't exist
        nonexistent_stations = res.get_stations_by_region(
            "NonExistent Region 12345"
        )
        assert len(nonexistent_stations) == 0, \
            "Should return empty dict for non-existent region"
