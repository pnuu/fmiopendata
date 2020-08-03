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

"""Test WFS interface."""

from unittest import mock


def test_get_capabilities():
    """Test downloading WFS capabilities."""
    from fmiopendata.wfs import get_capabilities

    res = get_capabilities()
    assert "WFS_Capabilities" in str(res)


def test_get_stored_queries():
    """Test downloading and parsing WFS stored queries."""
    from fmiopendata.wfs import get_stored_queries

    res = get_stored_queries()
    for key in res.keys():
        assert isinstance(key, str)
        assert "title" in res[key]


def test_get_stored_query_descriptions():
    """Test downloading stored query descriptions."""
    from fmiopendata.wfs import get_stored_query_descriptions

    res = get_stored_query_descriptions()
    for key in res.keys():
        assert isinstance(key, str)
        assert "title" in res[key]
        assert "description" in res[key]


def test_download_stored_query_radar():
    """Test that download/parse function is imported from radar module."""
    with mock.patch("fmiopendata.radar.download_and_parse") as dap:
        from fmiopendata.wfs import download_stored_query

        res = download_stored_query("foo::radar::grid")
        del res
    dap.assert_called_once()


def test_download_stored_query_sounding():
    """Test that download/parse function is imported from sounding module."""
    with mock.patch("fmiopendata.sounding.download_and_parse") as dap:
        from fmiopendata.wfs import download_stored_query

        res = download_stored_query("foo::sounding::multipointcoverage")
        del res
    dap.assert_called_once()


def test_download_stored_query_lightning():
    """Test that download/parse function is imported from lightning module."""
    with mock.patch("fmiopendata.lightning.download_and_parse") as dap:
        from fmiopendata.wfs import download_stored_query

        res = download_stored_query("foo::lightning::bar")
        del res
    dap.assert_called_once()


def test_download_stored_query_grid():
    """Test that download/parse function is imported from grid module."""
    with mock.patch("fmiopendata.grid.download_and_parse") as dap:
        from fmiopendata.wfs import download_stored_query

        res = download_stored_query("foo::grid::bar")
        del res
    dap.assert_called_once()


def test_download_stored_query_multipointcoverage():
    """Test that download/parse function is imported from multipoint module."""
    with mock.patch("fmiopendata.multipoint.download_and_parse") as dap:
        from fmiopendata.wfs import download_stored_query

        res = download_stored_query("foo::multipointcoverage::bar")
        del res
    dap.assert_called_once()


def test_download_stored_query_notimplemented():
    """Test that proper error is raised for invalid request."""
    from fmiopendata.wfs import download_stored_query
    import pytest

    with pytest.raises(NotImplementedError):
        _ = download_stored_query("foo::bar::baz")
