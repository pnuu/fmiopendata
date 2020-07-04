# fmiopendata
Python interface for FMI open data

## Examples

### Download and parse latest soundings
```python

from fmiopendata.wfs import download_stored_query

snd.soundings = download_stored_query("fmi::observations::weather::sounding::multipointcoverage")
```

Now `snd.soundings.soundings` is a list of the soundings, and the data within each can be reached from the attributes:

```python

snd.soundings[0].name  # Name of the sounding station
snd.soundings[0].id  # Station ID of the sounding station
snd.soundings[0].nominal_time  # Nominal time of the sounding
snd.soundings[0].start_time  # Actual start time of the sounding
snd.soundings[0].end_time  # Actual end time of the sounding
snd.soundings[0].lats  # Numpy array of the measurement location latitudes [degrees]
snd.soundings[0].lons  # Numpy array of the measurement location longitudes [degrees]
snd.soundings[0].altitudes  # Numpy array of the measurement location altitudes [m]
snd.soundings[0].times  # Numpy array of the measurement times [s] (unix time)
snd.soundings[0].pressures  # Numpy array of measured pressures [hPa]
snd.soundings[0].temperatures  # Numpy array of measured temperatures [°C]
snd.soundings[0].dew_points  # Numpy array of measured dew points [°C]
snd.soundings[0].wind_speeds  # Numpy array of measured wind speeds [m/s]
snd.soundings[0].wind_directions  # Numpy array of measured wind directions [°]
```

More refined search results can be retrieved by passing arguments that will be added to the WFS request URL.

```python

snd.soundings = download_stored_query("fmi::observations::weather::sounding::multipointcoverage",
                                      "place=Jokioinen")
```
