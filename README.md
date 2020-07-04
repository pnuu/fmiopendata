# fmiopendata
Python interface for FMI open data

## Examples

### Download and parse latest soundings
```python

from fmiopendata.wfs import download_stored_query

snd.soundings = download_stored_query("fmi::observations::weather::sounding::multipointcoverage")
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
sounding.times  # Numpy array of the measurement times [s] (unix time)
sounding.pressures  # Numpy array of measured pressures [hPa]
sounding.temperatures  # Numpy array of measured temperatures [°C]
sounding.dew_points  # Numpy array of measured dew points [°C]
sounding.wind_speeds  # Numpy array of measured wind speeds [m/s]
sounding.wind_directions  # Numpy array of measured wind directions [°]
```

More refined search results can be retrieved by passing arguments that will be added to the WFS request URL.

```python

snd.soundings = download_stored_query("fmi::observations::weather::sounding::multipointcoverage",
                                      "place=Jokioinen")
```
