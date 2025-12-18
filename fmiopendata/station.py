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

import os
import sys
import defusedxml.ElementTree as ET
import datetime as dt
import numpy as np

from xml.etree.ElementTree import Element
from typing import List, Dict, Optional

# Add the parent directory to the Python path when running as a script
if __name__ == "__main__":
    sys.path.insert(0, os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    ))

from fmiopendata import wfs
from fmiopendata.utils import read_url

TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

# Add the needed possibly missing constants
# to wfs module when running as script.
if __name__ == "__main__":
    if not hasattr(wfs, "EF_ENVIRONMENTAL_MONITORING_FACILITY"):
        wfs.EF_ENVIRONMENTAL_MONITORING_FACILITY = (
            ".//{http://inspire.ec.europa.eu/schemas/ef/4.0}"
            "EnvironmentalMonitoringFacility"
        )
    if not hasattr(wfs, "EF_NAME"):
        wfs.EF_NAME = (
            ".//{http://inspire.ec.europa.eu/schemas/ef/4.0}name"
        )
    if not hasattr(wfs, "EF_BELONGS_TO"):
        wfs.EF_BELONGS_TO = (
            ".//{http://inspire.ec.europa.eu/schemas/ef/4.0}belongsTo"
        )
    if not hasattr(wfs, "XLINK_TITLE"):
        wfs.XLINK_TITLE = "{http://www.w3.org/1999/xlink}title"
    if not hasattr(wfs, "GML_TIME_PERIOD"):
        wfs.GML_TIME_PERIOD = (
            ".//{http://www.opengis.net/gml/3.2}TimePeriod"
        )
    if not hasattr(wfs, "EF_INSPIRE_ID"):
        wfs.EF_INSPIRE_ID = (
            ".//{http://inspire.ec.europa.eu/schemas/ef/4.0}inspireId"
        )
    if not hasattr(wfs, "INS_BASE_LOCAL_ID"):
        wfs.INS_BASE_LOCAL_ID = (
            ".//{http://inspire.ec.europa.eu/schemas/base/3.3}localId"
        )
    if not hasattr(wfs, "INS_BASE_NAMESPACE"):
        wfs.INS_BASE_NAMESPACE = (
            ".//{http://inspire.ec.europa.eu/schemas/base/3.3}namespace"
        )
    if not hasattr(wfs, "EF_MOBILE"):
        wfs.EF_MOBILE = (
            ".//{http://inspire.ec.europa.eu/schemas/ef/4.0}mobile"
        )
    if not hasattr(wfs, "EF_MEASUREMENT_REGIME"):
        wfs.EF_MEASUREMENT_REGIME = (
            ".//{http://inspire.ec.europa.eu/schemas/ef/4.0}"
            "measurementRegime"
        )


