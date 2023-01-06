# Available WFS stored queries in FMI open data.

## ECMWF Pressure Grid

ECMWF forecast model's pressure levels as a grid data encoded in GRIB format.

* Query ID: `ecmwf::forecast::pressure::grid`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * levels
        * Pressure levels
        * A comma separated list of pressure levels (For example 1000,925,850).
    * format
        * Dataset format.
        * Encoding format for the returned dataset. Formats available are grib1, grib2 and netcdf. Default format is grib2.


## ECMWF weather forecast for cities in Finland as multipointcoverage

This stored query fetch ECMWF weather forecast for cities in Finland. The forcast is returned in multi point coverage format. By default, forcast is returned for the next 36 hours.

* Query ID: `ecmwf::forecast::surface::cities::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of time interval
        * The parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * The parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067


## ECMWF weather forecast for cities in Finland as simple features

This stored query fetch ECMWF weather forecast for cities in Finland. The forcast is returned in simple feature format. By default, forcast is returned for the next 36 hours.

* Query ID: `ecmwf::forecast::surface::cities::simple`
* Available arguments:
    * starttime
        * Begin of time interval
        * The Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * The Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067


## ECMWF weather forecast for cities in Finland as time value pairs

This stored query fetch ECMWF weather forecast for cities in Finland. The forcast is returned as time value pairs. By default, forcast is returned for the next 36 hours.

* Query ID: `ecmwf::forecast::surface::cities::timevaluepair`
* Available arguments:
    * starttime
        * Begin of time interval
        * The parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * The parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default, all parameters are returned.
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day. Default timestep is 60 minutes.
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## ECMWF surface level weather forecast for Finland as a grid.

This Stored Query request retrieve ECMWF surface level forecast raw dataset as a grid for Finland region.

* Query ID: `ecmwf::forecast::surface::finland::grid`
* Available arguments:
    * producer
        * Producer
        * Model or process which provides the data.
    * starttime
        * Begin of the time interval
        * Parameter starttime specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter endtime specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return. Default parameters are Temperature, Pressure, Humidity, DewPoint, WindUMS, WindVMS and Precipitation1h.
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (min Longitude, min Latitude, max Longitude, max Latitude) Default bounding box is 19.1,59.7,31.7,70.1.
    * format
        * Dataset format.
        * Encoding format for the returned dataset. Formats available are grib1, grib2 and netcdf. Default format is General Regularly-distributed Information in Binary form edition 2 (GRIB2).


## ECMWF Surface Grid

ECMWF forecast model's surface level as grid data encoded in GRIB format.

* Query ID: `ecmwf::forecast::surface::grid`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
		In addition to default parameters, there is 'RadiationDiffuseAccumulation'
		parameter that is not distributed in grib2 format.
		Default: GeopHeight,Temperature,Pressure,Humidity,WindUMS,WindVMS,MaximumWind,
		WindGust,DewPoint,TotalCloudCover,LowCloudCover,MediumCloudCover,HighCloudCover,
		Precipitation1h,PrecipitationAmount,RadiationGlobalAccumulation,RadiationLWAccumulation,
		RadiationNetSurfaceLWAccumulation,RadiationNetSurfaceSWAccumulation,LandSeaMask,
		WindSpeedMS,WindDirection,Cape
    * format
        * Dataset format.
        * Encoding format for the returned dataset. Formats available are grib1, grib2 and netcdf. Default format is General Regularly-distributed Information in Binary form edition 2 (GRIB2).


## ECMWF weather forecast for observation stations as multipointcoverage.

This stored query fetch ECMWF weather forecast for observation stations in Finland. The forcast is returned as multipointcoverage form. By default, forecast is returned for the next 36 hours.

* Query ID: `ecmwf::forecast::surface::obsstations::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter starttime specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter endtime specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default, all parameters are returned.
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day. Default timestep is 60 minutes.


## ECMWF weather forecast for observation stations as simple feature.

This stored query fetch ECMWF weather forecast for observation stations in Finland. The forcast is returned as simple feature form. By default, forecast is returned for the next 36 hours.

* Query ID: `ecmwf::forecast::surface::obsstations::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter starttime specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter endtime specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default, all parameters are returned.
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day. Default timestep is 60 minutes.


## ECMWF weather forecast for observation stations as time value pairs.

This stored query fetch ECMWF weather forecast for observation stations in Finland. The forcast is returned as time value pairs. By default, forecast is returned for the next 36 hours.

* Query ID: `ecmwf::forecast::surface::obsstations::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter starttime specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter endtime specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default, all parameters are returned.
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day. Default timestep is 60 minutes.
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## ECMWF Point Weather Forecast as multipointcoverage

ECMWF weather forecast fetched to a specific location returned in multi point coverage format. Location need to be specified as place or geoid or latlon query parameters.

