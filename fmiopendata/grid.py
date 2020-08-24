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
import xml.etree.ElementTree as ET
import os
import tempfile
import sys
if sys.version_info < (3, 6):
    from collections import OrderedDict as dict

import numpy as np
import eccodes

from fmiopendata import wfs
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

    def download(self, fname=None):
        """Read the data."""
        if self._fname is not None:
            return
        if fname is None:
            temp = tempfile.NamedTemporaryFile(delete=False)
            fname = temp.name
        outpath, http_msg = download_to_file(self.url, fname)
        self._fname = fname

    def parse(self, delete=False):
        """Parse the data."""
        if "grib" in self.url:
            parser = self._parse_grib
        else:
            format = [itm for itm in self.url.split("&") if "format" in itm.lower()][0]
            raise NotImplementedError("No parser for %s" % format)

        self.download()
        if self.data:
            return
        parser()
        if delete:
            self.delete_file()

    def _parse_grib(self):
        """Parser for GRIB data."""
        with eccodes.GribFile(self._fname) as grib:
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
                level[msg["name"]] = dict()
                data = np.reshape(msg["values"], (msg["Nj"], msg["Ni"]))
                data[data == msg["missingValue"]] = np.nan
                level[msg["name"]]["data"] = data
                level[msg["name"]]["units"] = msg["units"]

    def delete_file(self):
        """Delete the downloaded file."""
        if os.path.isfile(self._fname):
            os.remove(self._fname)


class ParseGrids(object):
    """Class for parsing grid data."""

    def __init__(self, xml):
        """Initialize class."""
        self._xml = ET.fromstring(xml)
        self.data = dict()
        self._parse()

    def _parse(self):
        """Parse grid data."""
        for member in self._xml.findall(wfs.WFS_MEMBER):
            grid = Grid()
            grid.init_time = dt.datetime.strptime(member.findtext(wfs.GML_TIME_POSITION), TIME_FORMAT)
            grid.start_time = dt.datetime.strptime(member.findtext(wfs.GML_BEGIN_POSITION), TIME_FORMAT)
            grid.end_time = dt.datetime.strptime(member.findtext(wfs.GML_END_POSITION), TIME_FORMAT)
            grid.url = member.findtext(wfs.GML_FILE_REFERENCE)
            self.data[grid.init_time] = grid


def download_and_parse(query_id, args=None):
    """Download and parse the given stored query."""
    url = wfs.STORED_QUERY_URL + query_id
    if args:
        url = url + "&" + "&".join(args)
    xml = read_url(url)
    return ParseGrids(xml)