class Station(object):
    """Class representing a weather station."""

    def __init__(self, xml: str) -> None:
        """Initialize class."""
        self._xml = ET.fromstring(xml)
        self.data = dict()

        self._parse(self._xml)

    def _parse(self, xml: Element) -> None:
        """Parse station data."""
        # Get all station entries from the XML
        for member in xml.findall(wfs.WFS_MEMBER):
            facility = member.find(wfs.EF_ENVIRONMENTAL_MONITORING_FACILITY)
            if facility is None:
                continue

            # Extract the station ID
            station_id_elem = facility.find(wfs.GML_IDENTIFIER)
            if station_id_elem is None:
                continue

            station_id = station_id_elem.text

            # Initialize station data dictionary with flattened structure
            station_data = {
                "id": facility.get(wfs.GML_ID),
                "fmisid": station_id,
                "geoid": None,
                "wmo": None,
                "name": None,
                "region": None,
                "country": None,
                "station_type": [],
                "latitude": None,
                "longitude": None,
                "start_time": None,
                "end_time": None,
                "inspire_local_id": None,
                "inspire_namespace": None,
                "measurement_regime": None,
                "mobile": None,
            }

            # Extract station names and other identifiers
            for name_elem in facility.findall(wfs.GML_NAME):
                code_space = name_elem.get("codeSpace", "")
                if "locationcode/name" in code_space:
                    station_data["name"] = name_elem.text
                elif "locationcode/geoid" in code_space:
                    station_data["geoid"] = name_elem.text
                elif "locationcode/wmo" in code_space:
                    station_data["wmo"] = name_elem.text
                elif "location/region" in code_space:
                    station_data["region"] = name_elem.text
                elif "location/country" in code_space:
                    station_data["country"] = name_elem.text

            # If name wasn't found in gml:name, try ef:name
            if station_data["name"] is None:
                name_elem = facility.find(wfs.EF_NAME)
                if name_elem is not None:
                    station_data["name"] = name_elem.text

            # Extract INSPIRE ID
            inspire_id_elem = facility.find(wfs.EF_INSPIRE_ID)
            if inspire_id_elem is not None:
                local_id_elem = inspire_id_elem.find(wfs.INS_BASE_LOCAL_ID)
                namespace_elem = inspire_id_elem.find(
                    wfs.INS_BASE_NAMESPACE
                )
                if local_id_elem is not None:
                    station_data["inspire_local_id"] = local_id_elem.text
                if namespace_elem is not None:
                    station_data["inspire_namespace"] = namespace_elem.text

            # Extract station position
            point_elem = facility.find(wfs.GML_POINT)
            if point_elem is not None:
                pos_elem = point_elem.find(wfs.GML_POS)
                if pos_elem is not None:
                    coords = pos_elem.text.split()
                    station_data["latitude"] = float(coords[0])
                    station_data["longitude"] = float(coords[1])

            # Extract measurement regime
            regime_elem = facility.find(wfs.EF_MEASUREMENT_REGIME)
            if regime_elem is not None:
                href = regime_elem.get(wfs.LINK)
                if href:
                    # Extract the value from the URL
                    station_data["measurement_regime"] = (
                        href.split("/")[-1]
                    )

            # Extract mobile status
            mobile_elem = facility.find(wfs.EF_MOBILE)
            if mobile_elem is not None and mobile_elem.text:
                station_data["mobile"] = (
                    mobile_elem.text.lower() == "true"
                )

            # Extract time period
            time_period_elem = facility.find(wfs.GML_TIME_PERIOD)
            if time_period_elem is not None:
                begin_elem = time_period_elem.find(wfs.GML_BEGIN_POSITION)
                end_elem = time_period_elem.find(wfs.GML_END_POSITION)

                if begin_elem is not None and begin_elem.text:
                    try:
                        station_data["start_time"] = dt.datetime.strptime(
                            begin_elem.text, TIME_FORMAT
                        )
                    except ValueError:
                        pass

                if end_elem is not None:
                    if end_elem.get("indeterminatePosition") == "now":
                        station_data["end_time"] = dt.datetime.now()
                    elif end_elem.text:
                        try:
                            station_data["end_time"] = dt.datetime.strptime(
                                end_elem.text, TIME_FORMAT
                            )
                        except ValueError:
                            pass

            # Extract station network types (can be multiple)
            belongs_elems = facility.findall(wfs.EF_BELONGS_TO)
            for belongs_elem in belongs_elems:
                title = belongs_elem.get(wfs.XLINK_TITLE)
                if title:
                    station_data["station_type"].append(title)

            # Add station data to the main data dictionary
            self.data[station_id] = station_data

    def _parse_times(
        self,
        xml: Element,
        positions: List[float]
    ) -> np.ndarray:
        """Parse time data from GML positions."""
        times = np.array(
            [
                dt.datetime(1970, 1, 1) + dt.timedelta(seconds=t)
                for t in positions[2::3]
            ]
        )
        if times.size == 0:
            times = np.array(
                [
                    dt.datetime.strptime(
                        xml.findtext(wfs.GML_TIME_POSITION),
                        TIME_FORMAT
                    )
                ]
            )
        return times

    def get_station_by_id(self, station_id: str) -> Optional[Dict]:
        """Get station information by its ID."""
        return self.data.get(station_id)

    def get_station_by_name(
        self,
        name: str
    ) -> Optional[Dict]:
        """Get station information by its name."""
        for _, station_data in self.data.items():
            if station_data["name"] == name:
                return station_data
        return None

    def get_stations_by_type(self, station_type: str) -> Optional[Dict]:
        """Get all stations of a specific type."""
        return {
            station_id: station_data
            for station_id, station_data in self.data.items()
            if station_type in station_data["station_type"]
        }

    def get_stations_by_country(self, country: str) -> Optional[Dict]:
        """Get all stations in a specific country."""
        return {
            station_id: station_data
            for station_id, station_data in self.data.items()
            if station_data["country"] == country
        }

    def get_stations_by_region(self, region: str) -> Optional[Dict]:
        """Get all stations in a specific region."""
        return {
            station_id: station_data
            for station_id, station_data in self.data.items()
            if station_data["region"] == region
        }


def download_and_parse(
        query_id: str = "fmi::ef::stations",
        args: List[str] = None
) -> Station:
    """Download and parse the data for the given stored query ID."""
    if args is None:
        args = []
    url = wfs.STORED_QUERY_URL + query_id
    if args:
        url = url + "&" + "&".join(args)
    xml = read_url(url)

    if query_id == "fmi::ef::stations":
        # Handling of the weather station data from FMI Open Data WFS service.
        return Station(xml)
    else:
        raise NotImplementedError(
            f"Custom parsing for query ID '{query_id}' not implemented!"
        )


if __name__ == "__main__":
    ARGS = []

    # Example usage
    station_data = download_and_parse("fmi::ef::stations", args=ARGS)
    # for station_id, info in station_data.data.items():
    #     print(f"Station ID: {station_id}, Name: {info['name']},
    #           Country: {info['country']}")
    print(station_data.data)