* Query ID: `ecmwf::forecast::surface::point::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## ECMWF Point Weather Forecast as simple features

ECMWF weather forecast fetched to a specific location returned in simple feature format. Location need to be specified as place or geoid or latlon query parameters.

* Query ID: `ecmwf::forecast::surface::point::simple`
* Available arguments:
    * starttime
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## ECMWF Point Weather Forecast as time value pairs

ECMWF weather forecast fetched to a specific location returned in time value pair format. Location need to be specified as place or geoid or latlon query parameters.

* Query ID: `ecmwf::forecast::surface::point::timevaluepair`
* Available arguments:
    * starttime
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Aviation weather from aerodromes in Finland

This stored query return aviation weather messages from the essential aerodromes in Finland (predefined aerodrome set). Each message is constructed from a METAR weather report and converted to IWXXM (ICAO Meteorological Information Exchange Model) format. By default, the data is returned from the last 60 minutes. One can change the time range by using starttime and endtime parameters. It is also possible to request additional aerodromes which are included into the predefined aerodrome set by using icaocode parameter (duplicates are iqnored).

* Query ID: `fmi::avi::observations::finland::iwxxm`
* Available arguments:
    * starttime
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * icaocode
        * ICAO Code
        * Four-character alphanumeric code designating each airport around the world. (for example EFHK).


## Aviation weather from aerodromes in Finland

This stored query return the latest aviation weather messages (one per aerodrome) from the essential aerodromes in Finland (predefined aerodrome set). Each message is constructed from a METAR weather report and converted to IWXXM (ICAO Meteorological Information Exchange Model) format. By default, the latest messages are searched from the last 24 hours. One can change the time range by using starttime and endtime parameters. It is also possible to request additional aerodromes which are included into the predefined aerodrome set by using icaocode parameter (duplicates are ignored).

* Query ID: `fmi::avi::observations::finland::latest::iwxxm`
* Available arguments:
    * starttime
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * icaocode
        * ICAO Code
        * Four-character alphanumeric code designating each airport around the world. (for example EFHK).


## Aviation weather from aerodromes

This stored query return aviation weather messages. Each message is constructed from a METAR weather report and converted to IWXXM (ICAO Meteorological Information Exchange Model) format. By default, the data is returned from the 60 minutes. One can change the time range by using starttime and endtime parameters. At least one location parameter (icaocode, bbox, geoid) must be given to get non zero result.

* Query ID: `fmi::avi::observations::iwxxm`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * icaocode
        * ICAO Code
        * Four-character alphanumeric code designating each airport around the world.
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data. For example  27.4,68.6,27.5,68.7,epsg:4326 (lonMin,latMin,lonMax,latMax,srs).
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)


## Aviation weather from aerodromes

This stored query return the latest aviation weather messages from aerodromes. Each message is constructed from a METAR weather report and converted to IWXXM (ICAO Meteorological Information Exchange Model) format. By default, the latest message is searched from the last 24 hours. One can change the time range by using starttime and endtime parameters. At least one location parameter (icaocode, bbox, geoid) must be given to get non zero result.

* Query ID: `fmi::avi::observations::latest::iwxxm`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * icaocode
        * ICAO Code
        * Four-character alphanumeric code designating each airport around the world.
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data. For example  27.4,68.6,27.5,68.7,epsg:4326 (lonMin,latMin,lonMax,latMax,srs).
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)


## Environmental Monitoring Networks

This stored query can be used to fetch the metadata of environmental monitoring networks of Finnish Meteorological Institute's and other data producers. The metadata contains information about network name, period of activity, responsible party and an short description.

* Query ID: `fmi::ef::networks`
* Available arguments:
    * networkid
        * Network identifier
        * Identifier of the observation network.


## Environmental Monitoring Stations

This stored query can be used to fetch the metadata of environmental monitoring stations of Finnish Meteorological Institute's and other data producers. The metadata contains information about station name, location, period of activity and the networks for which station belongs to.

* Query ID: `fmi::ef::stations`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * networkid
        * Network identifier
        * Identifier of the observation network.
    * fmisid
        * Station identifier
        * Identifier of the observation station.


## Climate Scenarios

Mean temperature and precipitation amount scenarios for three periods of thirty years. The data contains 10x10km grid and is returned in GRIB format.

* Query ID: `fmi::forecast::climatology::scenario::grid`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.


## FMI-ENFUSER air quality forecast as grid

FMI-ENFUSER (The Finnish Meteorological Institute's ENvironmental information FUsion SERvice) is a novel air quality model that combines dispersion modelling techniques, information fusion algorithms and statistical approaches. The operational modelling system provides both real-time and forecasted, high resolution information on the urban air quality. This stored query provides near real-time information on Helsinki metropolitan air quality with a resolution of ~20m for the hourly concentrations of PM2.5, PM10, NO2, O3 and Air Quality Index (in a scale of 1 to 5) as a grid. New dataset will come available once in an hour.

* Query ID: `fmi::forecast::enfuser::airquality::helsinki-metropolitan::grid`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter specifies the begin of time interval to return data in ISO 8601 format (for example 2017-01-25T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter specifies the end of time interval to return data in ISO 8601 format (for example 2017-01-25T00:00:00Z).
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.


## Harmonie Scandinavia Hybrid Weather Forecast as Grid data

The stored query can be used to fetch Harmonie hybrid weather forecast data encoded in GRIB or NetCDF format. The model data covers the geographical area of Scandinavia and hybrid levels from 65 (near the model topography) to 12 (highest available elevation). New forecast dataset will come available every 6 hours. By default all the parameters, levels and timesteps are selected.

* Query ID: `fmi::forecast::harmonie::hybrid::grid`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2017-07-07T07:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2017-07-07T07:00:00Z).
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * levels
        * Hybrid levels
        * A comma separated list of levels (For example 40,30,20). By default all available levels are selected.
    * format
        * Dataset format.
        * Encoding format for the returned dataset. Formats available are grib1, grib2 and netcdf. Default format is grib2.


## Harmonie Hybrid Point Weather Forecast as multipointcoverage

The stored query can be used to fetch Harmonie hybrid weather forecast data in multi point coverage format. The model data covers the geographical area of Scandinavia and heights between 13 and 10000 meters from the model topography. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned from the height of 100 meters above the model topography and 50 hours from the request time.

* Query ID: `fmi::forecast::harmonie::hybrid::point::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * height
        * Height from the topography of forecast model
        * The request parameter specifies height in meters from the topography of forecast model.


## Harmonie Hybrid Point Weather Forecast as simple features

The stored query can be used to fetch Harmonie hybrid weather forecast data in simple feature format. The model data covers the geographical area of Scandinavia and heights between 13 and 10000 meters from the model topography. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned from the height of 100 meters above the model topography and 50 hours from the request time.

* Query ID: `fmi::forecast::harmonie::hybrid::point::simple`
* Available arguments:
    * starttime
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * height
        * Height from the topography of forecast model
        * The request parameter specifies height in meters from the topography of forecast model.


## Harmonie Hybrid Point Weather Forecast as time value pairs

The stored query can be used to fetch Harmonie hybrid weather forecast data in time value pair format. The model data covers the geographical area of Scandinavia and heights between 13 and 10000 meters from the model topography. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned from the height of 100 meters above the model topography and 50 hours from the request time.

* Query ID: `fmi::forecast::harmonie::hybrid::point::timevaluepair`
* Available arguments:
    * starttime
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * height
        * Height from the topography of forecast model
        * The request parameter specifies height in meters from the topography of forecast model.


## Harmonie Scandinavia Pressure Level Weather Forecast as Grid data

The stored query can be used to fetch Harmonie weather forecast data from pressure levels encoded in GRIB or NetCDF format. The model data covers the geographical area of Scandinavia and pressure levels: 300, 500, 700, 850, 925, 1000 hPa. New forecast dataset will come available every 6 hours. By default all the parameters, levels and timesteps are selected.

* Query ID: `fmi::forecast::harmonie::pressure::grid`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2017-07-07T07:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2017-07-07T07:00:00Z).
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * levels
        * Pressure levels
        * A comma separated list of pressure levels (For example 400,850,1000). By default all available levels are selected.
    * format
        * Dataset format.
        * Encoding format for the returned dataset. Formats available are grib1, grib2 and netcdf. Default format is grib2.


## Harmonie Pressure Point Weather Forecast as multipointcoverage

The stored query can be used to fetch Harmonie pressure level weather forecast data in multi point coverage format. The model data covers the geographical area of Scandinavia and pressure levels 300, 500, 700, 850, 925, 1000 hPa. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned from the level of 850 hPa and 50 hours from the request time.

* Query ID: `fmi::forecast::harmonie::pressure::point::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * pressure
        * Pressure value
        * The request parameter specifies level of pressure in hPa from which to return data.


## Harmonie Pressure Point Weather Forecast as simple features

The stored query can be used to fetch Harmonie pressure level weather forecast data in simple feature format. The model data covers the geographical area of Scandinavia and pressure levels 300, 500, 700, 850, 925, 1000 hPa. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned from the level of 850 hPa and 50 hours from the request time.

* Query ID: `fmi::forecast::harmonie::pressure::point::simple`
* Available arguments:
    * starttime
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * pressure
        * Pressure value
        * The request parameter specifies level of pressure in hPa from which to return data.


## Harmonie Pressure Point Weather Forecast as time value pairs

The stored query can be used to fetch Harmonie pressure level weather forecast data in time value pair format. The model data covers the geographical area of Scandinavia and pressure levels 300, 500, 700, 850, 925, 1000 hPa. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned from the level of 850 hPa and 50 hours from the request time.

* Query ID: `fmi::forecast::harmonie::pressure::point::timevaluepair`
* Available arguments:
    * starttime
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * pressure
        * Pressure value
        * The request parameter specifies level of pressure in hPa from which to return data.


## Harmonie Scandinavia Surface Level Weather Forecast as Grid data

The stored query can be used to fetch Harmonie surface level weather forecast data encoded in GRIB or NetCDF format. The model data covers the geographical area of Scandinavia. New forecast dataset will come available every 6 hours. By default all the parameters and timesteps are selected.

* Query ID: `fmi::forecast::harmonie::surface::grid`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2017-07-07T07:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2017-07-07T07:00:00Z).
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
		Default: Pressure,GeopHeight,Temperature,DewPoint,Humidity,WindDirection,
		WindSpeedMS,WindUMS,WindVMS,PrecipitationAmount,TotalCloudCover,LowCloudCover,
		MediumCloudCover,HighCloudCover,RadiationGlobal,RadiationGlobalAccumulation,
		RadiationNetSurfaceLWAccumulation,RadiationNetSurfaceSWAccumulation,
		RadiationSWAccumulation,Visibility,WindGust,Cape
    * format
        * Dataset format.
        * Encoding format for the returned dataset. Formats available are grib2 and netcdf. Default format is grib2.


## Harmonie Surface Point Weather Forecast as multipointcoverage

The stored query can be used to fetch Harmonie surface level weather forecast in multi point coverage format. The model data covers the geographical area of Scandinavia. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned 50 hours from the request time.

* Query ID: `fmi::forecast::harmonie::surface::point::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Harmonie Surface Point Weather Forecast as simple features

