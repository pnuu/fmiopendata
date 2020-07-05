# fmiopendata
Python interface for FMI open data

## Resources
[FMI open data](https://en.ilmatieteenlaitos.fi/open-data)
[FMI WFS guide](https://en.ilmatieteenlaitos.fi/open-data-manual-wfs-examples-and-guidelines)

### Available data
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
