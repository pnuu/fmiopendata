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

from urllib.request import urlretrieve
import warnings

import requests
import defusedxml.ElementTree as ET

EXCEPTION_TEXT = './/{http://www.opengis.net/ows/1.1}ExceptionText'


def read_url(url):
    """Read url."""
    req = requests.get(url)
    if not req.ok:
        _give_warning(req.content)
    return req.content


def _give_warning(req_content):
    root = ET.fromstring(req_content)
    exceptions = '\n'.join([" - " + ex_.text for ex_ in root.findall(EXCEPTION_TEXT)])
    exception_text = "\n\nFMI servers responded with the following errors:\n\n%s\n" % exceptions
    warnings.warn(exception_text)


def download_to_file(url, fname):
    """Download file from *ulr* to *fname*."""
    outpath, http_msg = urlretrieve(url, filename=fname)
    return outpath, http_msg
