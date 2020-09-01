# fmiopendata
Python interface for FMI open data

## Resources
[FMI open data](https://en.ilmatieteenlaitos.fi/open-data)

[FMI WFS guide](https://en.ilmatieteenlaitos.fi/open-data-manual-wfs-examples-and-guidelines)

## Installation

```bash

pip install fmiopendata
```

For `grid` datasets install also `eccodes`, and for `radar` datasets `rasterio` is needed.  Both
can be installed with `pip`, although usage of `miniconda` is strongly encouraged.

## Available data
This library provides two very simple scripts that list all the available data on
FMI open data WMS and WFS services.

Create `wms.html` that lists all the availble WMS layers:
```bash

wms_html.py
```

The `Layer ID` strings are used to identify WMS (image) datasets. Examples to be added.

Create `wfs.html` that lists all the availble WFS layers:
```bash

wfs_html.py
```

The `Query ID` is the handle that can be used to request data from WFS stored queries. See examples below.

## Examples

* [Download and parse latest soundings](#download-and-parse-latest-soundings)
* [Download and calibrate latest radar reflectivity (dBZ) composite](#download-and-calibrate-latest-radar-reflectivity-dBZ-composite)
* [Download and parse latest lightning data](#download-and-parse-latest-lightning-data)
* [Download and parse grid data](#download-and-parse-grid-data)
* [Download and parse observation data](#download-and-parse-observation-data)

### Download and parse latest soundings
```python

from fmiopendata.wfs import download_stored_query

snd = download_stored_query("fmi::observations::weather::sounding::multipointcoverage")
```

Now `snd.soundings` is a list of the soundings, and the data within each can be reached from the attributes:

```python

sounding = snd.soundings[0]
sounding.name  # Name of the sounding station
sounding.id  # Station ID of the sounding station
sounding.nominal_time  # Nominal time of the sounding
sounding.start_time  # Actual start time of the sounding
sounding.end_time  # Actual end time of the sounding
sounding.lats  # Numpy array of the measurement location latitudes [degrees]
sounding.lons  # Numpy array of the measurement location longitudes [degrees]
sounding.altitudes  # Numpy array of the measurement location altitudes [m]
sounding.times  # Numpy array of the measurement times [datetime]
sounding.pressures  # Numpy array of measured pressures [hPa]
sounding.temperatures  # Numpy array of measured temperatures [°C]
sounding.dew_points  # Numpy array of measured dew points [°C]
sounding.wind_speeds  # Numpy array of measured wind speeds [m/s]
sounding.wind_directions  # Numpy array of measured wind directions [°]
```

More refined search results can be retrieved by passing a list of arguments that will be added to the WFS request URL.

```python

snd.soundings = download_stored_query("fmi::observations::weather::sounding::multipointcoverage",
                                      ["place=Jokioinen"])
```


### Download and calibrate latest radar reflectivity (dBZ) composite

This parser requires the `rasterio` library to be installed.  All radar queries will work.

```python

from fmiopendata.wfs import download_stored_query

composites = download_stored_query("fmi::radar::composite::dbz")
```

Now `composites.data` is a list of the individual reflectivity composites and `composites.times` is a list of the nominal measurement times.

```python

import numpy as np

composite = composites[0]
# Download the image data
composite.download()
# Calibrate the data from image values to dBZ
# Calls `composite.download() if data are not already downloaded
composite.calibrate()
# Get mask for area outside the radar reach
# Calls `composite.download() if data are not already downloaded
mask1 = composite.get_area_mask()
# Get mask for invalid data
# Calls `composite.download() if data are not already downloaded
mask2 = composite.get_data_mask()
# Mask all the invalid areas using the above masks
composite.data[mask1 | mask2] = np.nan
```

The following attributes are available in the underlaying `Radar` class for all radar data:

```python

Radar.data  # The downloaded data, if .download() has been called
Radar.elevation  # Measurement angle for single radar datasets
Radar.etop_threshold  # Reflectivity limit for `etop` datasets
Radar.label  # Clear-text name for the data
Radar.max_velocity  # Maximum wind speed for `vrad` datasets
Radar.name  # Name of the dataset
Radar.projection  # WKT projection string for the dataset
Radar.time  # Nominal measurement time of the dataset
Radar.unit  # Unit of the calibrated data
Radar.url  # Direct download URL for the data
```

### Download and parse latest lightning data
```python

from fmiopendata.wfs import download_stored_query

# These both give identical results, the first one is much faster
lightning1 = download_stored_query("fmi::observations::lightning::multipointcoverage")
lightning2 = download_stored_query("fmi::observations::lightning::simple")
```

The following attributes hold the lightning data.

```python

lightning1.latitudes  # Latitude of the lightning event [° North]
lightning1.longitudes  # Longitude of the lightning event [° East]
lightning1.times  # Time of the lightning event [datetime]
lightning1.cloud_indicator  # Indicator for cloud flashes (1 == cloud lightning)
lightning1.multiplicity  # Multiplicity of the lightning event
lightning1.peak_current  # Maximum current of the lightning event [kA]
lightning1.ellipse_major  # Location accuracy of the lightning event [km]
```

### Download and parse grid data

The example below uses `fmi::forecast::harmonie::surface::grid` for demonstration.  Also other
`grid` stored queries should work, as long as the data are available in GRIB format.
This parser requires `eccodes` library to be installed.

```python

from fmiopendata.wfs import download_stored_query

model_data = download_stored_query("fmi::forecast::harmonie::surface::grid",
                                   args=["starttime=2020-07-06T18:00:00Z",
                                         "endtime=2020-07-06T20:00:00Z",
                                         "bbox=18,55,35,75"])
```

Here we limit both the time frame and area.  By default the WFS interface would offer all data
fields, full globe and all time steps, which would result in a huge amount of data.  It's better
to split the retrieval in smaller time intervals and do the downloading in parallel and start
processing the each chunk of data as soon as the download completes.

The above call doesn't download any data actual, it just collects some metadata:

```python

print(model_data.data)
# -> {datetime.datetime(2020, 7, 7, 0, 0): <fmiopendata.grid.Grid object at 0x7fda9858d2e8>,
#     datetime.datetime(2020, 7, 7, 6, 0): <fmiopendata.grid.Grid object at 0x7fda9858d0b8>,
#     datetime.datetime(2020, 7, 7, 12, 0): <fmiopendata.grid.Grid object at 0x7fda9858d1d0>}
```

Here the dictionary keys are the model initialization times.

The structure of the underlying `Grid` class is:

```python

Grid.data  # Parsed data, more info below
Grid.delete_file()  # Delete the downloaded GRIB2 file
Grid.download()  # Download the data
Grid.end_time  # Last valid time of the data [datetime]
Grid.init_time  # Initialization time of the data [datetime]
Grid.latitudes  # Latitudes of the parsed data [Numpy array]
Grid.longitudes  # Longitudes of the parsed data [Numpy array]
Grid.parse()  # Download and parse the data
Grid.start_time  # First valid time of the data [datetime]
Grid.url  # The URL where the data are downloaded from
```

Now, download and parse the data from the latest run:

```python

latest_run = max(model_data.data.keys())  # datetime.datetime(2020, 7, 7, 12, 0)
data = model_data[latest_run]
# This will download the data to a temporary file, parse the data and delete the file
data.parse(delete=True)
```

The `data.data` dictionary now has the following structure:

```python

# The first level has the valid times
valid_times = data.data.keys()
print(list(valid_times))
# -> [datetime.datetime(2020, 7, 7, 18, 0),
#     datetime.datetime(2020, 7, 7, 19, 0),
#     datetime.datetime(2020, 7, 7, 20, 0)]
```

The second level of the dictionary has the data vertical levels, here the earliest time step is shown:

```python
earliest_step = min(valid_times)
data_levels = data.data[earliest_step].keys()
print(list(data_lavels))
# -> [0, 2, 10]
```

Lets loop over these levels and print the dataset names and the units.

```python

for level in data_levels:
    datasets = data.data[earliest_step][level]
    for dset in datasets:
        unit = datasets[dset]["units"]
        data_array = datasets[dset]["data"]  # Numpy array of the actual data
        print("Level: %d, dataset name: %s, data unit: %s" % (level, dset, units))
```

This will print:

```
Level: 0, dataset name: Mean sea level pressure, data unit: J m**-2
Level: 0, dataset name: Orography, data unit: J m**-2
Level: 0, dataset name: Surface thermal radiation downwards, data unit: J m**-2
Level: 0, dataset name: Surface net thermal radiation, data unit: J m**-2
Level: 0, dataset name: Surface net solar radiation, data unit: J m**-2
Level: 2, dataset name: 2 metre temperature, data unit: J m**-2
Level: 2, dataset name: 2 metre dewpoint temperature, data unit: J m**-2
Level: 2, dataset name: 2 metre relative humidity, data unit: J m**-2
Level: 10, dataset name: Mean wind direction, data unit: J m**-2
Level: 10, dataset name: 10 metre wind speed, data unit: J m**-2
Level: 10, dataset name: 10 metre U wind component, data unit: J m**-2
Level: 10, dataset name: 10 metre V wind component, data unit: J m**-2
Level: 10, dataset name: surface precipitation amount, rain, convective, data unit: J m**-2
Level: 10, dataset name: Total Cloud Cover, data unit: J m**-2
Level: 10, dataset name: Low cloud cover, data unit: J m**-2
Level: 10, dataset name: Medium cloud cover, data unit: J m**-2
Level: 10, dataset name: High cloud cover, data unit: J m**-2
Level: 10, dataset name: Land-sea mask, data unit: J m**-2
Level: 10, dataset name: Precipitation rate, data unit: J m**-2
Level: 10, dataset name: Maximum wind velocity, data unit: J m**-2
Level: 10, dataset name: 10 metre wind gust since previous post-processing, data unit: J m**-2
Level: 10, dataset name: Surface solar radiation downwards, data unit: J m**-2
```

The whole structure `Grid.data[valid_time][level][dataset_name]` with `'data'` and `'units'`
members is common to all `grid` type WFS data.

The data arrays will have invalid values replaced with `np.nan`.

## Download and parse observation data
```python

from fmiopendata.wfs import download_stored_query

# Retrieve the latest hour of data from a bounding box
end_time = dt.datetime.utcnow()
start_time = end_time - dt.timedelta(hours=1)
# Convert times to properly formatted strings
start_time = start_time.isoformat(timespec="seconds") + "Z"
# -> 2020-07-07T12:00:00Z
end_time = end_time.isoformat(timespec="seconds") + "Z"
# -> 2020-07-07T13:00:00Z

obs = download_stored_query("fmi::observations::weather::multipointcoverage",
                            args=["bbox=18,55,35,75",
                                  "starttime=" + start_time,
                                  "endtime=" + end_time])
```

The structure of the returned `MultiPoint` class is

```python

MultiPoint.data  # The observation data
MultiPoint.location_metadata  # Location information for the observation locations
```

The `data` dictionary has the following structure:

```python

# The observation times are the primary key
print(sorted(obs.data.keys())
# -> [datetime.datetime(2020, 7, 7, 15, 0),
#     datetime.datetime(2020, 7, 7, 15, 1),
#     datetime.datetime(2020, 7, 7, 15, 2),
#     datetime.datetime(2020, 7, 7, 15, 3),
#     datetime.datetime(2020, 7, 7, 15, 4),
#     datetime.datetime(2020, 7, 7, 15, 5)]

# The next level has the names of the observation stations as keys
latest_tstep = max(obs.data.keys())
print(sorted(obs.data[latest_tstep].keys()))
# Will print a long list of weather station names, e.g. "Jyväskylä lentoasema", which we'll use
# as an example below

# On the third level we find the names of the observed parameters
print(sorted(obs.data[latest_tstep]["Jyväskylä lentoasema"].keys()))
# -> ['Air temperature',
#     'Cloud amount',
#     'Dew-point temperature',
#     'Gust speed',
#     'Horizontal visibility',
#     'Precipitation amount',
#     'Precipitation intensity',
#     'Present weather (auto)',
#     'Pressure (msl)',
#     'Relative humidity',
#     'Snow depth',
#     'Wind direction',
#     'Wind speed']

# And on the last level we find the value and unit of the observation
print(obs.data[latest_tstep]["Jyväskylä lentoasema"]["Air temperature"])
# -> {'value': 18.0, 'units': 'degC'}
```

To get the location for the stations, one can use the `location_metadata` dictionary:

```python

print(obs.location_metadata["Jyväskylä lentoasema"])
# -> {'fmisid': 101339, 'latitude': 62.39758, 'longitude': 25.67087}
```

This parser supports at least the following stored queries:

* `fmi::forecast::hirlam::surface::obsstations::multipointcoverage`
* `fmi::forecast::oaas::sealevel::point::multipointcoverage`
* `fmi::observations::airquality::hourly::multipointcoverage`
* `fmi::observations::mareograph::daily::multipointcoverage`
* `fmi::observations::mareograph::instant::multipointcoverage`
* `fmi::observations::mareograph::monthly::multipointcoverage`
* `fmi::observations::mareograph::multipointcoverage`
* `fmi::observations::radiation::multipointcoverage`
* `fmi::observations::wave::multipointcoverage`
* `fmi::observations::weather::cities::multipointcoverage`
* `fmi::observations::weather::multipointcoverage`
* `stuk::observations::air::radionuclide-activity-concentration::multipointcoverage`
* `stuk::observations::external-radiation::latest::multipointcoverage`
* `stuk::observations::external-radiation::multipointcoverage`
* `urban::observations::airquality::hourly::multipointcoverage`