The stored query can be used to fetch Harmonie surface level weather forecast in simple feature format. The model data covers the geographical area of Scandinavia. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned 50 hours from the request time.

* Query ID: `fmi::forecast::harmonie::surface::point::simple`
* Available arguments:
    * starttime
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Harmonie Surface Point Weather Forecast as time value pairs

The stored query can be used to fetch Harmonie surface level weather forecast in time value pair format. The model data covers the geographical area of Scandinavia. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned 50 hours from the request time.

* Query ID: `fmi::forecast::harmonie::surface::point::timevaluepair`
* Available arguments:
    * starttime
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## HBM Current Model Grid

HBM forecast model provides sea currents and water temperature forecast as grid data encoded in GRIB format.

* Query ID: `fmi::forecast::hbm::grid`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * format
        * Dataset format.
        * Encoding format for the returned dataset. Formats available are grib1, grib2 and netcdf. Default format is grib2.
    * levels
        * Vertical level
        * A comma separated list of vertical levels of sea (For exmaple 0,100,200). Available levels are 0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,150,200,300,400. Default level is 0.


## HBM Current Model Point

HBM forecast model provides sea currents and water temperature forecast. This stored query provides the data as point data encoded in multi point coverage format.

* Query ID: `fmi::forecast::hbm::point::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## HBM Current Model Point

HBM forecast model provides sea currents and water temperature forecast. This stored query provides the data as point data encoded in simple feature format.

* Query ID: `fmi::forecast::hbm::point::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## HBM Current Model Point

HBM forecast model provides sea currents and water temperature forecast. This stored query provides the data as point data encoded in time value pair format.

* Query ID: `fmi::forecast::hbm::point::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Helsinki multi-category ice model as a grid.

This Stored Query request retrieve Helsinki multi-category ice model forecast raw dataset as a grid.

* Query ID: `fmi::forecast::helmi::grid`
* Available arguments:
    * producer
        * Producer
        * Model or process which provides the data.
    * starttime
        * Begin of the time interval
        * Parameter starttime specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter endtime specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return. Default parameters are Concentration, NorthwardIceVelocity, EastwardIceVelocity, MeanIceThickness
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (min Longitude, min Latitude, max Longitude, max Latitude) Default bounding box is 16.7168,56.7416,30.51542,65.99345.
    * format
        * Dataset format.
        * Encoding format for the returned dataset. Formats available are grib1, grib2 and netcdf. Default format is General Regularly-distributed Information in Binary form edition 2 (GRIB2).


## Hydrodynamic Current Model Grid

Hydrodynamic forecast model provides sea currents and water temperature forecast as grid data encoded in GRIB format.

* Query ID: `fmi::forecast::hydrodyn::grid`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * format
        * Dataset format.
        * Encoding format for the returned dataset. Formats available are grib1, grib2 and netcdf. Default format is grib2.
    * levels
        * Vertical level
        * A comma separated list of vertical levels of sea (For exmaple 0,100,200). Available levels are 0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,150,200,300,400. Default level is 0.


## Hydrodynamic Current Model Point

Hydrodynamic forecast model provides sea currents and water temperature forecast. This stored query provides the data as point data encoded in multi point coverage format.

* Query ID: `fmi::forecast::hydrodyn::point::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Hydrodynamic Current Model Point

Hydrodynamic forecast model provides sea currents and water temperature forecast. This stored query provides the data as point data encoded in simple feature format.

* Query ID: `fmi::forecast::hydrodyn::point::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Hydrodynamic Current Model Point

Hydrodynamic forecast model provides sea currents and water temperature forecast. This stored query provides the data as point data encoded in time value pair format.

* Query ID: `fmi::forecast::hydrodyn::point::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Harmonie (MEPS) Scandinavia Hybrid Weather Forecast as Grid data

The stored query can be used to fetch Harmonie (MEPS) hybrid weather forecast data encoded in GRIB or NetCDF format. The model data covers the geographical area of Scandinavia and hybrid levels from 65 (near the model topography) to 12 (highest available elevation). New forecast dataset will come available every 6 hours. By default all the parameters, levels and timesteps are selected.

* Query ID: `fmi::forecast::meps::hybrid::grid`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2017-07-07T07:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2017-07-07T07:00:00Z).
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * levels
        * Hybrid levels
        * A comma separated list of levels (For example 40,30,20). By default all available levels are selected.
    * format
        * Dataset format.
        * Encoding format for the returned dataset. Formats available are grib1, grib2 and netcdf. Default format is grib2.


## Harmonie (MEPS) Hybrid Point Weather Forecast as multipointcoverage

The stored query can be used to fetch Harmonie (MEPS) hybrid weather forecast data in multi point coverage format. The model data covers the geographical area of Scandinavia and heights between 13 and 10000 meters from the model topography. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned from the height of 100 meters above the model topography and 50 hours from the request time.

* Query ID: `fmi::forecast::meps::hybrid::point::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * height
        * Height from the topography of forecast model
        * The request parameter specifies height in meters from the topography of forecast model.


## Harmonie (MEPS) Hybrid Point Weather Forecast as simple features

The stored query can be used to fetch Harmonie (MEPS) hybrid weather forecast data in simple feature format. The model data covers the geographical area of Scandinavia and heights between 13 and 10000 meters from the model topography. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned from the height of 100 meters above the model topography and 50 hours from the request time.

* Query ID: `fmi::forecast::meps::hybrid::point::simple`
* Available arguments:
    * starttime
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * height
        * Height from the topography of forecast model
        * The request parameter specifies height in meters from the topography of forecast model.


## Harmonie (MEPS) Hybrid Point Weather Forecast as time value pairs

The stored query can be used to fetch Harmonie (MEPS) hybrid weather forecast data in time value pair format. The model data covers the geographical area of Scandinavia and heights between 13 and 10000 meters from the model topography. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned from the height of 100 meters above the model topography and 50 hours from the request time.

* Query ID: `fmi::forecast::meps::hybrid::point::timevaluepair`
* Available arguments:
    * starttime
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * height
        * Height from the topography of forecast model
        * The request parameter specifies height in meters from the topography of forecast model.


## Harmonie (MEPS) Scandinavia Pressure Level Weather Forecast as Grid data

The stored query can be used to fetch Harmonie (MEPS) weather forecast data from pressure levels encoded in GRIB or NetCDF format. The model data covers the geographical area of Scandinavia and pressure levels: 300, 500, 700, 850, 925, 1000 hPa. New forecast dataset will come available every 6 hours. By default all the parameters, levels and timesteps are selected.

* Query ID: `fmi::forecast::meps::pressure::grid`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2017-07-07T07:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2017-07-07T07:00:00Z).
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * levels
        * Pressure levels
        * A comma separated list of pressure levels (For example 400,850,1000). By default all available levels are selected.
    * format
        * Dataset format.
        * Encoding format for the returned dataset. Formats available are grib1, grib2 and netcdf. Default format is grib2.


## Harmonie (MEPS) Pressure Point Weather Forecast as multipointcoverage

The stored query can be used to fetch Harmonie (MEPS) pressure level weather forecast data in multi point coverage format. The model data covers the geographical area of Scandinavia and pressure levels 300, 500, 700, 850, 925, 1000 hPa. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned from the level of 850 hPa and 50 hours from the request time.

* Query ID: `fmi::forecast::meps::pressure::point::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * pressure
        * Pressure value
        * The request parameter specifies level of pressure in hPa from which to return data.


