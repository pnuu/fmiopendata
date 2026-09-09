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
import os
import tempfile
import warnings

import defusedxml.ElementTree as ET

import numpy as np
import eccodes

from fmiopendata import namespaces, wfs
from fmiopendata.utils import read_url, download_to_file

TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
# The names NetCDF data from FMI give the dimensions of a grid
_TIME_DIMENSION = "time"
_LEVEL_DIMENSION = "level"
_LATITUDE_DIMENSION = "lat"
_LONGITUDE_DIMENSION = "lon"


class Grid(object):
    """Class for holding grid data."""

    def __init__(self):
        """Initialize the class."""
        self.init_time = None
        self.start_time = None
        self.end_time = None
        self.data = dict()
        self.latitudes = None
        self.longitudes = None
        self.url = None
        self._fname = None
        self._temporary_file = False

    def download(self, fname=None):
        """Read the data.

        The data are downloaded only once.  Asking afterwards for them to be placed
        in a different file is an error, rather than a call that quietly does
        nothing and leaves the data where they already are.
        """
        if self._fname is not None:
            if fname is not None and fname != self._fname:
                raise ValueError("The data have already been downloaded to %s" %
                                 self._fname)
            return
        if fname is None:
            fid, fname = tempfile.mkstemp(suffix=".grib")
            os.close(fid)
            self._temporary_file = True
        download_to_file(self.url, fname)
        self._fname = fname

    def __del__(self):
        """Remove the temporary file this object created, if there is one."""
        if not self._temporary_file:
            return
        try:
            self.delete_file()
        except (AttributeError, OSError, TypeError):
            # Nothing can be done about it while the interpreter is shutting down
            pass

    def parse(self, delete=False):
        """Parse the data."""
        parser = self._get_parser()
        if self.data:
            return

        self.download()
        parser()
        if delete:
            self.delete_file()

    def _get_parser(self):
        """Get the parser for the format the data are served in."""
        data_format = (_get_url_format(self.url) or "").lower()
        if "grib" in data_format:
            return self._parse_grib
        if "netcdf" in data_format:
            return self._parse_netcdf
        raise NotImplementedError("No parser for %s" % (data_format or self.url))

    def _parse_grib(self):
        """Parser for GRIB data."""
        with eccodes.reader.FileReader(self._fname) as grib:
            for msg in grib:
                valid_date = msg["validityDate"]
                year = valid_date // 10000
                month = valid_date % 10000 // 100
                day = valid_date % 10000 % 100
                valid_time = msg["validityTime"]
                hour = valid_time // 100
                minute = valid_time % 100
                datime = dt.datetime(year, month, day, hour, minute)
                if self.latitudes is None:
                    self.latitudes = np.reshape(msg["latitudes"], (msg["Nj"], msg["Ni"]))
                    self.longitudes = np.reshape(msg["longitudes"], (msg["Nj"], msg["Ni"]))
                if datime not in self.data:
                    self.data[datime] = dict()
                if msg["level"] not in self.data[datime]:
                    self.data[datime][msg["level"]] = dict()
                level = self.data[datime][msg["level"]]
                name = msg["name"]
                if name in level:
                    name = _unique_name(name, level, msg)
                    warnings.warn("Several %s messages for level %s at %s, "
                                  "the later ones are named like \"%s\"" %
                                  (msg["name"], msg["level"], datime, name), stacklevel=2)
                data = np.reshape(msg["values"], (msg["Nj"], msg["Ni"]))
                data[data == msg["missingValue"]] = np.nan
                level[name] = dict({"data": data, "units": msg["units"]})

    def _parse_netcdf(self):
        """Parser for NetCDF data."""
        try:
            import netCDF4
        except ImportError:
            raise ImportError("Reading NetCDF data requires the netCDF4 library, which "
                              "comes with the \"netcdf\" extra of fmiopendata") from None

        with netCDF4.Dataset(self._fname) as dataset:
            times = _get_times(dataset)
            levels = _get_levels(dataset)
            self.latitudes, self.longitudes = _get_coordinates(dataset)
            for name, variable in dataset.variables.items():
                if not _is_data_variable(variable, dataset):
                    continue
                self._collect_netcdf_variable(name, variable, times, levels)

    def _collect_netcdf_variable(self, name, variable, times, levels):
        """Collect one NetCDF variable, one grid per time and level."""
        name = getattr(variable, "long_name", name)
        units = getattr(variable, "units", "")
        values = _to_array(variable[:])
        has_levels = _LEVEL_DIMENSION in variable.dimensions

        for i, time in enumerate(times):
            for j, level in enumerate(levels):
                data = values[i, j] if has_levels else values[i]
                level_data = self.data.setdefault(time, dict()).setdefault(level, dict())
                level_data[name] = dict({"data": data, "units": units})
                if not has_levels:
                    break

    def delete_file(self):
        """Delete the downloaded file, if there is one."""
        if self._fname is not None and os.path.isfile(self._fname):
            os.remove(self._fname)


