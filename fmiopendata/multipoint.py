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

import datetime as dt
import warnings

import defusedxml.ElementTree as ET

import numpy as np

from fmiopendata import namespaces, wfs
from fmiopendata.utils import epoch_to_datetime, read_cached_xml, read_url

TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
COORDINATE_DECIMALS = 5
# The key the measurement times are kept under in the timeseries layout
TIMES_KEY = "times"


class MultiPoint(object):
    """Class for holding multipoint data."""

    def __init__(self, xml, query_id, timeseries=False):
        """Initialize class."""
        self._xml = ET.fromstring(xml)
        self.data = dict()
        self.location_metadata = dict()
        self._location2name = dict()
        self._unknown_locations = set()
        self._timeseries = timeseries

        if "radionuclide-activity-concentration" in query_id:
            self._parse_radionuclide()
        else:
            self._parse(self._xml)

    def _parse_radionuclide(self):
        """Parse radionuclide data."""
        for member in self._xml.findall(namespaces.WFS_MEMBER):
            self._parse(member)

    def _parse_location_metadata(self, xml):
        """Parse location metadata."""
        for point in xml.findall(namespaces.GML_POINT):
            fmisid = int(point.attrib[namespaces.GML_ID].split('-')[-1])
            name = point.findtext(namespaces.GML_NAME)
            # A position can carry an elevation after the coordinates
            latitude, longitude = (float(p) for p in point.findtext(namespaces.GML_POS).split()[:2])
            self.location_metadata[name] = dict({"fmisid": fmisid,
                                                 "latitude": latitude,
                                                 "longitude": longitude
                                                 })
            self._location2name[_location_key(latitude, longitude)] = name

    def _name_for_location(self, latitude, longitude):
        """Get the name of the station at the given coordinates."""
        key = _location_key(latitude, longitude)
        try:
            return self._location2name[key]
        except KeyError:
            if key not in self._unknown_locations:
                self._unknown_locations.add(key)
                warnings.warn("No station metadata for location %s, "
                              "its measurements are skipped" % (key,), stacklevel=2)
            return None

    def _parse(self, xml):
        """Parse data."""
        positions_txt = xml.findtext(namespaces.GMLCOV_POSITIONS)
        if positions_txt is None:
            warnings.warn("No observations found", stacklevel=2)
            return

        self._parse_location_metadata(xml)

        type2obs = parse_names_and_units(xml)
        positions = _parse_positions(positions_txt)
        latitudes = positions[::3]
        longitudes = positions[1::3]
        times = _parse_times(xml, positions)
        measurements = _parse_measurements(xml, (len(times), len(type2obs)))

        if self._timeseries:
            self._collect_timeseries(type2obs, latitudes, longitudes, times, measurements)
        else:
            self._collect_non_timeseries(type2obs, latitudes, longitudes, times, measurements)

    def to_dataframe(self, exclude_empty=False):
        """Collect the observations into a pandas DataFrame.

        The frame is indexed by the observation time and the station name, and has a
        column per observed parameter.  The units are in ``frame.attrs["units"]`` and
        the station coordinates in ``frame.attrs["location_metadata"]``, since a
        DataFrame has nowhere else to keep them.

        With *exclude_empty* the columns that hold no values at all are left out;
        querying a bounding box tends to produce a few of those.
        """
        pd = _import_pandas()

        index, rows, units = self._collect_rows()
        frame = pd.DataFrame(rows, index=pd.MultiIndex.from_tuples(
            index, names=["time", "location"])).sort_index()
        if exclude_empty:
            frame = frame.dropna(axis=1, how="all")
        frame.attrs["units"] = {name: unit for name, unit in units.items() if name in frame}
        frame.attrs["location_metadata"] = self.location_metadata

        return frame

    def _collect_rows(self):
        """Collect the observations as one row per time and station."""
        index, rows, units = [], [], dict()

        for time, name, measurements in self._iterate_observations():
            index.append((time, name))
            row = dict()
            for parameter, measurement in measurements.items():
                row[parameter] = measurement["value"]
                units.setdefault(parameter, measurement["units"])
            rows.append(row)

        return index, rows, units

    def _iterate_observations(self):
        """Go through the data as (time, station, {parameter: {value, units}}).

        The two layouts keep the same observations in a different shape, and a frame
        is built from either of them.
        """
        if not self._timeseries:
            for time, stations in self.data.items():
                for name, measurements in stations.items():
                    yield time, name, measurements
            return

        for name, station in self.data.items():
            parameters = [key for key in station if key != TIMES_KEY]
            for i, time in enumerate(station[TIMES_KEY]):
                yield time, name, {parameter: {"value": station[parameter]["values"][i],
                                               "units": station[parameter]["unit"]}
                                   for parameter in parameters}

    def _collect_timeseries(self, type2obs, latitudes, longitudes, times, measurements):
        parameter_names = _timeseries_names(type2obs)
        for i, tim in enumerate(times):
            name = self._name_for_location(latitudes[i], longitudes[i])
            if name is None:
                continue
            if name not in self.data:
                self.data[name] = {TIMES_KEY: []}
            self.data[name][TIMES_KEY].append(tim)
            for j, key in enumerate(type2obs.keys()):
                parameter = parameter_names[key]
                if parameter not in self.data[name]:
                    self.data[name][parameter] = {"values": [], "unit": type2obs[key]["units"]}
                self.data[name][parameter]["values"].append(measurements[i, j])

    def _collect_non_timeseries(self, type2obs, latitudes, longitudes, times, measurements):
        for i, tim in enumerate(times):
            name = self._name_for_location(latitudes[i], longitudes[i])
            if name is None:
                continue
            if tim not in self.data:
                self.data[tim] = dict()
            if name not in self.data[tim]:
                self.data[tim][name] = dict()
            for j, key in enumerate(type2obs.keys()):
                self.data[tim][name][type2obs[key]["name"]] = dict({"value": measurements[i, j],
                                                                    "units": type2obs[key]["units"]
                                                                    })