## Harmonie (MEPS) Pressure Point Weather Forecast as simple features

The stored query can be used to fetch Harmonie (MEPS) pressure level weather forecast data in simple feature format. The model data covers the geographical area of Scandinavia and pressure levels 300, 500, 700, 850, 925, 1000 hPa. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned from the level of 850 hPa and 50 hours from the request time.

* Query ID: `fmi::forecast::meps::pressure::point::simple`
* Available arguments:
    * starttime
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * pressure
        * Pressure value
        * The request parameter specifies level of pressure in hPa from which to return data.


## Harmonie (MEPS) Pressure Point Weather Forecast as time value pairs

The stored query can be used to fetch Harmonie (MEPS) pressure level weather forecast data in time value pair format. The model data covers the geographical area of Scandinavia and pressure levels 300, 500, 700, 850, 925, 1000 hPa. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned from the level of 850 hPa and 50 hours from the request time.

* Query ID: `fmi::forecast::meps::pressure::point::timevaluepair`
* Available arguments:
    * starttime
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * pressure
        * Pressure value
        * The request parameter specifies level of pressure in hPa from which to return data.


## Harmonie (MEPS) Scandinavia Surface Level Weather Forecast as Grid data

The stored query can be used to fetch Harmonie (MEPS) surface level weather forecast data encoded in GRIB or NetCDF format. The model data covers the geographical area of Scandinavia. New forecast dataset will come available every 6 hours. By default all the parameters and timesteps are selected.

* Query ID: `fmi::forecast::meps::surface::grid`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2017-07-07T07:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2017-07-07T07:00:00Z).
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
		Default: Pressure,GeopHeight,Temperature,DewPoint,Humidity,WindDirection,
		WindSpeedMS,WindUMS,WindVMS,PrecipitationAmount,TotalCloudCover,LowCloudCover,
		MediumCloudCover,HighCloudCover,RadiationGlobal,RadiationGlobalAccumulation,
		RadiationNetSurfaceLWAccumulation,RadiationNetSurfaceSWAccumulation,
		RadiationSWAccumulation,Visibility,WindGust,Cape
    * format
        * Dataset format.
        * Encoding format for the returned dataset. Formats available are grib2 and netcdf. Default format is grib2.


## Harmonie (MEPS) Surface Point Weather Forecast as multipointcoverage

The stored query can be used to fetch Harmonie (MEPS) surface level weather forecast in multi point coverage format. The model data covers the geographical area of Scandinavia. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned 50 hours from the request time.

* Query ID: `fmi::forecast::meps::surface::point::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Harmonie (MEPS) Surface Point Weather Forecast as simple features

The stored query can be used to fetch Harmonie (MEPS) surface level weather forecast in simple feature format. The model data covers the geographical area of Scandinavia. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned 50 hours from the request time.

* Query ID: `fmi::forecast::meps::surface::point::simple`
* Available arguments:
    * starttime
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Harmonie (MEPS) Surface Point Weather Forecast as time value pairs

The stored query can be used to fetch Harmonie (MEPS) surface level weather forecast in time value pair format. The model data covers the geographical area of Scandinavia. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned 50 hours from the request time.

* Query ID: `fmi::forecast::meps::surface::point::timevaluepair`
* Available arguments:
    * starttime
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## OAAS Sea Level Model Point

OAAS forecast model provides sea level height forecast to points. This stored query provides point data encoded in multi point coverage format.

* Query ID: `fmi::forecast::oaas::sealevel::point::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21


## OAAS Sea Level Model Point

OAAS forecast model provides sea level height forecast to points. This stored query provides point data encoded in simple feature format.

* Query ID: `fmi::forecast::oaas::sealevel::point::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## OAAS Sea Level Model Point

OAAS forecast model provides sea level height forecast to points. This stored query provides point data encoded in time value pair format.

* Query ID: `fmi::forecast::oaas::sealevel::point::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## OAAS Sea Level Model Point

OAAS forecast model provides sea level height forecast to points. This stored query provides point data encoded in multi point coverage format.

* Query ID: `fmi::forecast::sealevel::point::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21


## OAAS Sea Level Model Point

OAAS forecast model provides sea level height forecast to points. This stored query provides point data encoded in simple feature format.

* Query ID: `fmi::forecast::sealevel::point::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## OAAS Sea Level Model Point

OAAS forecast model provides sea level height forecast to points. This stored query provides point data encoded in time value pair format.

* Query ID: `fmi::forecast::sealevel::point::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## SILAM air quality forecast as grid

SILAM (System for Integrated modeLling of Atmospheric coMposition) is a global-to-meso-scale dispersion model developed for atmospheric composition, air quality, and emergency decision support applications. This stored query provides an air quality forecast for the main ambient pollutants: CO, NO, NO2, O3, SO2, PM10 and PM25. The model data covers the geographical area of Europe. New forecast dataset will come available once in a day. The data is returened as a grid. Output file format is NetCDF.

* Query ID: `fmi::forecast::silam::airquality::surface::grid`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO 8601 format (for example 2017-01-25T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO 8601 format (for example 2017-01-25T00:00:00Z).
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.


## SILAM air quality forecast as point data

SILAM (System for Integrated modeLling of Atmospheric coMposition) is a global-to-meso-scale dispersion model developed for atmospheric composition, air quality, and emergency decision support applications. This stored query provides an air quality forecast for the main ambient pollutants: CO, NO, NO2, O3, SO2, PM10 and PM25. The model data covers the geographical area of Europe. New forecast dataset will come available once in a day. The data is returened in multi point coverage format.

* Query ID: `fmi::forecast::silam::airquality::surface::point::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO 8601 format (for example 2017-01-25T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO 8601 format (for example 2017-01-25T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes.
    * parameters
        * Parameters to return
        * Comma separated list of air quality parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example http://www.opengis.net/def/crs/EPSG/0/4326
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## SILAM air quality forecast as simple feature

SILAM (System for Integrated modeLling of Atmospheric coMposition) is a global-to-meso-scale dispersion model developed for atmospheric composition, air quality, and emergency decision support applications. This stored query provides an air quality forecast for the main ambient pollutants: CO, NO, NO2, O3, SO2, PM10 and PM25. The model data covers the geographical area of Europe. New forecast dataset will come available once in a day. The data is returened as simple features.

* Query ID: `fmi::forecast::silam::airquality::surface::point::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO 8601 format (for example 2017-01-25T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO 8601 format (for example 2017-01-25T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes.
    * parameters
        * Parameters to return
        * Comma separated list of air quality parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example http://www.opengis.net/def/crs/EPSG/0/4326
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## SILAM air quality forecast as as time value pairs

SILAM (System for Integrated modeLling of Atmospheric coMposition) is a global-to-meso-scale dispersion model developed for atmospheric composition, air quality, and emergency decision support applications. This stored query provides an air quality forecast for the main ambient pollutants: CO, NO, NO2, O3, SO2, PM10 and PM25. The model data covers the geographical area of Europe. New forecast dataset will come available once in a day. The data is returened as as time value pairs.

* Query ID: `fmi::forecast::silam::airquality::surface::point::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO 8601 format (for example 2017-01-25T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO 8601 format (for example 2017-01-25T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes.
    * parameters
        * Parameters to return
        * Comma separated list of air quality parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example http://www.opengis.net/def/crs/EPSG/0/4326
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## WAM Wave Model Grid

WAM forecast model provides wave height forecast as grid data encoded in GRIB format.

* Query ID: `fmi::forecast::wam::grid`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.


## WAM Wave Model Point

WAM forecast model provides wave height forecast. This stored query provides point data encoded in multi point coverage format.

* Query ID: `fmi::forecast::wam::point::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21


## WAM Wave Model Point

WAM forecast model provides wave height forecast. This stored query provides point data encoded in simple feature format.

* Query ID: `fmi::forecast::wam::point::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21


## WAM Wave Model Point

WAM forecast model provides wave height forecast. This stored query provides point data encoded in time value pair format. Location has to be specified as geoid or latlon-coordinates.

* Query ID: `fmi::forecast::wam::point::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Hourly Air Quality Observations

Hourly air quality observations from weather stations of Finnish Meteorological Institute. By default, all the station are selected and the data is returned from the last 24 hours. The data is returned as multi point coverage format.

* Query ID: `fmi::observations::airquality::hourly::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2015-03-13T10:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2015-03-13T12:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 24,60,25,61
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Helsinki).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)


## Hourly Air Quality Observations

Hourly air quality observations from weather stations or Finnish Meteorological Institute. By default, all the station are selected and the data is returned from the last 24 hours. The data is returned as a simple feature format.

* Query ID: `fmi::observations::airquality::hourly::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2015-03-13T10:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2015-03-13T12:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 24,60,25,61
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Helsinki).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around a location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Hourly Air Quality Observations

Hourly air quality observations from weather stations of Finnish Meteorological Institute. By default, all the station are selected and the data is returned from the last 24 hours. The data is returned as timevaluepair format.

* Query ID: `fmi::observations::airquality::hourly::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2015-03-13T10:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2015-03-13T12:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 24,60,25,61
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Helsinki).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around a location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Salinity and Water temperature observations

Salinity and water temperature observations (CTD observations) from fixed locations. Available parameters are water temperature, salinity, conductivity, density, and the speed of sound as a function of water pressure (corresponding approximately to depth). The data is returned in multipointcoverage format.

* Query ID: `fmi::observations::ctd::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.


## Salinity and Water temperature observations

Salinity and water temperature observations (CTD observations) from fixed locations. Available parameters are water temperature, salinity, conductivity, density, and the speed of sound as a function of water pressure (corresponding approximately to depth). The data is returned in a time value pair format.

* Query ID: `fmi::observations::ctd::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Lightning Strikes

The response contains all detected lightning strikes in Northern Europe. Observations are mainly ground flashes but some of cloud flashes are also detected.

* Query ID: `fmi::observations::lightning::multipointcoverage`
* Available arguments:
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).


