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

import defusedxml
import defusedxml.ElementTree as ET
import requests

EXCEPTION_TEXT = './/{http://www.opengis.net/ows/1.1}ExceptionText'
CHUNK_SIZE = 1024 * 1024
EPOCH = dt.datetime(1970, 1, 1)


def epoch_to_datetime(seconds):
    """Convert *seconds* since the Unix epoch to a naive UTC datetime."""
    return EPOCH + dt.timedelta(seconds=float(seconds))


def read_url(url):
    """Read url."""
    req = requests.get(url)
    if not req.ok:
        _give_warning(req)
    return req.content


def _give_warning(req):
    """Warn about a failed request *req*."""
    exceptions = _collect_exception_texts(req.content)
    if not exceptions:
        # The failure did not come from the WFS/WMS application itself, so there is no
        # exception report to show.  Fall back to what the HTTP layer tells us.
        exceptions = ["HTTP %s %s" % (req.status_code, req.reason)]
    details = '\n'.join([" - " + ex_ for ex_ in exceptions])
    exception_text = "\n\nFMI servers responded with the following errors:\n\n%s\n" % details
    warnings.warn(exception_text)


def _collect_exception_texts(req_content):
    """Collect the OWS exception messages from *req_content*, if it holds any."""
    try:
        root = ET.fromstring(req_content)
    except (ET.ParseError, defusedxml.DefusedXmlException):
        return []
    return [ex_.text for ex_ in root.findall(EXCEPTION_TEXT) if ex_.text]


def download_to_file(url, fname):
    """Download file from *url* to *fname*."""
    req = requests.get(url, stream=True)
    if not req.ok:
        _give_warning(req)
    with open(fname, "wb") as fid:
        for chunk in req.iter_content(chunk_size=CHUNK_SIZE):
            fid.write(chunk)
    return fname, req.headers
