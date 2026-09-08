# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

`fmiopendata` is a Python library that downloads and parses data from the Finnish
Meteorological Institute (FMI) open data WFS/WMS services. It is GPLv3, requires
Python >= 3.10, and has no plugin/entry-point machinery — parsers are plain modules
selected by string matching on the WFS stored query ID.

## Commands

```bash
# Install for development (deps come from conda, see below)
pip install --no-deps -e .

# Build the distributions the way CI does
python -m build && twine check dist/*

# Run the whole test suite with coverage (what CI does)
pytest --cov=fmiopendata fmiopendata/tests --cov-report=xml

# Run only the tests that do not need the FMI services (~0.2 s)
pytest -m "not network" fmiopendata/tests

# Run one test module / one test
pytest fmiopendata/tests/test_multipoint.py
pytest fmiopendata/tests/test_multipoint.py::test_multipoint_weather

# Lint (flake8 with docstrings/debugger/bugbear plugins; config in setup.cfg)
pre-commit run --all-files
```

The `rasterio` (radar) and `eccodes` (grid) dependencies are painful via pip; the CI
environment in `continuous_integration/environment.yaml` installs them from
conda-forge (`eccodes` needs both the conda library and the `eccodes` pip bindings).
Recreate that environment locally when touching `radar.py` or `grid.py`.

## Most tests hit the live FMI servers

Twenty of the tests perform real HTTP requests to `opendata.fmi.fi` /
`openwms.fmi.fi`, so failures are frequently caused by the upstream service (a
retired stored query, an inconsistent response, a broken WMS layer) rather than by
the code. They carry `@pytest.mark.network`, so `pytest -m "not network"` runs the
rest. Tests for known-broken upstream layers are marked
`@pytest.mark.xfail(raises=AssertionError, reason="Broken WMS layer")` — prefer that
over deleting a test. Queries that need a fixed time window (lightning, old daily
observations) hard-code historical `starttime`/`endtime` values so the response is
stable.

The offline tests build their input inline rather than carrying fixtures: XML as
string templates, a GeoTIFF written into memory with `rasterio.io.MemoryFile`
(`test_radar.py`), and a 214-byte GRIB2 message built from an eccodes sample
(`test_grids.py`). Keep it that way — no binary fixtures in the repository. The
radar image in `test_radar.py` is deliberately smaller than the file buffer, which
is what makes it catch a missing `flush()` in `Radar.download()`.

## Architecture

Everything flows through one public entry point:

```
fmiopendata.wfs.download_stored_query(query_id, args)
  -> dispatches on substrings in query_id to a parser module's download_and_parse()
```

`wfs.download_stored_query()` (`fmiopendata/wfs.py`) matches the lowercased query ID
against the `PARSERS` table and imports the matching module lazily — this is why
`rasterio`/`eccodes` stay optional extras. Unknown IDs raise `NotImplementedError`.
Adding support for a new data type means adding a module with
`download_and_parse(query_id, args=None)` and an entry in that table; the order of
the entries matters, since lightning and sounding queries also end in
`multipointcoverage`.

Every parser module follows the same shape:

- `download_and_parse()` builds the URL as `wfs.STORED_QUERY_URL + query_id` plus
  `"&".join(args)`, calls `utils.read_url()`, and hands the XML to a parser class.
- The parser class calls `defusedxml.ElementTree.fromstring()` and walks the tree
  using the namespaced XPath constants defined **centrally in
  `fmiopendata/namespaces.py`** (`GML_*`, `WFS_*`, `SWE_*`, `OM_*`, `OMOP_*`;
  `wfs.py` re-exports them for compatibility). Add new namespace constants there,
  not in the parser module.
- `TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"` is redefined per module (`wms.py` uses a
  different one, with fractional seconds).
- A response that is missing, empty or self-inconsistent produces a
  `warnings.warn()` and an empty or truncated result — parsers do not raise.

Two-stage (lazy) parsers — `radar.py` and `grid.py` — differ from the rest. Their
WFS response contains only metadata and a `fileReference` URL, so parsing returns
container objects whose payload is *not* fetched until the caller acts:

- `Radar.download()` fetches a GeoTIFF into a temp file and reads it with `rasterio`;
  `calibrate()` (idempotent), `get_area_mask()` and `get_data_mask()` each call
  `download()` first and interpret raw counts via the
  `linearTransformationGain`/`Offset` values taken from the XML, converting the
  sentinel value only when `_calibrated` is set. `.projection` is the CRS
  identifier, `.projection_wkt` the WKT filled in at download. Metadata documents
  are cached by `utils.read_cached_xml()`, shared with `multipoint.py`.
- `Grid.download()` / `Grid.parse()` fetch a GRIB file and decode it with `eccodes`
  into `Grid.data[valid_time][level][dataset_name]` = `{"data": ndarray, "units": str}`,
  replacing `missingValue` with `np.nan`. The format comes from the URL's `format`
  argument; anything but GRIB raises `NotImplementedError`. Messages that collide on
  (time, level, name) are stored under a qualified name rather than overwriting. The
  temporary file is removed when the `Grid` is dropped, unless the caller named it.

`multipoint.py` is the workhorse (most stored queries route here) and produces two
different layouts from the same XML: the default `data[time][station][parameter]` =
`{"value", "units"}`, or, when `"timeseries=True"` is passed in `args` (a marker read
by this library, filtered out of a copy before the URL is built),
`data[station][parameter]["values"]` plus a shared
`data[station]["times"]` list (a parameter actually named `times` is renamed, see
`TIMES_KEY`). Station coordinates live separately in
`location_metadata[station]`. Radionuclide queries take a separate per-`member`
parsing path.

`utils.read_url()` never raises on an HTTP error: it emits a `warnings.warn()`
containing the `ows:ExceptionText` from the FMI error document — or the HTTP status,
when the body is not an exception report — and returns the body, so parsers must cope
with unexpected content. `utils.download_to_file()` streams to disk the same way.

`wms.py` is independent of the WFS path — it parses GetCapabilities into `WMSLayer`
objects and is used mainly by the `bin/` scripts.

## Scripts and generated docs

`fmiopendata/wfs_html.py` and `fmiopendata/wms_html.py` dump the live service
catalogue. They are installed as the console scripts `wfs_html.py` and `wms_html.py`
(the names keep the `.py` they have always had) through `[project.scripts]` in
`pyproject.toml`, so their `main()` must stay importable. Both write HTML, or
Markdown if the output filename does not end in `html`. The HTML default is
deliberate — it opens in any browser locally — and the checked-in `wfs.md` and
`wms.md` are Markdown so that GitHub renders them; the `*_html.py` names are not a
leftover, so don't "fix" either. Both catalogues are large and generated —
regenerate them rather than editing by hand.

## Conventions

- Bump `__version__` in `fmiopendata/__init__.py`; `pyproject.toml` reads it from
  there as a dynamic version. Packaging lives in `pyproject.toml`, flake8 config in
  `setup.cfg` (flake8 does not read pyproject).
- Every class and function carries a docstring (flake8-docstrings is enforced; the
  module-level `D100`/`D104` are ignored, the licence header stands in for them).
- Lines up to 120 characters; `warnings.warn()` calls pass a `stacklevel`.
- Always use `defusedxml.ElementTree`, never the stdlib `xml.etree`.
- New parsers should document the supported stored query IDs and the resulting data
  structure in `README.md`, following the existing per-datatype example sections.