## Lightning Strikes

The response contains all detected lightning strikes in Northern Europe. Observations are mainly ground flashes but some of cloud flashes are also detected.

* Query ID: `fmi::observations::lightning::simple`
* Available arguments:
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).


## Mareograph Water Temperature Daily Statistical Values

Daily water temperature average, minimum and maximum from 14 locations. By default, the data is returned from last 744 hours. The data is retuned in multi point coverage format.

* Query ID: `fmi::observations::mareograph::daily::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.


## Mareograph Water Temperature Daily Statistical Values

Daily water temperature average, minimum and maximum from 14 locations. By default, the data is returned from last 744 hours. The data is retuned in simple feature format.

* Query ID: `fmi::observations::mareograph::daily::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.


## Mareograph Water Temperature Daily Statistical Values

Daily water temperature average, minimum and maximum from 14 locations. By default, the data is returned from last 744 hours. The data is retuned in time value pair format.

* Query ID: `fmi::observations::mareograph::daily::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.


## Sea Level and Temperature Observations

Sea level and temperature observations from 14 locations. Time step is 1 minute. The data is retuned in multi point coverage format.

* Query ID: `fmi::observations::mareograph::instant::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.


## Sea Level and Temperature Observations

Sea level and temperature observations from 14 locations. Time step is 1 minute. The data is retuned in simple feature format.

* Query ID: `fmi::observations::mareograph::instant::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.


## Sea Level and Temperature Observations

Sea level and temperature observations from 14 locations. Time step is 1 minute. The data is returned in time value pair format.

* Query ID: `fmi::observations::mareograph::instant::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Monthly water level and temperature observations of 30-year normal period.

Monthly water level and temperature observations of 30-year normal period 1991 - 2020. Notice that there is only data at the begin of each month of the first year of the period. By default data is returned from 15 locations. The data is returned in multipointcoverage format.

* Query ID: `fmi::observations::mareograph::monthly::30year::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default all parameters will be returned.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Hanko).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Monthly water level and temperature observations of 30-year normal period.

Monthly water level and temperature observations of 30-year normal period 1991 - 2020. Notice that there is only data at the begin of each month of the first year of the period. By default data is returned from 15 locations. The data is returned in simple feature format.

* Query ID: `fmi::observations::mareograph::monthly::30year::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default all parameters will be returned.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Hanko).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Monthly water level and temperature observations of 30-year normal period.

Monthly water level and temperature observations of 30-year normal period 1991 - 2020. Notice that there is only data at the begin of each month of the first year of the period. By default data is returned from 15 locations. The data is returned in timevaluepair format.

* Query ID: `fmi::observations::mareograph::monthly::30year::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default all parameters will be returned.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Hanko).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Mareograph Water Temperature Monthly Statistical Values

Monthly water temperature average, minimum and maximum from 14 locations. By default, the data is returned from last 12 months. The data is retuned in multi point coverage format.

* Query ID: `fmi::observations::mareograph::monthly::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.


## Mareograph Water Temperature Monthly Statistical Values

Monthly water temperature average, minimum and maximum from 14 locations. By default, the data is returned from last 12 months. The data is retuned in simple feature format.

* Query ID: `fmi::observations::mareograph::monthly::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.


## Mareograph Water Temperature Monthly Statistical Values

Monthly water temperature average, minimum and maximum from 14 locations. By default, the data is returned from last 12 months. The data is retuned in time value pair format.

* Query ID: `fmi::observations::mareograph::monthly::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.


## Sea Level and Temperature Observations

Sea level and temperature observations from 14 locations. Time step is 60 minutes. The data is retuned in multi point coverage format.

* Query ID: `fmi::observations::mareograph::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.


## Sea Level and Temperature Observations

Sea level and temperature observations from 14 locations. Time step is 60 minutes. The data is retuned in simple feature format.

* Query ID: `fmi::observations::mareograph::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.


## Sea Level and Temperature Observations

Sea level and temperature observations from 14 locations. Time step is 60 minutes. The data is returned in time value pair format.

* Query ID: `fmi::observations::mareograph::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Yearly water level observations of 30-year normal period.

Yearly water level observations of 30-year normal period 1991 - 2020. Notice that there is only data at the begin of the period. By default data is returned from 13 locations. The data is returned in multipointcoverage format.

* Query ID: `fmi::observations::mareograph::yearly::30year::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default all parameters will be returned.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Hanko).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Yearly water level observations of 30-year normal period.

Yearly water level observations of 30-year normal period 1991 - 2020. Notice that there is only data at the begin of the period. By default data is returned from 13 locations. The data is returned in simple feature format.

* Query ID: `fmi::observations::mareograph::yearly::30year::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default all parameters will be returned.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Hanko).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Yearly water level observations of 30-year normal period.

Yearly water level observations of 30-year normal period 1991 - 2020. Notice that there is only data at the begin of the period. By default data is returned from 13 locations. The data is returned in timevaluepair format.

* Query ID: `fmi::observations::mareograph::yearly::30year::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default all parameters will be returned.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Hanko).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Sun Radiation Observations

Sun radiation observations from weather stations. By default the data is returned from last 1 hour and from stations in Sodankylä, Jokioinen, Helsinki, Parainen, Vantaa, Jyväskylä, Sotkamo and Utsjoki. The data is returned in 'multipointcoverage' format.

* Query ID: `fmi::observations::radiation::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.


## Sun Radiation Observations

Sun radiation observations from weather stations. By default the data is returned from last 1 hour and from stations in Sodankylä, Jokioinen, Helsinki, Parainen, Vantaa, Jyväskylä, Sotkamo and Utsjoki. The data is returned in 'simple feature' format.

* Query ID: `fmi::observations::radiation::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.


## Sun Radiation Observations