def _unique_name(name, level, msg):
    """Find a name for a message whose name is taken at this level already.

    GRIB tells messages apart by more than the name, the level and the validity
    time this library keys the data by, so two messages can land on the same key.
    Qualify the name of the later one with what does distinguish them instead of
    dropping it.
    """
    qualifiers = [_get_key(msg, key) for key in ("typeOfLevel", "stepType")]
    qualifiers = [str(qualifier) for qualifier in qualifiers if qualifier is not None]

    candidate = "%s (%s)" % (name, ", ".join(qualifiers)) if qualifiers else name
    number = 2
    while candidate in level:
        candidate = "%s (%d)" % (name, number)
        number += 1

    return candidate


def _get_key(msg, key):
    """Get *key* of the GRIB message *msg*, or None if it does not have it."""
    try:
        return msg[key]
    except (KeyError, RuntimeError, ValueError):
        return None


def _get_times(dataset):
    """Get the times of the grids in *dataset* as naive UTC datetimes."""
    import netCDF4

    variable = dataset.variables[_TIME_DIMENSION]
    times = netCDF4.num2date(variable[:], variable.units,
                             only_use_cftime_datetimes=False, only_use_python_datetimes=True)

    # num2date gives a datetime subclass of its own; the GRIB data are keyed by plain
    # datetimes, and the two are not worth telling apart
    return [dt.datetime(time.year, time.month, time.day,
                        time.hour, time.minute, time.second, time.microsecond)
            for time in np.atleast_1d(times)]


def _get_levels(dataset):
    """Get the levels of the grids in *dataset*.

    A dataset without a level dimension has all its data on one level, which is
    given as 0 so that the data are laid out the same way as GRIB data are.
    """
    variable = dataset.variables.get(_LEVEL_DIMENSION)
    if variable is None:
        return [0]

    return [_to_number(level) for level in np.atleast_1d(variable[:])]


def _get_coordinates(dataset):
    """Get the latitudes and longitudes of *dataset* as grids."""
    latitudes = _to_array(dataset.variables[_LATITUDE_DIMENSION][:])
    longitudes = _to_array(dataset.variables[_LONGITUDE_DIMENSION][:])
    if latitudes.ndim == 1:
        longitudes, latitudes = np.meshgrid(longitudes, latitudes)

    return latitudes, longitudes


def _is_data_variable(variable, dataset):
    """Tell whether *variable* holds data rather than describing the grid."""
    if variable.name in dataset.dimensions:
        return False

    return _LATITUDE_DIMENSION in variable.dimensions and _LONGITUDE_DIMENSION in variable.dimensions


def _to_array(values):
    """Turn *values* into a plain array, with the values that are missing as NaN."""
    return np.ma.filled(np.ma.masked_invalid(np.ma.asarray(values, dtype=float)), np.nan)


def _to_number(value):
    """Turn a coordinate value into an int when it is one, so that levels read nicely."""
    number = float(value)

    return int(number) if number.is_integer() else number


def _get_url_format(url):
    """Get the format the data at *url* are served in, if the URL says so."""
    for item in url.split("&"):
        if item.lower().startswith("format="):
            return item.split("=", 1)[1]
    return None


class ParseGrids(object):
    """Class for parsing grid data."""

    def __init__(self, xml):
        """Initialize class."""
        self._xml = ET.fromstring(xml)
        self.data = dict()
        self._parse()

    def _parse(self):
        """Parse grid data."""
        for member in self._xml.findall(namespaces.WFS_MEMBER):
            grid = Grid()
            grid.init_time = dt.datetime.strptime(member.findtext(namespaces.GML_TIME_POSITION), TIME_FORMAT)
            grid.start_time = dt.datetime.strptime(member.findtext(namespaces.GML_BEGIN_POSITION), TIME_FORMAT)
            grid.end_time = dt.datetime.strptime(member.findtext(namespaces.GML_END_POSITION), TIME_FORMAT)
            grid.url = member.findtext(namespaces.GML_FILE_REFERENCE)
            self.data[grid.init_time] = grid


def download_and_parse(query_id, args=None):
    """Download and parse the given stored query."""
    url = wfs.STORED_QUERY_URL + query_id
    if args:
        url = url + "&" + "&".join(args)
    xml = read_url(url)
    return ParseGrids(xml)