def _import_pandas():
    """Import pandas, explaining what to install when it is not there."""
    try:
        import pandas
    except ImportError:
        raise ImportError("Collecting the observations into a DataFrame requires "
                          "pandas, which comes with the \"pandas\" extra of "
                          "fmiopendata") from None

    return pandas


def _timeseries_names(type2obs):
    """Get the key each parameter is stored under in the timeseries layout.

    The measurement times share the dictionary with the parameters, so a parameter
    of that name would replace them.
    """
    names = dict()
    for key, observation in type2obs.items():
        name = observation["name"]
        if name == TIMES_KEY:
            name = "%s (parameter)" % name
            warnings.warn('A parameter is called "%s", which is where the measurement '
                          'times are kept, so it is stored as "%s"' % (TIMES_KEY, name),
                          stacklevel=2)
        names[key] = name

    return names


def _location_key(latitude, longitude):
    """Build the key used to match a measurement position to a station.

    The station coordinates and the measurement positions are read from two
    different elements of the response, so they are rounded to a fixed precision
    before they are compared.
    """
    return (round(float(latitude), COORDINATE_DECIMALS),
            round(float(longitude), COORDINATE_DECIMALS))


def _parse_positions(positions_txt):
    return np.fromstring(positions_txt, dtype=float, sep=" ")


def _parse_times(xml, positions):
    times = np.array([epoch_to_datetime(t) for t in positions[2::3]])
    if times.size == 0:
        times = np.array([dt.datetime.strptime(xml.findtext(namespaces.GML_TIME_POSITION), TIME_FORMAT)])
    return times


def _parse_measurements(xml, shape):
    measurements = np.fromstring(xml.findtext(namespaces.GML_DOUBLE_OR_NIL_REASON_TUPLE_LIST), dtype=float, sep=" ")
    return np.reshape(measurements, shape)


def parse_names_and_units(xml):
    """Get the name and unit of every observed parameter described in *xml*."""
    type2obs = dict()

    for field in xml.findall(namespaces.SWE_FIELD):
        typ = field.attrib["name"]
        url = field.attrib.get(namespaces.LINK)
        if url is None:
            # The label and unit are given inline
            name = field.findtext(namespaces.SWE_LABEL)
            units = field.find(namespaces.SWE_UOM).attrib['code']
        else:
            # They are in a separate metadata document.  The same document is
            # referred to by every member of a response, so it is cached.
            root = read_cached_xml(url)
            name = root.findtext(namespaces.OMOP_LABEL)
            try:
                units = root.find(namespaces.OMOP_UOM).attrib["uom"]
            except AttributeError:
                units = ''
        # FMI does not always give a label for a parameter.  Fall back on the name
        # of the field itself, so that the data are keyed by something the caller
        # can use instead of by None.
        name = name or typ
        type2obs[typ] = dict({"name": name, "units": units})

    return type2obs


def download_and_parse(query_id, args=None):
    """Download and parse the given stored query."""
    # Work on a copy: "timeseries=True" is a marker for this library rather than a
    # query argument, and removing it must not modify the caller's list.
    args = list(args) if args else []
    timeseries = "timeseries=True" in args
    if timeseries:
        args.remove("timeseries=True")
    url = wfs.STORED_QUERY_URL + query_id
    if args:
        url = url + "&" + "&".join(args)
    xml = read_url(url)
    return MultiPoint(xml, query_id, timeseries=timeseries)