Sun radiation observations from weather stations. By default the data is returned from last 1 hour and from stations in Sodankylä, Jokioinen, Helsinki, Parainen, Vantaa, Jyväskylä, Sotkamo and Utsjoki. The data is returned in 'timevaluepair' format.

* Query ID: `fmi::observations::radiation::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Manual Sea Ice Observations

Manually made sea ice observations from The Baltic Sea. By default, the data is returned from last 30 days.  At least one location parameter (geoid/place/fmisid/wmo/bbox/latlon) has to be given. The data is returned as a time value pair format.

* Query ID: `fmi::observations::seaice::manual::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 63.890,22.943
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Hourly Soil Observations

Hourly minimum, maximum and average soil values from weather stations. By default, the data is returned from last 12 hour.  At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned as multi point coverage format.

* Query ID: `fmi::observations::soil::hourly::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Salkola,Somero).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Hourly Soil Observations

Hourly minimum, maximum and average soil values from weather stations. By default, the data is returned from last 12 hour.  At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned as simple feature format.

* Query ID: `fmi::observations::soil::hourly::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Salkola,Somero).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Hourly Soil Observations

Hourly minimum, maximum and average soil values from weather stations. By default, the data is returned from last 12 hour.  At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned as a time value pair format.

* Query ID: `fmi::observations::soil::hourly::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Salkola,Somero).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Sea Surface Temperature Observations

Sea surface temperature observations from a range of measurements. Time step is variable and depends on the measurement point. The data is retuned in simple feature format.

* Query ID: `fmi::observations::surfacetemperature::daily::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.


## Sea Surface Temperature Observations

Sea surface temperature observations from a range of measurements. Time step is variable and depends on the measurement point. The data is retuned in simple feature format.

* Query ID: `fmi::observations::surfacetemperature::monthly::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.


## Sea Surface Temperature Observations

Sea surface temperature observations from a range of measurements. Time step is variable and depends on the measurement point. The data is retuned in simple feature format.

* Query ID: `fmi::observations::surfacetemperature::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.


## Buoy Water Temperature Daily Statistical Values

Daily water temperature average, minimum and maximum from buoys. By default, the data is returned from last 744 hours. The data is returned in multi point coverage format.

* Query ID: `fmi::observations::wave::daily::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.


## Buoy Water Temperature Daily Statistical Values

Daily water temperature average, minimum and maximum from buoys. By default, the data is returned from last 744 hours. The data is returned in simple feature format.

* Query ID: `fmi::observations::wave::daily::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.


## Buoy Water Temperature Daily Statistical Values

Daily water temperature average, minimum and maximum from buoys. By default, the data is returned from last 744 hours. The data is returned in time value pair format.

* Query ID: `fmi::observations::wave::daily::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.


## Buoy Water Temperature Monthly Statistical Values

Monthly water temperature average, minimum and maximum from buoys. By default, the data is returned from last 12 months. The data is returned in multi point coverage format.

* Query ID: `fmi::observations::wave::monthly::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.


## Buoy Water Temperature Monthly Statistical Values

Monthly water temperature average, minimum and maximum from buoys. By default, the data is returned from last 12 months. The data is returned in simple feature format.

* Query ID: `fmi::observations::wave::monthly::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.


## Buoy Water Temperature Monthly Statistical Values

Monthly water temperature average, minimum and maximum from buoys. By default, the data is returned from last 12 months. The data is returned in time value pair format.

* Query ID: `fmi::observations::wave::monthly::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.


## Wave and Water temperature observations

Wave and water temperature observations from buoys. Available parameters are significant wave height, wave direction, deviation of wave direction, modal period and water temperature. Some buoys return only temperature values. Time step is 30 minutes. The data is returned in multipointcoverage format.

* Query ID: `fmi::observations::wave::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.


## Wave and Water temperature observations

Wave and water temperature observations from buoys. Available parameters are significant wave height, wave direction, deviation of wave direction, modal period and water temperature. Some buoys return only temperature values. Time step is 30 minutes. The data is returned in simple feature format.

* Query ID: `fmi::observations::wave::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.


## Wave and Water temperature observations

Wave and water temperature observations from buoys. Available parameters are significant wave height, wave direction, deviation of wave direction, modal period and water temperature. Some buoys return only temperature values. Time step is 30 minutes. The data is returned in time value pair format.

* Query ID: `fmi::observations::wave::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Weather observations for cities as multipointcoverage.

Weather observations for cities in Finland as multipointcoverage.

* Query ID: `fmi::observations::weather::cities::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter starttime specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter endtime specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * timestep
        * The time step in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.


## Weather observations for cities as simple feature.

Weather observations for cities in Finland as simple feature.

* Query ID: `fmi::observations::weather::cities::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter starttime specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter endtime specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * timestep
        * The time step in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.


## Weather observations for cities as time value pairs.

Weather observations for cities in Finland as time value pairs.

* Query ID: `fmi::observations::weather::cities::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter starttime specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter endtime specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Daily Weather Observations

Daily weather observations from weather stations. Default set contains daily precipitation rate, mean temperature, snow depth, and minimum  and maximum temperature. By default, the data is returned from last 744 hours. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned in multi point coverage format.

* Query ID: `fmi::observations::weather::daily::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Daily Weather Observations

Daily weather observations from weather stations. Default set contains daily precipitation rate, mean temperature, snow depth, and minimum  and maximum temperature. By default, the data is returned from last 744 hours. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned in simple feature format.

* Query ID: `fmi::observations::weather::daily::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Daily Weather Observations

Daily weather observations from weather stations. Default set contains daily precipitation rate, mean temperature, snow depth, minimum temperature and maximum temperature. By default, the data is returned from last 744 hours. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned time value pair format.

* Query ID: `fmi::observations::weather::daily::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Dropsonde observations

This stored query returns atmospheric dropsonde observations in multipointcoverage format. By default dropsonde observations are returned from the observation stations of Finland the last 12 hours.

* Query ID: `fmi::observations::weather::dropsonde::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2017-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2017-02-27T00:00:00Z).
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 23,60,24,61
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Jokioinen).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latest
        * Return only latest measurements
        * If only latest mearurements are wanted to return for each station use value 'true' otherwise 'false'.
    * altituderange
        * Altitude range
        * Altitude range to return data  (minAltitude,maxAltitude) in meters. For example 5000.0,10000.0.
    * pressurerange
        * Pressure range
        * Pressure range to return data  (minPressure,maxPressure) in units of hPa. For example 800.0,850.0
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::7904


## Hourly Weather Observations

Hourly weather observations from weather stations. Default set contains hourly air temperature average, maximum and minimum, air relative humidity average, wind speed average, minumum (10 minute average) and maximum (10 minute average), wind direction average, wind gust speed maximum (3 second average), rain accumulated, rain intensity maximum, air pressure average and the most significant weather code. By default, the data is returned from last 24 hours. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned in multi point coverage format.

* Query ID: `fmi::observations::weather::hourly::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Hourly Weather Observations

Hourly weather observations from weather stations. Default set contains hourly air temperature average, maximum and minimum, air relative humidity average, wind speed average, minumum (10 minute average) and maximum (10 minute average), wind direction average, wind gust speed maximum (3 second average), rain accumulated, rain intensity maximum, air pressure average and the most significant weather code. By default, the data is returned from last 24 hours. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned in simple format.

* Query ID: `fmi::observations::weather::hourly::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Hourly Weather Observations

Hourly weather observations from weather stations. Default set contains hourly air temperature average, maximum and minimum, air relative humidity average, wind speed average, minumum (10 minute average) and maximum (10 minute average), wind direction average, wind gust speed maximum (3 second average), rain accumulated, rain intensity maximum, air pressure average and the most significant weather code. By default, the data is returned from last 24 hours. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned in time value pair format.

