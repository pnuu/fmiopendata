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
        data_format = _get_url_format(self.url)
        if data_format is not None and "grib" in data_format.lower():
            return self._parse_grib
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
