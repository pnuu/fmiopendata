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

"""Parse the metadata of the FMI observation stations."""

import datetime as dt
from typing import Dict, List, Optional
from xml.etree.ElementTree import Element

import defusedxml.ElementTree as ET
import numpy as np

from fmiopendata import namespaces, wfs
from fmiopendata.utils import read_url

TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


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
        for member in xml.findall(namespaces.WFS_MEMBER):
            facility = member.find(namespaces.EF_ENVIRONMENTAL_MONITORING_FACILITY)
            if facility is None:
                continue

            # Extract the station ID
            station_id_elem = facility.find(namespaces.GML_IDENTIFIER)
            if station_id_elem is None:
                continue

            station_id = station_id_elem.text

            # Initialize station data dictionary with flattened structure
            station_data = {
                "id": facility.get(namespaces.GML_ID),
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
            for name_elem in facility.findall(namespaces.GML_NAME):
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
                name_elem = facility.find(namespaces.EF_NAME)
                if name_elem is not None:
                    station_data["name"] = name_elem.text

            # Extract INSPIRE ID
            inspire_id_elem = facility.find(namespaces.EF_INSPIRE_ID)
            if inspire_id_elem is not None:
                local_id_elem = inspire_id_elem.find(namespaces.INS_BASE_LOCAL_ID)
                namespace_elem = inspire_id_elem.find(
                    namespaces.INS_BASE_NAMESPACE
                )
                if local_id_elem is not None:
                    station_data["inspire_local_id"] = local_id_elem.text
                if namespace_elem is not None:
                    station_data["inspire_namespace"] = namespace_elem.text

            # Extract station position
            point_elem = facility.find(namespaces.GML_POINT)
            if point_elem is not None:
                pos_elem = point_elem.find(namespaces.GML_POS)
                if pos_elem is not None:
                    coords = pos_elem.text.split()
                    station_data["latitude"] = float(coords[0])
                    station_data["longitude"] = float(coords[1])

            # Extract measurement regime
            regime_elem = facility.find(namespaces.EF_MEASUREMENT_REGIME)
            if regime_elem is not None:
                href = regime_elem.get(namespaces.LINK)
                if href:
                    # Extract the value from the URL
                    station_data["measurement_regime"] = (
                        href.split("/")[-1]
                    )

            # Extract mobile status
            mobile_elem = facility.find(namespaces.EF_MOBILE)
            if mobile_elem is not None and mobile_elem.text:
                station_data["mobile"] = (
                    mobile_elem.text.lower() == "true"
                )

            # Extract time period
            time_period_elem = facility.find(namespaces.GML_TIME_PERIOD)
            if time_period_elem is not None:
                begin_elem = time_period_elem.find(namespaces.GML_BEGIN_POSITION)
                end_elem = time_period_elem.find(namespaces.GML_END_POSITION)

                if begin_elem is not None and begin_elem.text:
                    try:
                        station_data["start_time"] = begin_elem.text
                    except ValueError:
                        pass

                if end_elem is not None:
                    if end_elem.get("indeterminatePosition") == "now":
                        station_data["end_time"] = dt.datetime.now().strftime(TIME_FORMAT)
                    elif end_elem.text:
                        try:
                            station_data["end_time"] = end_elem.text
                        except ValueError:
                            pass

            # Extract station network types (can be multiple)
            belongs_elems = facility.findall(namespaces.EF_BELONGS_TO)
            for belongs_elem in belongs_elems:
                title = belongs_elem.get(namespaces.XLINK_TITLE)
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
                (dt.datetime(1970, 1, 1) + dt.timedelta(seconds=t)).strftime(TIME_FORMAT)
                for t in positions[2::3]
            ]
        )
        if times.size == 0:
            times = np.array(
                [
                    dt.datetime.strptime(
                        xml.findtext(namespaces.GML_TIME_POSITION),
                        TIME_FORMAT
                    ).strftime(TIME_FORMAT)
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
    # Example usage: python -m fmiopendata.station
    print(download_and_parse("fmi::ef::stations").data)