* Query ID: `fmi::observations::weather::hourly::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Instantaneous profile observations from masts

This stored query return instantaneous profile observations from masts in multipointcoverage format. By default latest observation of the available meteo paramters are returned in 10 minute resolution. At least one location has to be given.

* Query ID: `fmi::observations::weather::mast::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Espoo).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Monthly weather observations of 30-year normal period

Monthly Weather Observations of 30-year normal period. By default, the data is returned from the normal period of 1991 - 2020. There is available the following normal periods: 1971 - 2000, 1981 - 2010, 1991 - 2020. Notice that there is only data at the begin of the period. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned in multi point coverage format.

* Query ID: `fmi::observations::weather::monthly::30year::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default all parameters will be returned.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Hanko).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Monthly weather observations of 30-year normal period

Monthly Weather Observations of 30-year normal period. By default, the data is returned from the normal period of 1991 - 2020. There is available the following normal periods: 1971 - 2000, 1981 - 2010, 1991 - 2020. Notice that there is only data at the begin of the period. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned in simple feature format.

* Query ID: `fmi::observations::weather::monthly::30year::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default all parameters will be returned.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Hanko).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Monthly weather observations of 30-year normal period

Monthly Weather Observations of 30-year normal period. By default, the data is returned from the normal period of 1991 - 2020. There is available the following normal periods: 1971 - 2000, 1981 - 2010, 1991 - 2020. Notice that there is only data at the begin of the period. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned in time value pair format.

* Query ID: `fmi::observations::weather::monthly::30year::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default all parameters will be returned.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Hanko).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Monthly Weather Observations

Monthly precipitation rate and mean temperature interpolated into a grid. The data is returned in GRIB format.

* Query ID: `fmi::observations::weather::monthly::grid`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.


## Monthly Weather Observations

Monthly weather observations from weather stations. Default set contains monthly precipitation rate, mean temperature. By default, the data is returned from last 12 months. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned in multi point coverage format.

* Query ID: `fmi::observations::weather::monthly::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Monthly Weather Observations

Monthly weather observations from weather stations. Default set contains monthly precipitation rate, mean temperature. By default, the data is returned from last 12 months. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned in simple feature format.

* Query ID: `fmi::observations::weather::monthly::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Monthly Weather Observations

Monthly weather observations from weather stations. Default set contains monthly precipitation rate, mean temperature. By default, the data is returned from last 12 months. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned in time value pair format.

* Query ID: `fmi::observations::weather::monthly::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Instantaneous Weather Observations

Real time weather observations from weather stations. Default set contains wind speed, direction, gust, temperature, relative humidity, dew point, pressure reduced to sea level, one hour precipitation amount, visibility and cloud cover. By default, the data is returned from last 12 hour. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned as a multi point coverage format.

* Query ID: `fmi::observations::weather::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Instantaneous Weather Observations

Real time weather observations from weather stations. Default set contains wind speed, direction, gust, temperature, relative humidity, dew point, pressure reduced to sea level, one hour precipitation amount, visibility and cloud cover. By default, the data is returned from last 12 hour. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned as a simple feature format.

* Query ID: `fmi::observations::weather::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Sounding observations

This stored query returns atmospheric sounding observations in multipointcoverage format. By default sounding observations are returned from the observation stations of Finland the last 12 hours.

* Query ID: `fmi::observations::weather::sounding::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2017-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2017-02-27T00:00:00Z).
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 23,60,24,61
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Jokioinen).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latest
        * Return only latest soundings
        * If only latest soundings is wanted to return for each station use value 'true' otherwise 'false'.
    * altituderange
        * Altitude range
        * Altitude range to return data  (minAltitude,maxAltitude) in meters. For example 5000.0,10000.0.
    * pressurerange
        * Pressure range
        * Pressure range to return data  (minPressure,maxPressure) in units of hPa. For example 800.0,850.0
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::7904
    * soundingtype
        * Sounding type
        * Sounding type


## Instantaneous Weather Observations

Real time weather observations from weather stations. Default set contains air temperatire, wind speed, gust speed, wind direction, relative humidity, dew point, one hour precipitation amount, precipitation intensity, snow depth, pressure reduced to sea level and visibility. By default, the data is returned from last 12 hour.  At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned as a time value pair format.

* Query ID: `fmi::observations::weather::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Yearly weather observations of 30-year normal period

Yearly Weather Observations of 30-year normal period. By default, the data is returned from the normal period of 1991 - 2020. There is available the following normal periods: 1971 - 2000, 1981 - 2010, 1991 - 2020. Notice that there is only data at the begin of the period. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned in multi point coverage format.

* Query ID: `fmi::observations::weather::yearly::30year::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default all parameters will be returned.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Hanko).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Yearly weather observations of 30-year normal period

Yearly Weather Observations of 30-year normal period. By default, the data is returned from the normal period of 1991 - 2020. There is available the following normal periods: 1971 - 2000, 1981 - 2010, 1991 - 2020. Notice that there is only data at the begin of the period. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned in simple feature format.

* Query ID: `fmi::observations::weather::yearly::30year::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default all parameters will be returned.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Hanko).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Yearly weather observations of 30-year normal period

Yearly Weather Observations of 30-year normal period. By default, the data is returned from the normal period of 1991 - 2020. There is available the following normal periods: 1971 - 2000, 1981 - 2010, 1991 - 2020. Notice that there is only data at the begin of the period. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned in time value pair format.

* Query ID: `fmi::observations::weather::yearly::30year::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default all parameters will be returned.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Hanko).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latlon
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Radar

All available radar images during last hour.

* Query ID: `fmi::radar`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat,srs). For example 21,61,22,62,epsg::4326


## Radar Reflectivity Composite

Radar reflectivity (dbz) as composite covering Finland.

* Query ID: `fmi::radar::composite::dbz`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat,srs). For example 21,61,22,62,epsg::4326


## Precipitation Rate Composite

Precipitation rate (rr) as composite covering Finland.

* Query ID: `fmi::radar::composite::rr`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat,srs). For example 21,61,22,62,epsg::4326


## Precipitation Amount 12h Composite

Precipitation amount of twelve hours (rr12h) as composite covering Finland.

* Query ID: `fmi::radar::composite::rr12h`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat,srs). For example 21,61,22,62,epsg::4326


## Precipitation Amount 1h Composite

Precipitation amount of one hour (rr1h) as composite covering Finland.

* Query ID: `fmi::radar::composite::rr1h`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat,srs). For example 21,61,22,62,epsg::4326


## Precipitation Amount 24h Composite

Precipitation amount of 24 hours (rr24h) as composite covering Finland.

* Query ID: `fmi::radar::composite::rr24h`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat,srs). For example 21,61,22,62,epsg::4326


## Radar Reflectivity Single

Radar reflectivity (dbz) from single radars.

* Query ID: `fmi::radar::single::dbz`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat,srs). For example 21,61,22,62,epsg::4326
    * elevation
        * Elevation
        * Elevation


## Echo Top Single

Echo top 20 (etop_20) from single radars.

* Query ID: `fmi::radar::single::etop_20`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat,srs). For example 21,61,22,62,epsg::4326


## Hydro Class Single

Hydro class (hclass) from single radars.

* Query ID: `fmi::radar::single::hclass`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat,srs). For example 21,61,22,62,epsg::4326


## Doppler Speed Single

Doppler speed (vrad) from single radars.

* Query ID: `fmi::radar::single::vrad`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat,srs). For example 21,61,22,62,epsg::4326


## Surface level Hilatar model deposition data

This Stored Query retrieve simulated surface level deposition of nitrogen and sulphur compounds in Scandinavia in units mg per m2 (S or N) in the selected time period. Data is available in NetCDF file format.

* Query ID: `fmi::transportmodel::hilatar::surface::scandinavia::grid`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter starttime specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * Parameter endtime specifies the end of time interval in ISO 8601 format (for example 2012-02-28T00:00:00Z).
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data. For example: 19.1,59.7,31.7,70.1 (minLon,minLat,maxLon,maxLat)


## Instantaneous Road Weather Observations

Real time road weather observations from road weather stations. By default, basic weather data is returned from last 20 minutes. At least one location parameter (geoid/place/fmisid/bbox) has to be given. The data is returned as a multi point coverage format.

* Query ID: `livi::observations::road::default::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62.
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Helsinki).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location (place/fmisid/geoid). By default, one location is returned.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)


## Instantaneous Road Weather Observations

Real time road weather observations from road weather stations. By default, basic weather data is returned from last 20 minutes. At least one location parameter (geoid/place/fmisid/bbox) has to be given. The data is returned as a simple feature format.

* Query ID: `livi::observations::road::default::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62.
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Helsinki).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location (place/fmisid/geoid). By default, one location is returned.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)


## Instantaneous Road Weather Observations

Real time road weather observations from road weather stations. By default, essential parameters are returned from last 20 minutes. At least one location parameter (geoid/place/fmisid/bbox) has to be given. The data is returned as a time value pair format.

* Query ID: `livi::observations::road::default::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62.
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Rovaniemi).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location (place/fmisid/geoid). By default, one location is returned.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Instantaneous Road Weather Observations

Real time road weather observations from road weather stations in Finland. By default, essential parameters are returned from last 20 minutes. The data is returned as a multi point coverage format.

* Query ID: `livi::observations::road::finland::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default, essential parameters are selected.


## Instantaneous Road Weather Observations

Real time road weather observations from road weather stations in Finland. By default, essential parameters are returned from last 20 minutes. The data is returned as a simple feature format.

* Query ID: `livi::observations::road::finland::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default, essential parameters are selected.


## Instantaneous Road Weather Observations

Real time road weather observations from road weather stations in Finland. By default, essential parameters are returned from last 20 minutes. The data is returned as a time value pair format.

* Query ID: `livi::observations::road::finland::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default, essential parameters are selected.
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Instantaneous Road Weather Observations

Real time road weather observations from road weather stations. By default, the data is returned from last 12 hours. At least one location parameter (geoid/place/fmisid/bbox) has to be given. The data is returned as a multi point coverage format.

* Query ID: `livi::observations::road::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default all available parameters are selected.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62.
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Utti).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location (place/fmisid/geoid). By default, one location is returned.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)


## Instantaneous Road Weather Observations

Real time road weather observations from road weather stations. By default, the data is returned from last 12 hours. At least one location parameter (geoid/place/fmisid/bbox) has to be given. The data is returned as a simple feature format.

* Query ID: `livi::observations::road::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default all available parameters are selected.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62.
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Utti).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location (place/fmisid/geoid). By default, one location is returned.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)


## Instantaneous Road Weather Observations

Real time road weather observations from road weather stations. By default, the data is returned from last 12 hours. At least one location parameter (geoid/place/fmisid/bbox) has to be given. The data is returned as a time value pair format.

* Query ID: `livi::observations::road::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default all available parameters are selected.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62.
    * place
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kokkola).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location (place/fmisid/geoid). By default, one location is returned.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Radioactivity in outdoor air

This stored query returns only the latest results of the measurement of the radioactivity samples collected by special equipment. At monitoring station samples are created by pumping high volumes of air through glass fibre filter. In Finland there are 8 monitoring stations. By default all the monitoring stations are selected and the latest results of measurements are search from the last 720 hours. The default values can be overwritten by using the time and location related input parameters.

* Query ID: `stuk::observations::air::radionuclide-activity-concentration::latest::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2015-04-20T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2015-04-21T00:00:00Z).
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 27,64,28,65
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Savilahti,Kuopio).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067


## Radioactivity in outdoor air

This stored query return only the latest results of measurement of radioactivity samples collected by special equipment that filtering outdoor air in the monitoring stations in Finland. By default all the monitoring stations are selected and the latest results of measurements are search from the last 720 hours. The default values can be overwritten by using the time and location related input parameters. Notice that a result member contains the coordinates of a monitoring station, the endtime of sample collection period, a nuclide code and measured activity concentration.

* Query ID: `stuk::observations::air::radionuclide-activity-concentration::latest::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2015-04-20T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2015-04-21T00:00:00Z).
    * nuclides
        * Radionuclides to return
        * Comma separated list of radionuclides to return from the latest analyses (for example Cs-137,Pb-210)
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 27,64,28,65
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Savilahti,Kuopio).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067


## Radioactivity in outdoor air

This stored query returns the results of the measurement of the radioactivity samples collected by special equipment. At monitoring station samples are created by pumping high volumes of air through glass fibre filter. In Finland there are 8 monitoring stations. By default all the monitoring stations are selected and the results of measurements are search from the last 720 hours. The default values can be overwritten by using the time and location related input parameters.

* Query ID: `stuk::observations::air::radionuclide-activity-concentration::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2015-04-20T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2015-04-21T00:00:00Z).
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 27,64,28,65
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Savilahti,Kuopio).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067


## Latest dose rate of external radiation in Finland

This stored query return the latest results of the external dose rate measured by the automatic dose rate monitoring stations in Finland. The automatic dose rate monitoring network have about 255 monitoring stations distributed evenly around the Finland.  The monitoring network is maintained by Radiation and Nuclear Safety Authority (STUK). By default, the latest data is searched from the last 24 hours. The data is returned as a multipointcoverage format. The default values can be overwritten by using the time and location related input parameters.

* Query ID: `stuk::observations::external-radiation::latest::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067


## Latest dose rate of external radiation in Finland

This stored query return the latest dose rate of external radiation in Finland. The dose rate of external radiation is measured by an automatic external-dose rate-monitoring network maintained by Radiation and Nuclear Safety Authority (STUK) and local rescue services. The network comprises about 255 stations. By default, the latest data is searched from the last 24 hours. The data is returned as a simple format.

* Query ID: `stuk::observations::external-radiation::latest::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * parameters
        * Parameters to return
        * Comma separated list of parameters to return.
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067


## Dose rate of external radiation in Finland

This stored query return the results of the external dose rate measured by the automatic dose rate monitoring stations in Finland. The automatic dose rate monitoring network have about 255 monitoring stations distributed evenly around the Finland.  The monitoring network is maintained by Radiation and Nuclear Safety Authority (STUK). By default, the data is returned from the last 2 hours. The data is returned as a multipointcoverage format. The default values can be overwritten by using the time and location related input parameters.

* Query ID: `stuk::observations::external-radiation::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067


## Hourly Air Quality Observations

Hourly air quality observations from Finnish municipalities. By default, all the station are selected and the data is returned from the last 24 hours. The data is returned as multi point coverage format.

* Query ID: `urban::observations::airquality::hourly::multipointcoverage`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2015-03-13T10:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2015-03-13T12:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 24,60,25,61
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Helsinki).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)


## Hourly Air Quality Observations

Hourly air quality observations from Finnish municipalities. By default, all the station are selected and the data is returned from the last 24 hours. The data is returned as a simple feature format.

* Query ID: `urban::observations::airquality::hourly::simple`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2015-03-13T10:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2015-03-13T12:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 24,60,25,61
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Helsinki).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around a location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Hourly Air Quality Observations

Hourly air quality observations from Finnish municipalities. By default, all the station are selected and the data is returned from the last 24 hours. The data is returned as timevaluepair format.

* Query ID: `urban::observations::airquality::hourly::timevaluepair`
* Available arguments:
    * starttime
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2015-03-13T10:00:00Z).
    * endtime
        * End of time interval
        * End of time interval in ISO-format (for example 2015-03-13T12:00:00Z).
    * timestep
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters
        * Parameters to return
        * Comma separated list of parameters to return.
    * crs
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 24,60,25,61
    * place
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Helsinki).
    * fmisid
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around a location.
    * geoid
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * timezone
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


