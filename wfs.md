# Available WFS stored queries in FMI open data.

## ECMWF Pressure Grid

ECMWF forecast model's pressure levels as a grid data encoded in GRIB format.

* Query ID: `ecmwf::forecast::pressure::grid`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * levels (gml:integerList)
        * Pressure levels
        * A comma separated list of pressure levels (For example 1000,925,850).
    * format (xsi:string)
        * Dataset format.
        * Encoding format for the returned dataset. Formats available are grib1, grib2 and netcdf. Default format is grib2.


## ECMWF weather forecast for cities in Finland as multipointcoverage

This stored query fetch ECMWF weather forecast for cities in Finland. The forcast is returned in multi point coverage format. By default, forcast is returned for the next 36 hours.

* Query ID: `ecmwf::forecast::surface::cities::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of time interval
        * The parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * The parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067


## ECMWF weather forecast for cities in Finland as simple features

This stored query fetch ECMWF weather forecast for cities in Finland. The forcast is returned in simple feature format. By default, forcast is returned for the next 36 hours.

* Query ID: `ecmwf::forecast::surface::cities::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of time interval
        * The Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * The Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067


## ECMWF weather forecast for cities in Finland as time value pairs

This stored query fetch ECMWF weather forecast for cities in Finland. The forcast is returned as time value pairs. By default, forcast is returned for the next 36 hours.

* Query ID: `ecmwf::forecast::surface::cities::timevaluepair`
* Available arguments:
    * starttime (xsi:dateTime)
        * Begin of time interval
        * The parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (xsi:dateTime)
        * End of time interval
        * The parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * parameters (gml:NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default, all parameters are returned.
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day. Default timestep is 60 minutes.
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## ECMWF surface level weather forecast for Finland as a grid.

This Stored Query request retrieve ECMWF surface level forecast raw dataset as a grid for Finland region.

* Query ID: `ecmwf::forecast::surface::finland::grid`
* Available arguments:
    * producer (xsi:string)
        * Producer
        * Model or process which provides the data.
    * starttime (xsi:dateTime)
        * Begin of the time interval
        * Parameter starttime specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (xsi:dateTime)
        * End of time interval
        * Parameter endtime specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * parameters (gml:NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return. Default parameters are Temperature, Pressure, Humidity, DewPoint, WindUMS, WindVMS and Precipitation1h.
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (min Longitude, min Latitude, max Longitude, max Latitude) Default bounding box is 19.1,59.7,31.7,70.1.
    * format (xsi:string)
        * Dataset format.
        * Encoding format for the returned dataset. Formats available are grib1, grib2 and netcdf. Default format is General Regularly-distributed Information in Binary form edition 2 (GRIB2).


## ECMWF Surface Grid

ECMWF forecast model's surface level as grid data encoded in GRIB format.

* Query ID: `ecmwf::forecast::surface::grid`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
		In addition to default parameters, there is 'RadiationDiffuseAccumulation'
		parameter that is not distributed in grib2 format.
		Default: GeopHeight,Temperature,Pressure,Humidity,WindUMS,WindVMS,MaximumWind,
		WindGust,DewPoint,TotalCloudCover,LowCloudCover,MediumCloudCover,HighCloudCover,
		Precipitation1h,PrecipitationAmount,RadiationGlobalAccumulation,RadiationLWAccumulation,
		RadiationNetSurfaceLWAccumulation,RadiationNetSurfaceSWAccumulation,LandSeaMask,
		WindSpeedMS,WindDirection,Cape
    * format (xsi:string)
        * Dataset format.
        * Encoding format for the returned dataset. Formats available are grib1, grib2 and netcdf. Default format is General Regularly-distributed Information in Binary form edition 2 (GRIB2).


## ECMWF weather forecast for observation stations as multipointcoverage.

This stored query fetch ECMWF weather forecast for observation stations in Finland. The forcast is returned as multipointcoverage form. By default, forecast is returned for the next 36 hours.

* Query ID: `ecmwf::forecast::surface::obsstations::multipointcoverage`
* Available arguments:
    * starttime (xsi:dateTime)
        * Begin of the time interval
        * Parameter starttime specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (xsi:dateTime)
        * End of time interval
        * Parameter endtime specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * parameters (gml:NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default, all parameters are returned.
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day. Default timestep is 60 minutes.


## ECMWF weather forecast for observation stations as simple feature.

This stored query fetch ECMWF weather forecast for observation stations in Finland. The forcast is returned as simple feature form. By default, forecast is returned for the next 36 hours.

* Query ID: `ecmwf::forecast::surface::obsstations::simple`
* Available arguments:
    * starttime (xsi:dateTime)
        * Begin of the time interval
        * Parameter starttime specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (xsi:dateTime)
        * End of time interval
        * Parameter endtime specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * parameters (gml:NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default, all parameters are returned.
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day. Default timestep is 60 minutes.


## ECMWF weather forecast for observation stations as time value pairs.

This stored query fetch ECMWF weather forecast for observation stations in Finland. The forcast is returned as time value pairs. By default, forecast is returned for the next 36 hours.

* Query ID: `ecmwf::forecast::surface::obsstations::timevaluepair`
* Available arguments:
    * starttime (xsi:dateTime)
        * Begin of the time interval
        * Parameter starttime specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (xsi:dateTime)
        * End of time interval
        * Parameter endtime specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * parameters (gml:NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default, all parameters are returned.
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day. Default timestep is 60 minutes.
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## ECMWF Point Weather Forecast as multipointcoverage

ECMWF weather forecast fetched to a specific location returned in multi point coverage format. Location need to be specified as place or geoid or latlon query parameters.

* Query ID: `ecmwf::forecast::surface::point::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## ECMWF Point Weather Forecast as simple features

ECMWF weather forecast fetched to a specific location returned in simple feature format. Location need to be specified as place or geoid or latlon query parameters.

* Query ID: `ecmwf::forecast::surface::point::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## ECMWF Point Weather Forecast as time value pairs

ECMWF weather forecast fetched to a specific location returned in time value pair format. Location need to be specified as place or geoid or latlon query parameters.

* Query ID: `ecmwf::forecast::surface::point::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Environmental Monitoring Networks

This stored query can be used to fetch the metadata of environmental monitoring networks of Finnish Meteorological Institute's and other data producers. The metadata contains information about network name, period of activity, responsible party and an short description.

* Query ID: `fmi::ef::networks`
* Available arguments:
    * networkid (xsi:int)
        * Network identifier
        * Identifier of the observation network.


## Environmental Monitoring Stations

This stored query can be used to fetch the metadata of environmental monitoring stations of Finnish Meteorological Institute's and other data producers. The metadata contains information about station name, location, period of activity and the networks for which station belongs to.

* Query ID: `fmi::ef::stations`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * networkid (xsi:int)
        * Network identifier
        * Identifier of the observation network.
    * fmisid (xsi:int)
        * Station identifier
        * Identifier of the observation station.


## Climate Scenarios

Mean temperature and precipitation amount scenarios for three periods of thirty years. The data contains 10x10km grid and is returned in GRIB format.

* Query ID: `fmi::forecast::climatology::scenario::grid`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.


## Edited Scandinavia Weather Forecast Grid

Edited Scandinavia forecast as grid data encoded in GRIB format.

* Query ID: `fmi::forecast::edited::weather::scandinavia::grid`
* Available arguments:
    * origintime (dateTime)
        * Analysis time
        * Analysis time specifies the time of analysis in ISO-format (for example 2012-02-27T00:00:00Z).
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * format (xsi:string)
        * Dataset format.
        * Encoding format for the returned dataset. Formats available are grib1, grib2 and netcdf. Default format is General Regularly-distributed Information in Binary form edition 2 (GRIB2).


## Edited Scandinavia Point Weather Forecast as multipointcoverage

Edited Scandinavia point weather forecast fetched to a specific location returned in multi point coverage format. Location need to be specified as place or geoid or latlon query parameters.

* Query ID: `fmi::forecast::edited::weather::scandinavia::point::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)


## Edited Scandinavia Point Weather Forecast as simple features

Edited Scandinavia point weather forecast fetched to a specific location returned in simple feature format. Location need to be specified as place or geoid or latlon query parameters.

* Query ID: `fmi::forecast::edited::weather::scandinavia::point::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)


## Edited Scandinavia Point Weather Forecast as time value pairs

Edited Scandinavia point weather forecast fetched to a specific location returned in time value pair format. Location need to be specified as place or geoid or latlon query parameters.

* Query ID: `fmi::forecast::edited::weather::scandinavia::point::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## FMI-ENFUSER air quality forecast as grid

FMI-ENFUSER (The Finnish Meteorological Institute's ENvironmental information FUsion SERvice) is a novel air quality model that combines dispersion modelling techniques, information fusion algorithms and statistical approaches. The operational modelling system provides both real-time and forecasted, high resolution information on the urban air quality. This stored query provides near real-time information on Helsinki metropolitan air quality with a resolution of ~20m for the hourly concentrations of PM2.5, PM10, NO2, O3 and Air Quality Index (in a scale of 1 to 5) as a grid. New dataset will come available once in an hour.

* Query ID: `fmi::forecast::enfuser::airquality::helsinki-metropolitan::grid`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter specifies the begin of time interval to return data in ISO 8601 format (for example 2017-01-25T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * Parameter specifies the end of time interval to return data in ISO 8601 format (for example 2017-01-25T00:00:00Z).
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.


## Harmonie Scandinavia Hybrid Weather Forecast as Grid data

The stored query can be used to fetch Harmonie hybrid weather forecast data encoded in GRIB or NetCDF format. The model data covers the geographical area of Scandinavia and hybrid levels from 65 (near the model topography) to 12 (highest available elevation). New forecast dataset will come available every 6 hours. By default all the parameters, levels and timesteps are selected.

* Query ID: `fmi::forecast::harmonie::hybrid::grid`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2017-07-07T07:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2017-07-07T07:00:00Z).
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * levels (gml:integerList)
        * Hybrid levels
        * A comma separated list of levels (For example 40,30,20). By default all available levels are selected.
    * format (xsi:string)
        * Dataset format.
        * Encoding format for the returned dataset. Formats available are grib1, grib2 and netcdf. Default format is grib2.


## Harmonie Hybrid Point Weather Forecast as multipointcoverage

The stored query can be used to fetch Harmonie hybrid weather forecast data in multi point coverage format. The model data covers the geographical area of Scandinavia and heights between 13 and 10000 meters from the model topography. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned from the height of 100 meters above the model topography and 50 hours from the request time.

* Query ID: `fmi::forecast::harmonie::hybrid::point::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * height (xsi:double)
        * Height from the topography of forecast model
        * The request parameter specifies height in meters from the topography of forecast model.


## Harmonie Hybrid Point Weather Forecast as simple features

The stored query can be used to fetch Harmonie hybrid weather forecast data in simple feature format. The model data covers the geographical area of Scandinavia and heights between 13 and 10000 meters from the model topography. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned from the height of 100 meters above the model topography and 50 hours from the request time.

* Query ID: `fmi::forecast::harmonie::hybrid::point::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * height (xsi:double)
        * Height from the topography of forecast model
        * The request parameter specifies height in meters from the topography of forecast model.


## Harmonie Hybrid Point Weather Forecast as time value pairs

The stored query can be used to fetch Harmonie hybrid weather forecast data in time value pair format. The model data covers the geographical area of Scandinavia and heights between 13 and 10000 meters from the model topography. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned from the height of 100 meters above the model topography and 50 hours from the request time.

* Query ID: `fmi::forecast::harmonie::hybrid::point::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * height (xsi:double)
        * Height from the topography of forecast model
        * The request parameter specifies height in meters from the topography of forecast model.


## Harmonie Scandinavia Pressure Level Weather Forecast as Grid data

The stored query can be used to fetch Harmonie weather forecast data from pressure levels encoded in GRIB or NetCDF format. The model data covers the geographical area of Scandinavia and pressure levels: 300, 500, 700, 850, 925, 1000 hPa. New forecast dataset will come available every 6 hours. By default all the parameters, levels and timesteps are selected.

* Query ID: `fmi::forecast::harmonie::pressure::grid`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2017-07-07T07:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2017-07-07T07:00:00Z).
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * levels (gml:integerList)
        * Pressure levels
        * A comma separated list of pressure levels (For example 400,850,1000). By default all available levels are selected.
    * format (xsi:string)
        * Dataset format.
        * Encoding format for the returned dataset. Formats available are grib1, grib2 and netcdf. Default format is grib2.


## Harmonie Pressure Point Weather Forecast as multipointcoverage

The stored query can be used to fetch Harmonie pressure level weather forecast data in multi point coverage format. The model data covers the geographical area of Scandinavia and pressure levels 300, 500, 700, 850, 925, 1000 hPa. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned from the level of 850 hPa and 50 hours from the request time.

* Query ID: `fmi::forecast::harmonie::pressure::point::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * pressure (xsi:int)
        * Pressure value
        * The request parameter specifies level of pressure in hPa from which to return data.


## Harmonie Pressure Point Weather Forecast as simple features

The stored query can be used to fetch Harmonie pressure level weather forecast data in simple feature format. The model data covers the geographical area of Scandinavia and pressure levels 300, 500, 700, 850, 925, 1000 hPa. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned from the level of 850 hPa and 50 hours from the request time.

* Query ID: `fmi::forecast::harmonie::pressure::point::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * pressure (xsi:int)
        * Pressure value
        * The request parameter specifies level of pressure in hPa from which to return data.


## Harmonie Pressure Point Weather Forecast as time value pairs

The stored query can be used to fetch Harmonie pressure level weather forecast data in time value pair format. The model data covers the geographical area of Scandinavia and pressure levels 300, 500, 700, 850, 925, 1000 hPa. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned from the level of 850 hPa and 50 hours from the request time.

* Query ID: `fmi::forecast::harmonie::pressure::point::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * pressure (xsi:int)
        * Pressure value
        * The request parameter specifies level of pressure in hPa from which to return data.


## Harmonie Scandinavia Surface Level Weather Forecast as Grid data

The stored query can be used to fetch Harmonie surface level weather forecast data encoded in GRIB or NetCDF format. The model data covers the geographical area of Scandinavia. New forecast dataset will come available every 6 hours. By default all the parameters and timesteps are selected.

* Query ID: `fmi::forecast::harmonie::surface::grid`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2017-07-07T07:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2017-07-07T07:00:00Z).
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
		Default: Pressure,GeopHeight,Temperature,DewPoint,Humidity,WindDirection,
		WindSpeedMS,WindUMS,WindVMS,PrecipitationAmount,TotalCloudCover,LowCloudCover,
		MediumCloudCover,HighCloudCover,RadiationGlobal,RadiationGlobalAccumulation,
		RadiationNetSurfaceLWAccumulation,RadiationNetSurfaceSWAccumulation,
		RadiationSWAccumulation,Visibility,WindGust,Cape
    * format (xsi:string)
        * Dataset format.
        * Encoding format for the returned dataset. Formats available are grib2 and netcdf. Default format is grib2.


## Harmonie Surface Point Weather Forecast as multipointcoverage

The stored query can be used to fetch Harmonie surface level weather forecast in multi point coverage format. The model data covers the geographical area of Scandinavia. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned 50 hours from the request time.

* Query ID: `fmi::forecast::harmonie::surface::point::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Harmonie Surface Point Weather Forecast as simple features

The stored query can be used to fetch Harmonie surface level weather forecast in simple feature format. The model data covers the geographical area of Scandinavia. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned 50 hours from the request time.

* Query ID: `fmi::forecast::harmonie::surface::point::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Harmonie Surface Point Weather Forecast as time value pairs

The stored query can be used to fetch Harmonie surface level weather forecast in time value pair format. The model data covers the geographical area of Scandinavia. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned 50 hours from the request time.

* Query ID: `fmi::forecast::harmonie::surface::point::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Hydrodynamic Current Model Grid

Hydrodynamic forecast model provides sea currents and water temperature forecast as grid data encoded in GRIB format.

* Query ID: `fmi::forecast::hydrodyn::grid`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * format (xsi:string)
        * Dataset format.
        * Encoding format for the returned dataset. Formats available are grib1, grib2 and netcdf. Default format is grib2.
    * levels (gml:integerList)
        * Vertical level
        * A comma separated list of vertical levels of sea (For exmaple 0,100,200). Available levels are 0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,150,200,300,400. Default level is 0.


## Hydrodynamic Current Model Point

Hydrodynamic forecast model provides sea currents and water temperature forecast. This stored query provides the data as point data encoded in multi point coverage format.

* Query ID: `fmi::forecast::hydrodyn::point::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Hydrodynamic Current Model Point

Hydrodynamic forecast model provides sea currents and water temperature forecast. This stored query provides the data as point data encoded in simple feature format.

* Query ID: `fmi::forecast::hydrodyn::point::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Hydrodynamic Current Model Point

Hydrodynamic forecast model provides sea currents and water temperature forecast. This stored query provides the data as point data encoded in time value pair format.

* Query ID: `fmi::forecast::hydrodyn::point::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Harmonie (MEPS) Scandinavia Hybrid Weather Forecast as Grid data

The stored query can be used to fetch Harmonie (MEPS) hybrid weather forecast data encoded in GRIB or NetCDF format. The model data covers the geographical area of Scandinavia and hybrid levels from 65 (near the model topography) to 12 (highest available elevation). New forecast dataset will come available every 6 hours. By default all the parameters, levels and timesteps are selected.

* Query ID: `fmi::forecast::meps::hybrid::grid`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2017-07-07T07:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2017-07-07T07:00:00Z).
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * levels (gml:integerList)
        * Hybrid levels
        * A comma separated list of levels (For example 40,30,20). By default all available levels are selected.
    * format (xsi:string)
        * Dataset format.
        * Encoding format for the returned dataset. Formats available are grib1, grib2 and netcdf. Default format is grib2.


## Harmonie (MEPS) Hybrid Point Weather Forecast as multipointcoverage

The stored query can be used to fetch Harmonie (MEPS) hybrid weather forecast data in multi point coverage format. The model data covers the geographical area of Scandinavia and heights between 13 and 10000 meters from the model topography. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned from the height of 100 meters above the model topography and 50 hours from the request time.

* Query ID: `fmi::forecast::meps::hybrid::point::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * height (xsi:double)
        * Height from the topography of forecast model
        * The request parameter specifies height in meters from the topography of forecast model.


## Harmonie (MEPS) Hybrid Point Weather Forecast as simple features

The stored query can be used to fetch Harmonie (MEPS) hybrid weather forecast data in simple feature format. The model data covers the geographical area of Scandinavia and heights between 13 and 10000 meters from the model topography. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned from the height of 100 meters above the model topography and 50 hours from the request time.

* Query ID: `fmi::forecast::meps::hybrid::point::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * height (xsi:double)
        * Height from the topography of forecast model
        * The request parameter specifies height in meters from the topography of forecast model.


## Harmonie (MEPS) Hybrid Point Weather Forecast as time value pairs

The stored query can be used to fetch Harmonie (MEPS) hybrid weather forecast data in time value pair format. The model data covers the geographical area of Scandinavia and heights between 13 and 10000 meters from the model topography. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned from the height of 100 meters above the model topography and 50 hours from the request time.

* Query ID: `fmi::forecast::meps::hybrid::point::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * height (xsi:double)
        * Height from the topography of forecast model
        * The request parameter specifies height in meters from the topography of forecast model.


## Harmonie (MEPS) Scandinavia Pressure Level Weather Forecast as Grid data

The stored query can be used to fetch Harmonie (MEPS) weather forecast data from pressure levels encoded in GRIB or NetCDF format. The model data covers the geographical area of Scandinavia and pressure levels: 300, 500, 700, 850, 925, 1000 hPa. New forecast dataset will come available every 6 hours. By default all the parameters, levels and timesteps are selected.

* Query ID: `fmi::forecast::meps::pressure::grid`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2017-07-07T07:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2017-07-07T07:00:00Z).
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * levels (gml:integerList)
        * Pressure levels
        * A comma separated list of pressure levels (For example 400,850,1000). By default all available levels are selected.
    * format (xsi:string)
        * Dataset format.
        * Encoding format for the returned dataset. Formats available are grib1, grib2 and netcdf. Default format is grib2.


## Harmonie (MEPS) Pressure Point Weather Forecast as multipointcoverage

The stored query can be used to fetch Harmonie (MEPS) pressure level weather forecast data in multi point coverage format. The model data covers the geographical area of Scandinavia and pressure levels 300, 500, 700, 850, 925, 1000 hPa. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned from the level of 850 hPa and 50 hours from the request time.

* Query ID: `fmi::forecast::meps::pressure::point::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * pressure (xsi:int)
        * Pressure value
        * The request parameter specifies level of pressure in hPa from which to return data.


## Harmonie (MEPS) Pressure Point Weather Forecast as simple features

The stored query can be used to fetch Harmonie (MEPS) pressure level weather forecast data in simple feature format. The model data covers the geographical area of Scandinavia and pressure levels 300, 500, 700, 850, 925, 1000 hPa. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned from the level of 850 hPa and 50 hours from the request time.

* Query ID: `fmi::forecast::meps::pressure::point::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * pressure (xsi:int)
        * Pressure value
        * The request parameter specifies level of pressure in hPa from which to return data.


## Harmonie (MEPS) Pressure Point Weather Forecast as time value pairs

The stored query can be used to fetch Harmonie (MEPS) pressure level weather forecast data in time value pair format. The model data covers the geographical area of Scandinavia and pressure levels 300, 500, 700, 850, 925, 1000 hPa. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned from the level of 850 hPa and 50 hours from the request time.

* Query ID: `fmi::forecast::meps::pressure::point::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * pressure (xsi:int)
        * Pressure value
        * The request parameter specifies level of pressure in hPa from which to return data.


## Harmonie (MEPS) Scandinavia Surface Level Weather Forecast as Grid data

The stored query can be used to fetch Harmonie (MEPS) surface level weather forecast data encoded in GRIB or NetCDF format. The model data covers the geographical area of Scandinavia. New forecast dataset will come available every 6 hours. By default all the parameters and timesteps are selected.

* Query ID: `fmi::forecast::meps::surface::grid`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2017-07-07T07:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2017-07-07T07:00:00Z).
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
		Default: Pressure,GeopHeight,Temperature,DewPoint,Humidity,WindDirection,
		WindSpeedMS,WindUMS,WindVMS,PrecipitationAmount,TotalCloudCover,LowCloudCover,
		MediumCloudCover,HighCloudCover,RadiationGlobal,RadiationGlobalAccumulation,
		RadiationNetSurfaceLWAccumulation,RadiationNetSurfaceSWAccumulation,
		RadiationSWAccumulation,Visibility,WindGust,Cape
    * format (xsi:string)
        * Dataset format.
        * Encoding format for the returned dataset. Formats available are grib2 and netcdf. Default format is grib2.


## Harmonie (MEPS) Surface Point Weather Forecast as multipointcoverage

The stored query can be used to fetch Harmonie (MEPS) surface level weather forecast in multi point coverage format. The model data covers the geographical area of Scandinavia. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned 50 hours from the request time.

* Query ID: `fmi::forecast::meps::surface::point::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Harmonie (MEPS) Surface Point Weather Forecast as simple features

The stored query can be used to fetch Harmonie (MEPS) surface level weather forecast in simple feature format. The model data covers the geographical area of Scandinavia. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned 50 hours from the request time.

* Query ID: `fmi::forecast::meps::surface::point::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Harmonie (MEPS) Surface Point Weather Forecast as time value pairs

The stored query can be used to fetch Harmonie (MEPS) surface level weather forecast in time value pair format. The model data covers the geographical area of Scandinavia. New forecast dataset will come available every 6 hours. Location need to be specified as place or geoid or latlon query parameters. By default data will be returned 50 hours from the request time.

* Query ID: `fmi::forecast::meps::surface::point::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of time interval
        * Parameter specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * Parameter specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Sea Level Model Point

The forecast model provides sea level height forecast to points. This stored query provides point data encoded in multi point coverage format.

* Query ID: `fmi::forecast::sealevel::point::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21


## Sea Level Model Point

The forecast model provides a sea level height forecast to points. This stored query provides point data encoded in simple feature format.

* Query ID: `fmi::forecast::sealevel::point::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Sea Level Model Point

The forecast model provides sea level height forecast to points. This stored query provides point data encoded in time value pair format.

* Query ID: `fmi::forecast::sealevel::point::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## SILAM air quality forecast as grid

SILAM (System for Integrated modeLling of Atmospheric coMposition) is a global-to-meso-scale dispersion model developed for atmospheric composition, air quality, and emergency decision support applications. This stored query provides an air quality forecast for the main ambient pollutants: CO, NO, NO2, O3, SO2, PM10 and PM25. The model data covers the geographical area of Europe. New forecast dataset will come available once in a day. The data is returened as a grid. Output file format is NetCDF.

* Query ID: `fmi::forecast::silam::airquality::surface::grid`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO 8601 format (for example 2017-01-25T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO 8601 format (for example 2017-01-25T00:00:00Z).
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.


## SILAM air quality forecast as point data

SILAM (System for Integrated modeLling of Atmospheric coMposition) is a global-to-meso-scale dispersion model developed for atmospheric composition, air quality, and emergency decision support applications. This stored query provides an air quality forecast for the main ambient pollutants: CO, NO, NO2, O3, SO2, PM10 and PM25. The model data covers the geographical area of Europe. New forecast dataset will come available once in a day. The data is returened in multi point coverage format.

* Query ID: `fmi::forecast::silam::airquality::surface::point::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO 8601 format (for example 2017-01-25T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO 8601 format (for example 2017-01-25T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of air quality parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example http://www.opengis.net/def/crs/EPSG/0/4326
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## SILAM air quality forecast as simple feature

SILAM (System for Integrated modeLling of Atmospheric coMposition) is a global-to-meso-scale dispersion model developed for atmospheric composition, air quality, and emergency decision support applications. This stored query provides an air quality forecast for the main ambient pollutants: CO, NO, NO2, O3, SO2, PM10 and PM25. The model data covers the geographical area of Europe. New forecast dataset will come available once in a day. The data is returened as simple features.

* Query ID: `fmi::forecast::silam::airquality::surface::point::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO 8601 format (for example 2017-01-25T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO 8601 format (for example 2017-01-25T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of air quality parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example http://www.opengis.net/def/crs/EPSG/0/4326
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## SILAM air quality forecast as as time value pairs

SILAM (System for Integrated modeLling of Atmospheric coMposition) is a global-to-meso-scale dispersion model developed for atmospheric composition, air quality, and emergency decision support applications. This stored query provides an air quality forecast for the main ambient pollutants: CO, NO, NO2, O3, SO2, PM10 and PM25. The model data covers the geographical area of Europe. New forecast dataset will come available once in a day. The data is returened as as time value pairs.

* Query ID: `fmi::forecast::silam::airquality::surface::point::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO 8601 format (for example 2017-01-25T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO 8601 format (for example 2017-01-25T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of air quality parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example http://www.opengis.net/def/crs/EPSG/0/4326
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## WAM Wave Model Grid

WAM forecast model provides wave height forecast as grid data encoded in GRIB format.

* Query ID: `fmi::forecast::wam::grid`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.


## WAM Wave Model Point

WAM forecast model provides wave height forecast. This stored query provides point data encoded in multi point coverage format.

* Query ID: `fmi::forecast::wam::point::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latlon (gml:point)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21


## WAM Wave Model Point

WAM forecast model provides wave height forecast. This stored query provides point data encoded in simple feature format.

* Query ID: `fmi::forecast::wam::point::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latlon (gml:point)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21


## WAM Wave Model Point

WAM forecast model provides wave height forecast. This stored query provides point data encoded in time value pair format. Location has to be specified as geoid or latlon-coordinates.

* Query ID: `fmi::forecast::wam::point::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Hourly Air Quality Observations

Hourly air quality observations from weather stations of Finnish Meteorological Institute. By default, all the station are selected and the data is returned from the last 24 hours. The data is returned as multi point coverage format.

* Query ID: `fmi::observations::airquality::hourly::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2015-03-13T10:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2015-03-13T12:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 24,60,25,61
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Helsinki).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)


## Hourly Air Quality Observations

Hourly air quality observations from weather stations or Finnish Meteorological Institute. By default, all the station are selected and the data is returned from the last 24 hours. The data is returned as a simple feature format.

* Query ID: `fmi::observations::airquality::hourly::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2015-03-13T10:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2015-03-13T12:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 24,60,25,61
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Helsinki).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around a location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Hourly Air Quality Observations

Hourly air quality observations from weather stations of Finnish Meteorological Institute. By default, all the station are selected and the data is returned from the last 24 hours. The data is returned as timevaluepair format.

* Query ID: `fmi::observations::airquality::hourly::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2015-03-13T10:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2015-03-13T12:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 24,60,25,61
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Helsinki).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around a location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Salinity and Water temperature observations

Salinity and water temperature observations (CTD observations) from fixed locations. Available parameters are water temperature, salinity, conductivity, density, and the speed of sound as a function of water pressure (corresponding approximately to depth). The data is returned in multipointcoverage format.

* Query ID: `fmi::observations::ctd::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.


## Salinity and Water temperature observations

Salinity and water temperature observations (CTD observations) from fixed locations. Available parameters are water temperature, salinity, conductivity, density, and the speed of sound as a function of water pressure (corresponding approximately to depth). The data is returned in a time value pair format.

* Query ID: `fmi::observations::ctd::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Lightning Strikes

The response contains all detected lightning strikes in Northern Europe. Observations are mainly ground flashes but some of cloud flashes are also detected.

* Query ID: `fmi::observations::lightning::multipointcoverage`
* Available arguments:
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).


## Lightning Strikes

The response contains all detected lightning strikes in Northern Europe. Observations are mainly ground flashes but some of cloud flashes are also detected.

* Query ID: `fmi::observations::lightning::simple`
* Available arguments:
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).


## Magnetometer Observations

Magnetometer observations from 12 locations. The data is retuned in simple feature format.

* Query ID: `fmi::observations::magnetometer::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62.
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Utti).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (xsi:int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location (place/fmisid/geoid). By default, one location is returned.


## Mareograph Water Temperature Daily Statistical Values

Daily water temperature average, minimum and maximum from 14 locations. By default, the data is returned from last 744 hours. The data is retuned in multi point coverage format.

* Query ID: `fmi::observations::mareograph::daily::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.


## Mareograph Water Temperature Daily Statistical Values

Daily water temperature average, minimum and maximum from 14 locations. By default, the data is returned from last 744 hours. The data is retuned in simple feature format.

* Query ID: `fmi::observations::mareograph::daily::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.


## Mareograph Water Temperature Daily Statistical Values

Daily water temperature average, minimum and maximum from 14 locations. By default, the data is returned from last 744 hours. The data is retuned in time value pair format.

* Query ID: `fmi::observations::mareograph::daily::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.


## Sea Level and Temperature Observations

Sea level and temperature observations from 14 locations. Time step is 1 minute. The data is retuned in multi point coverage format.

* Query ID: `fmi::observations::mareograph::instant::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.


## Sea Level and Temperature Observations

Sea level and temperature observations from 14 locations. Time step is 1 minute. The data is retuned in simple feature format.

* Query ID: `fmi::observations::mareograph::instant::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.


## Sea Level and Temperature Observations

Sea level and temperature observations from 14 locations. Time step is 1 minute. The data is returned in time value pair format.

* Query ID: `fmi::observations::mareograph::instant::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Monthly water level and temperature observations of 30-year normal period.

Monthly water level and temperature observations of 30-year normal period 1991 - 2020. Notice that there is only data at the begin of each month of the first year of the period. By default data is returned from 15 locations. The data is returned in multipointcoverage format.

* Query ID: `fmi::observations::mareograph::monthly::30year::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default all parameters will be returned.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Hanko).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Monthly water level and temperature observations of 30-year normal period.

Monthly water level and temperature observations of 30-year normal period 1991 - 2020. Notice that there is only data at the begin of each month of the first year of the period. By default data is returned from 15 locations. The data is returned in simple feature format.

* Query ID: `fmi::observations::mareograph::monthly::30year::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default all parameters will be returned.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Hanko).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Monthly water level and temperature observations of 30-year normal period.

Monthly water level and temperature observations of 30-year normal period 1991 - 2020. Notice that there is only data at the begin of each month of the first year of the period. By default data is returned from 15 locations. The data is returned in timevaluepair format.

* Query ID: `fmi::observations::mareograph::monthly::30year::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default all parameters will be returned.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Hanko).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Mareograph Water Temperature Monthly Statistical Values

Monthly water temperature average, minimum and maximum from 14 locations. By default, the data is returned from last 12 months. The data is retuned in multi point coverage format.

* Query ID: `fmi::observations::mareograph::monthly::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.


## Mareograph Water Temperature Monthly Statistical Values

Monthly water temperature average, minimum and maximum from 14 locations. By default, the data is returned from last 12 months. The data is retuned in simple feature format.

* Query ID: `fmi::observations::mareograph::monthly::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.


## Mareograph Water Temperature Monthly Statistical Values

Monthly water temperature average, minimum and maximum from 14 locations. By default, the data is returned from last 12 months. The data is retuned in time value pair format.

* Query ID: `fmi::observations::mareograph::monthly::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.


## Sea Level and Temperature Observations

Sea level and temperature observations from 14 locations. Time step is 60 minutes. The data is retuned in multi point coverage format.

* Query ID: `fmi::observations::mareograph::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.


## Sea Level and Temperature Observations

Sea level and temperature observations from 14 locations. Time step is 60 minutes. The data is retuned in simple feature format.

* Query ID: `fmi::observations::mareograph::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.


## Sea Level and Temperature Observations

Sea level and temperature observations from 14 locations. Time step is 60 minutes. The data is returned in time value pair format.

* Query ID: `fmi::observations::mareograph::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Yearly water level observations of 30-year normal period.

Yearly water level observations of 30-year normal period 1991 - 2020. Notice that there is only data at the begin of the period. By default data is returned from 13 locations. The data is returned in multipointcoverage format.

* Query ID: `fmi::observations::mareograph::yearly::30year::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default all parameters will be returned.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Hanko).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Yearly water level observations of 30-year normal period.

Yearly water level observations of 30-year normal period 1991 - 2020. Notice that there is only data at the begin of the period. By default data is returned from 13 locations. The data is returned in simple feature format.

* Query ID: `fmi::observations::mareograph::yearly::30year::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default all parameters will be returned.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Hanko).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Yearly water level observations of 30-year normal period.

Yearly water level observations of 30-year normal period 1991 - 2020. Notice that there is only data at the begin of the period. By default data is returned from 13 locations. The data is returned in timevaluepair format.

* Query ID: `fmi::observations::mareograph::yearly::30year::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default all parameters will be returned.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Hanko).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Sun Radiation Observations

Sun radiation observations from weather stations. By default the data is returned from last 1 hour and from stations in Sodankylä, Jokioinen, Helsinki, Parainen, Vantaa, Jyväskylä, Sotkamo and Utsjoki. The data is returned in 'multipointcoverage' format.

* Query ID: `fmi::observations::radiation::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.


## Sun Radiation Observations

Sun radiation observations from weather stations. By default the data is returned from last 1 hour and from stations in Sodankylä, Jokioinen, Helsinki, Parainen, Vantaa, Jyväskylä, Sotkamo and Utsjoki. The data is returned in 'simple feature' format.

* Query ID: `fmi::observations::radiation::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.


## Sun Radiation Observations

Sun radiation observations from weather stations. By default the data is returned from last 1 hour and from stations in Sodankylä, Jokioinen, Helsinki, Parainen, Vantaa, Jyväskylä, Sotkamo and Utsjoki. The data is returned in 'timevaluepair' format.

* Query ID: `fmi::observations::radiation::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Manual Sea Ice Observations

Manually made sea ice observations from The Baltic Sea. By default, the data is returned from last 30 days.  At least one location parameter (geoid/place/fmisid/wmo/bbox/latlon) has to be given. The data is returned as a time value pair format.

* Query ID: `fmi::observations::seaice::manual::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 63.890,22.943
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Hourly Soil Observations

Hourly minimum, maximum and average soil values from weather stations. By default, the data is returned from last 12 hour.  At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned as multi point coverage format.

* Query ID: `fmi::observations::soil::hourly::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Salkola,Somero).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Hourly Soil Observations

Hourly minimum, maximum and average soil values from weather stations. By default, the data is returned from last 12 hour.  At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned as simple feature format.

* Query ID: `fmi::observations::soil::hourly::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Salkola,Somero).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Hourly Soil Observations

Hourly minimum, maximum and average soil values from weather stations. By default, the data is returned from last 12 hour.  At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned as a time value pair format.

* Query ID: `fmi::observations::soil::hourly::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Salkola,Somero).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Sea Surface Temperature Observations

Sea surface temperature observations from a range of measurements. Time step is variable and depends on the measurement point. The data is retuned in simple feature format.

* Query ID: `fmi::observations::surfacetemperature::daily::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.


## Sea Surface Temperature Observations

Sea surface temperature observations from a range of measurements. Time step is variable and depends on the measurement point. The data is retuned in simple feature format.

* Query ID: `fmi::observations::surfacetemperature::monthly::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.


## Sea Surface Temperature Observations

Sea surface temperature observations from a range of measurements. Time step is variable and depends on the measurement point. The data is retuned in simple feature format.

* Query ID: `fmi::observations::surfacetemperature::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.


## Buoy Water Temperature Daily Statistical Values

Daily water temperature average, minimum and maximum from buoys. By default, the data is returned from last 744 hours. The data is returned in multi point coverage format.

* Query ID: `fmi::observations::wave::daily::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.


## Buoy Water Temperature Daily Statistical Values

Daily water temperature average, minimum and maximum from buoys. By default, the data is returned from last 744 hours. The data is returned in simple feature format.

* Query ID: `fmi::observations::wave::daily::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.


## Buoy Water Temperature Daily Statistical Values

Daily water temperature average, minimum and maximum from buoys. By default, the data is returned from last 744 hours. The data is returned in time value pair format.

* Query ID: `fmi::observations::wave::daily::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.


## Buoy Water Temperature Monthly Statistical Values

Monthly water temperature average, minimum and maximum from buoys. By default, the data is returned from last 12 months. The data is returned in multi point coverage format.

* Query ID: `fmi::observations::wave::monthly::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.


## Buoy Water Temperature Monthly Statistical Values

Monthly water temperature average, minimum and maximum from buoys. By default, the data is returned from last 12 months. The data is returned in simple feature format.

* Query ID: `fmi::observations::wave::monthly::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.


## Buoy Water Temperature Monthly Statistical Values

Monthly water temperature average, minimum and maximum from buoys. By default, the data is returned from last 12 months. The data is returned in time value pair format.

* Query ID: `fmi::observations::wave::monthly::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.


## Wave and Water temperature observations

Wave and water temperature observations from buoys. Available parameters are significant wave height, wave direction, deviation of wave direction, modal period and water temperature. Some buoys return only temperature values. Time step is 30 minutes. The data is returned in multipointcoverage format.

* Query ID: `fmi::observations::wave::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.


## Wave and Water temperature observations

Wave and water temperature observations from buoys. Available parameters are significant wave height, wave direction, deviation of wave direction, modal period and water temperature. Some buoys return only temperature values. Time step is 30 minutes. The data is returned in simple feature format.

* Query ID: `fmi::observations::wave::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.


## Wave and Water temperature observations

Wave and water temperature observations from buoys. Available parameters are significant wave height, wave direction, deviation of wave direction, modal period and water temperature. Some buoys return only temperature values. Time step is 30 minutes. The data is returned in time value pair format.

* Query ID: `fmi::observations::wave::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Weather observations for cities as multipointcoverage.

Weather observations for cities in Finland as multipointcoverage.

* Query ID: `fmi::observations::weather::cities::multipointcoverage`
* Available arguments:
    * starttime (xsi:dateTime)
        * Begin of the time interval
        * Parameter starttime specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (xsi:dateTime)
        * End of time interval
        * Parameter endtime specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * parameters (gml:NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * timestep (xsi:unsignedInteger)
        * The time step in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.


## Weather observations for cities as simple feature.

Weather observations for cities in Finland as simple feature.

* Query ID: `fmi::observations::weather::cities::simple`
* Available arguments:
    * starttime (xsi:dateTime)
        * Begin of the time interval
        * Parameter starttime specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (xsi:dateTime)
        * End of time interval
        * Parameter endtime specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * parameters (gml:NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * timestep (xsi:unsignedInteger)
        * The time step in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.


## Weather observations for cities as time value pairs.

Weather observations for cities in Finland as time value pairs.

* Query ID: `fmi::observations::weather::cities::timevaluepair`
* Available arguments:
    * starttime (xsi:dateTime)
        * Begin of the time interval
        * Parameter starttime specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (xsi:dateTime)
        * End of time interval
        * Parameter endtime specifies the end of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * parameters (gml:NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * timestep (xsi:unsignedInteger)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Daily Weather Observations

Daily weather observations from weather stations. Default set contains daily precipitation rate, mean temperature, snow depth, and minimum  and maximum temperature. By default, the data is returned from last 744 hours. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned in multi point coverage format.

* Query ID: `fmi::observations::weather::daily::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Daily Weather Observations

Daily weather observations from weather stations. Default set contains daily precipitation rate, mean temperature, snow depth, and minimum  and maximum temperature. By default, the data is returned from last 744 hours. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned in simple feature format.

* Query ID: `fmi::observations::weather::daily::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Daily Weather Observations

Daily weather observations from weather stations. Default set contains daily precipitation rate, mean temperature, snow depth, minimum temperature and maximum temperature. By default, the data is returned from last 744 hours. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned time value pair format.

* Query ID: `fmi::observations::weather::daily::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Dropsonde observations

This stored query returns atmospheric dropsonde observations in multipointcoverage format. By default dropsonde observations are returned from the observation stations of Finland the last 12 hours.

* Query ID: `fmi::observations::weather::dropsonde::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2017-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2017-02-27T00:00:00Z).
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 23,60,24,61
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Jokioinen).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latest (boolean)
        * Return only latest measurements
        * If only latest mearurements are wanted to return for each station use value 'true' otherwise 'false'.
    * altituderange (gml:pos)
        * Altitude range
        * Altitude range to return data  (minAltitude,maxAltitude) in meters. For example 5000.0,10000.0.
    * pressurerange (gml:pos)
        * Pressure range
        * Pressure range to return data  (minPressure,maxPressure) in units of hPa. For example 800.0,850.0
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::7904


## Hourly Weather Observations

Hourly weather observations from weather stations. Default set contains hourly air temperature average, maximum and minimum, air relative humidity average, wind speed average, minumum (10 minute average) and maximum (10 minute average), wind direction average, wind gust speed maximum (3 second average), rain accumulated, rain intensity maximum, air pressure average and the most significant weather code. By default, the data is returned from last 24 hours. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned in multi point coverage format.

* Query ID: `fmi::observations::weather::hourly::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Hourly Weather Observations

Hourly weather observations from weather stations. Default set contains hourly air temperature average, maximum and minimum, air relative humidity average, wind speed average, minumum (10 minute average) and maximum (10 minute average), wind direction average, wind gust speed maximum (3 second average), rain accumulated, rain intensity maximum, air pressure average and the most significant weather code. By default, the data is returned from last 24 hours. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned in simple format.

* Query ID: `fmi::observations::weather::hourly::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Hourly Weather Observations

Hourly weather observations from weather stations. Default set contains hourly air temperature average, maximum and minimum, air relative humidity average, wind speed average, minumum (10 minute average) and maximum (10 minute average), wind direction average, wind gust speed maximum (3 second average), rain accumulated, rain intensity maximum, air pressure average and the most significant weather code. By default, the data is returned from last 24 hours. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned in time value pair format.

* Query ID: `fmi::observations::weather::hourly::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Instantaneous profile observations from masts

This stored query return instantaneous profile observations from masts in multipointcoverage format. By default latest observation of the available meteo paramters are returned in 10 minute resolution. At least one location has to be given.

* Query ID: `fmi::observations::weather::mast::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Espoo).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Monthly weather observations of 30-year normal period

Monthly Weather Observations of 30-year normal period. By default, the data is returned from the normal period of 1991 - 2020. There is available the following normal periods: 1971 - 2000, 1981 - 2010, 1991 - 2020. Notice that there is only data at the begin of the period. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned in multi point coverage format.

* Query ID: `fmi::observations::weather::monthly::30year::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default all parameters will be returned.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Hanko).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Monthly weather observations of 30-year normal period

Monthly Weather Observations of 30-year normal period. By default, the data is returned from the normal period of 1991 - 2020. There is available the following normal periods: 1971 - 2000, 1981 - 2010, 1991 - 2020. Notice that there is only data at the begin of the period. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned in simple feature format.

* Query ID: `fmi::observations::weather::monthly::30year::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default all parameters will be returned.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Hanko).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Monthly weather observations of 30-year normal period

Monthly Weather Observations of 30-year normal period. By default, the data is returned from the normal period of 1991 - 2020. There is available the following normal periods: 1971 - 2000, 1981 - 2010, 1991 - 2020. Notice that there is only data at the begin of the period. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned in time value pair format.

* Query ID: `fmi::observations::weather::monthly::30year::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default all parameters will be returned.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Hanko).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Monthly Weather Observations

Monthly precipitation rate and mean temperature interpolated into a grid. The data is returned in GRIB format.

* Query ID: `fmi::observations::weather::monthly::grid`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.


## Monthly Weather Observations

Monthly weather observations from weather stations. Default set contains monthly precipitation rate, mean temperature. By default, the data is returned from last 12 months. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned in multi point coverage format.

* Query ID: `fmi::observations::weather::monthly::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Monthly Weather Observations

Monthly weather observations from weather stations. Default set contains monthly precipitation rate, mean temperature. By default, the data is returned from last 12 months. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned in simple feature format.

* Query ID: `fmi::observations::weather::monthly::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Monthly Weather Observations

Monthly weather observations from weather stations. Default set contains monthly precipitation rate, mean temperature. By default, the data is returned from last 12 months. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned in time value pair format.

* Query ID: `fmi::observations::weather::monthly::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Instantaneous Weather Observations

Real time weather observations from weather stations. Default set contains wind speed, direction, gust, temperature, relative humidity, dew point, pressure reduced to sea level, one hour precipitation amount, visibility and cloud cover. By default, the data is returned from last 12 hour. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned as a multi point coverage format.

* Query ID: `fmi::observations::weather::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Instantaneous Weather Observations

Real time weather observations from weather stations. Default set contains wind speed, direction, gust, temperature, relative humidity, dew point, pressure reduced to sea level, one hour precipitation amount, visibility and cloud cover. By default, the data is returned from last 12 hour. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned as a simple feature format.

* Query ID: `fmi::observations::weather::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.


## Sounding observations

This stored query returns atmospheric sounding observations in multipointcoverage format. By default sounding observations are returned from the observation stations of Finland the last 12 hours.

* Query ID: `fmi::observations::weather::sounding::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2017-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2017-02-27T00:00:00Z).
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 23,60,24,61
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Jokioinen).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latest (boolean)
        * Return only latest soundings
        * If only latest soundings is wanted to return for each station use value 'true' otherwise 'false'.
    * altituderange (gml:pos)
        * Altitude range
        * Altitude range to return data  (minAltitude,maxAltitude) in meters. For example 5000.0,10000.0.
    * pressurerange (gml:pos)
        * Pressure range
        * Pressure range to return data  (minPressure,maxPressure) in units of hPa. For example 800.0,850.0
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::7904
    * soundingtype (int)
        * Sounding type
        * Sounding type


## Instantaneous Weather Observations

Real time weather observations from weather stations. Default set contains air temperatire, wind speed, gust speed, wind direction, relative humidity, dew point, one hour precipitation amount, precipitation intensity, snow depth, pressure reduced to sea level and visibility. By default, the data is returned from last 12 hour.  At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned as a time value pair format.

* Query ID: `fmi::observations::weather::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Yearly weather observations of 30-year normal period

Yearly Weather Observations of 30-year normal period. By default, the data is returned from the normal period of 1991 - 2020. There is available the following normal periods: 1971 - 2000, 1981 - 2010, 1991 - 2020. Notice that there is only data at the begin of the period. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned in multi point coverage format.

* Query ID: `fmi::observations::weather::yearly::30year::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default all parameters will be returned.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Hanko).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Yearly weather observations of 30-year normal period

Yearly Weather Observations of 30-year normal period. By default, the data is returned from the normal period of 1991 - 2020. There is available the following normal periods: 1971 - 2000, 1981 - 2010, 1991 - 2020. Notice that there is only data at the begin of the period. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned in simple feature format.

* Query ID: `fmi::observations::weather::yearly::30year::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default all parameters will be returned.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Hanko).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Yearly weather observations of 30-year normal period

Yearly Weather Observations of 30-year normal period. By default, the data is returned from the normal period of 1991 - 2020. There is available the following normal periods: 1971 - 2000, 1981 - 2010, 1991 - 2020. Notice that there is only data at the begin of the period. At least one location parameter (geoid/place/fmisid/wmo/bbox) has to be given. The data is returned in time value pair format.

* Query ID: `fmi::observations::weather::yearly::30year::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return. By default all parameters will be returned.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide forecast. Region can be given after location name separated by comma (for example Hanko).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * wmo (int)
        * WMO code of the location for which to return data.
        * WMO code of the location for which to return data.
    * latlon (gml:pos)
        * Location coordinates to return data.
        * Location coordinates to return data  (lat,lon). For example 61.2,21
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Radar

All available radar images during last hour.

* Query ID: `fmi::radar`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat,srs). For example 21,61,22,62,epsg::4326
* Calibration:
    * rr (Rain rate)
        * Calibrated unit: mm/h
        * Calibration: y = 0.01 * x + 0.0
    * dbz (Radar reflectivity)
        * Calibrated unit: dBZ
        * Calibration: y = 0.5 * x - 32.0
    * dbz (Radar reflectivity)
        * Calibrated unit: dBZ
    * vrad (Radial Doppler velocity)
        * Calibrated unit: m/s
        * Calibration: y = 0.251339 * x - 32.171337
    * vrad (Radial Doppler velocity)
        * Calibrated unit: m/s
        * Calibration: y = 0.314173 * x - 40.214172
    * vrad (Radial Doppler velocity)
        * Calibrated unit: m/s
        * Calibration: y = 0.252283 * x - 32.292282
    * vrad (Radial Doppler velocity)
        * Calibrated unit: m/s
        * Calibration: y = 0.315354 * x - 40.365353
    * vrad (Radial Doppler velocity)
        * Calibrated unit: m/s
        * Calibration: y = 0.252756 * x - 32.352757
    * vrad (Radial Doppler velocity)
        * Calibrated unit: m/s
        * Calibration: y = 0.315945 * x - 40.440945
    * vrad (Radial Doppler velocity)
        * Calibrated unit: m/s
        * Calibration: y = 0.251811 * x - 32.23181
    * vrad (Radial Doppler velocity)
        * Calibrated unit: m/s
        * Calibration: y = 0.314764 * x - 40.289764
    * vrad (Radial Doppler velocity)
        * Calibrated unit: m/s
    * hclass (HydroClass hydrometeor classification)
        * Calibrated unit: Index
        * Calibration: y = 1.0 * x + 0.0
    * hclass (HydroClass hydrometeor classification)
        * Calibrated unit: Index
    * etop (Echo top using 20dBZ threshold)
        * Calibrated unit: m
    * etop (Echo top using 20dBZ threshold)
        * Calibrated unit: m
        * Calibration: y = 0.1 * x - 0.1


## Radar Reflectivity Composite

Radar reflectivity (dbz) as composite covering Finland.

* Query ID: `fmi::radar::composite::dbz`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat,srs). For example 21,61,22,62,epsg::4326
* Calibration:
    * dbz (Radar reflectivity)
        * Calibrated unit: dBZ
        * Calibration: y = 0.5 * x - 32.0


## Precipitation Rate Composite

Precipitation rate (rr) as composite covering Finland.

* Query ID: `fmi::radar::composite::rr`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat,srs). For example 21,61,22,62,epsg::4326
* Calibration:
    * rr (Rain rate)
        * Calibrated unit: mm/h
        * Calibration: y = 0.01 * x + 0.0


## Precipitation Amount 12h Composite

Precipitation amount of twelve hours (rr12h) as composite covering Finland.

* Query ID: `fmi::radar::composite::rr12h`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat,srs). For example 21,61,22,62,epsg::4326
* Calibration:
    * rr12h (12 hour rain sum)
        * Calibrated unit: mm
        * Calibration: y = 0.01 * x + 0.0


## Precipitation Amount 1h Composite

Precipitation amount of one hour (rr1h) as composite covering Finland.

* Query ID: `fmi::radar::composite::rr1h`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat,srs). For example 21,61,22,62,epsg::4326
* Calibration:
    * rr1h (1 hour rain sum)
        * Calibrated unit: mm
        * Calibration: y = 0.01 * x + 0.0


## Precipitation Amount 24h Composite

Precipitation amount of 24 hours (rr24h) as composite covering Finland.

* Query ID: `fmi::radar::composite::rr24h`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat,srs). For example 21,61,22,62,epsg::4326
* Calibration:
    * rr24h (24 hour rain sum)
        * Calibrated unit: mm
        * Calibration: y = 0.01 * x + 0.0


## Radar Reflectivity Single

Radar reflectivity (dbz) from single radars.

* Query ID: `fmi::radar::single::dbz`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat,srs). For example 21,61,22,62,epsg::4326
    * elevation (string)
        * Elevation
        * Elevation
* Calibration:
    * dbz (Radar reflectivity)
        * Calibrated unit: dBZ
    * dbz (Radar reflectivity)
        * Calibrated unit: dBZ
        * Calibration: y = 0.5 * x - 32.0


## Echo Top Single

Echo top 20 (etop_20) from single radars.

* Query ID: `fmi::radar::single::etop_20`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat,srs). For example 21,61,22,62,epsg::4326
* Calibration:
    * etop (Echo top using 20dBZ threshold)
        * Calibrated unit: m
        * Calibration: y = 0.1 * x - 0.1
    * etop (Echo top using 20dBZ threshold)
        * Calibrated unit: m


## Hydro Class Single

Hydro class (hclass) from single radars.

* Query ID: `fmi::radar::single::hclass`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat,srs). For example 21,61,22,62,epsg::4326
* Calibration:
    * hclass (HydroClass hydrometeor classification)
        * Calibrated unit: Index
    * hclass (HydroClass hydrometeor classification)
        * Calibrated unit: Index
        * Calibration: y = 1.0 * x + 0.0


## Doppler Speed Single

Doppler speed (vrad) from single radars.

* Query ID: `fmi::radar::single::vrad`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat,srs). For example 21,61,22,62,epsg::4326
* Calibration:
    * vrad (Radial Doppler velocity)
        * Calibrated unit: m/s
        * Calibration: y = 0.314173 * x - 40.214172
    * vrad (Radial Doppler velocity)
        * Calibrated unit: m/s
        * Calibration: y = 0.251339 * x - 32.171337
    * vrad (Radial Doppler velocity)
        * Calibrated unit: m/s
        * Calibration: y = 0.315354 * x - 40.365353
    * vrad (Radial Doppler velocity)
        * Calibrated unit: m/s
        * Calibration: y = 0.252283 * x - 32.292282
    * vrad (Radial Doppler velocity)
        * Calibrated unit: m/s
        * Calibration: y = 0.315945 * x - 40.440945
    * vrad (Radial Doppler velocity)
        * Calibrated unit: m/s
        * Calibration: y = 0.252756 * x - 32.352757
    * vrad (Radial Doppler velocity)
        * Calibrated unit: m/s
        * Calibration: y = 0.314764 * x - 40.289764
    * vrad (Radial Doppler velocity)
        * Calibrated unit: m/s
        * Calibration: y = 0.251811 * x - 32.23181
    * vrad (Radial Doppler velocity)
        * Calibrated unit: m/s


## Surface level Hilatar model deposition data

This Stored Query retrieve simulated surface level deposition of nitrogen and sulphur compounds in Scandinavia in units mg per m2 (S or N) in the selected time period. Data is available in NetCDF file format.

* Query ID: `fmi::transportmodel::hilatar::surface::scandinavia::grid`
* Available arguments:
    * starttime (xsi:dateTime)
        * Begin of the time interval
        * Parameter starttime specifies the begin of time interval in ISO 8601 format (for example 2012-02-27T00:00:00Z).
    * endtime (xsi:dateTime)
        * End of time interval
        * Parameter endtime specifies the end of time interval in ISO 8601 format (for example 2012-02-28T00:00:00Z).
    * parameters (gml:NameList)
        * Parameters to return
        * Comma separated list of meteorological parameters to return.
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data. For example: 19.1,59.7,31.7,70.1 (minLon,minLat,maxLon,maxLat)


## Radioactivity in outdoor air

This stored query returns only the latest results of the measurement of the radioactivity samples collected by special equipment. At monitoring station samples are created by pumping high volumes of air through glass fibre filter. In Finland there are 8 monitoring stations. By default all the monitoring stations are selected and the latest results of measurements are search from the last 720 hours. The default values can be overwritten by using the time and location related input parameters.

* Query ID: `stuk::observations::air::radionuclide-activity-concentration::latest::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2015-04-20T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2015-04-21T00:00:00Z).
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 27,64,28,65
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Savilahti,Kuopio).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067


## Radioactivity in outdoor air

This stored query return only the latest results of measurement of radioactivity samples collected by special equipment that filtering outdoor air in the monitoring stations in Finland. By default all the monitoring stations are selected and the latest results of measurements are search from the last 720 hours. The default values can be overwritten by using the time and location related input parameters. Notice that a result member contains the coordinates of a monitoring station, the endtime of sample collection period, a nuclide code and measured activity concentration.

* Query ID: `stuk::observations::air::radionuclide-activity-concentration::latest::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2015-04-20T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2015-04-21T00:00:00Z).
    * nuclides (NameList)
        * Radionuclides to return
        * Comma separated list of radionuclides to return from the latest analyses (for example Cs-137,Pb-210)
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 27,64,28,65
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Savilahti,Kuopio).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067


## Radioactivity in outdoor air

This stored query returns the results of the measurement of the radioactivity samples collected by special equipment. At monitoring station samples are created by pumping high volumes of air through glass fibre filter. In Finland there are 8 monitoring stations. By default all the monitoring stations are selected and the results of measurements are search from the last 720 hours. The default values can be overwritten by using the time and location related input parameters.

* Query ID: `stuk::observations::air::radionuclide-activity-concentration::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2015-04-20T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2015-04-21T00:00:00Z).
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 27,64,28,65
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Savilahti,Kuopio).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067


## Latest dose rate of external radiation in Finland

This stored query return the latest results of the external dose rate measured by the automatic dose rate monitoring stations in Finland. The automatic dose rate monitoring network have about 255 monitoring stations distributed evenly around the Finland.  The monitoring network is maintained by Radiation and Nuclear Safety Authority (STUK). By default, the latest data is searched from the last 24 hours. The data is returned as a multipointcoverage format. The default values can be overwritten by using the time and location related input parameters.

* Query ID: `stuk::observations::external-radiation::latest::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067


## Latest dose rate of external radiation in Finland

This stored query return the latest dose rate of external radiation in Finland. The dose rate of external radiation is measured by an automatic external-dose rate-monitoring network maintained by Radiation and Nuclear Safety Authority (STUK) and local rescue services. The network comprises about 255 stations. By default, the latest data is searched from the last 24 hours. The data is returned as a simple format.

* Query ID: `stuk::observations::external-radiation::latest::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of parameters to return.
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067


## Dose rate of external radiation in Finland

This stored query return the results of the external dose rate measured by the automatic dose rate monitoring stations in Finland. The automatic dose rate monitoring network have about 255 monitoring stations distributed evenly around the Finland.  The monitoring network is maintained by Radiation and Nuclear Safety Authority (STUK). By default, the data is returned from the last 2 hours. The data is returned as a multipointcoverage format. The default values can be overwritten by using the time and location related input parameters.

* Query ID: `stuk::observations::external-radiation::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2012-02-27T00:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 21,61,22,62
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Kolari).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067


## Hourly Air Quality Observations

Hourly air quality observations from Finnish municipalities. By default, all the station are selected and the data is returned from the last 24 hours. The data is returned as multi point coverage format.

* Query ID: `urban::observations::airquality::hourly::multipointcoverage`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2015-03-13T10:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2015-03-13T12:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 24,60,25,61
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Helsinki).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around the location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)


## Hourly Air Quality Observations

Hourly air quality observations from Finnish municipalities. By default, all the station are selected and the data is returned from the last 24 hours. The data is returned as a simple feature format.

* Query ID: `urban::observations::airquality::hourly::simple`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2015-03-13T10:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2015-03-13T12:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 24,60,25,61
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Helsinki).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around a location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


## Hourly Air Quality Observations

Hourly air quality observations from Finnish municipalities. By default, all the station are selected and the data is returned from the last 24 hours. The data is returned as timevaluepair format.

* Query ID: `urban::observations::airquality::hourly::timevaluepair`
* Available arguments:
    * starttime (dateTime)
        * Begin of the time interval
        * Parameter begin specifies the begin of time interval in ISO-format (for example 2015-03-13T10:00:00Z).
    * endtime (dateTime)
        * End of time interval
        * End of time interval in ISO-format (for example 2015-03-13T12:00:00Z).
    * timestep (int)
        * The time step of data in minutes
        * The time step of data in minutes. Notice that timestep is calculated from start of the ongoing hour or day.
    * parameters (NameList)
        * Parameters to return
        * Comma separated list of parameters to return.
    * crs (xsi:string)
        * Coordinate projection to use in results
        * Coordinate projection to use in results. For example EPSG::3067
    * bbox (xsi:string)
        * Bounding box of area for which to return data.
        * Bounding box of area for which to return data (lon,lat,lon,lat). For example 24,60,25,61
    * place (xsi:string)
        * The location for which to provide data
        * The location for which to provide data. Region can be given after location name separated by comma (for example Kumpula,Helsinki).
    * fmisid (int)
        * FMI observation station identifier.
        * Identifier of the observation station.
    * maxlocations (int)
        * Amount of locations
        * How many observation stations are fetched around queried locations. Note that stations are only searched with 50 kilometers radius around a location.
    * geoid (int)
        * Geoid of the location for which to return data.
        * Geoid of the location for which to return data. (ID from geonames.org)
    * timezone (xsi:string)
        * Time zone
        * Time zone of the time instant of the data point in the form Area/Location (for example America/Costa_Rica). Default value is UTC.


# Available parameters

Parameters that can be named in the `parameters` argument of the queries
that have one.  Not every parameter is available from every query.

| ID | Description | Unit |
| --- | --- | --- |
| `ac_p7d_avg` | Activity concentration | µBq/m3 |
| `aero_pt1s_avg` | AERO-sähke |  |
| `akkuj` | Battery voltage | V |
| `aqindex_pt1h_avg` | Air Quality Index | index |
| `avika` | Sensor error |  |
| `batt` | Battery voltage | V |
| `batt_pt12h_min` | Battery voltage | V |
| `batt_pt1h_avg` | Battery voltage | V |
| `batt_pt1m_avg` | Battery voltage | V |
| `ble_pt1s_instant` | Battery age | weeks |
| `ch1_aws` | Height of base of cloud | m |
| `ch2_aws` | Height of base of 2. lowest cloud | m |
| `ch3_aws` | Height of base of 3. lowest cloud | m |
| `ch4_aws` | Height of base of 4. lowest cloud | m |
| `cla0_pt1m_instant` | Low or middle cloud amount | 1/8 |
| `cla1_pt1m_acc` | Low or middle cloud amount | 1/8 |
| `cla1_pt1m_instant` | Low or middle cloud amount | 1/8 |
| `cla2_pt1m_acc` | Second lowest cloud amount | 1/8 |
| `cla2_pt1m_instant` | Second lowest cloud amount | 1/8 |
| `cla3_pt1m_acc` | Third lowest cloud amount | 1/8 |
| `cla3_pt1m_instant` | Third lowest cloud amount | 1/8 |
| `cla4_pt1m_acc` | Fourth lowest cloud amount | 1/8 |
| `cla4_pt1m_instant` | Fourth lowest cloud amount | 1/8 |
| `cla5_pt1m_acc` | Fifth lowest cloud amount | 1/8 |
| `cla5_pt1m_instant` | Fifth lowest cloud amount | 1/8 |
| `cla_pt1m_acc` | Cloud amount | 1/8 |
| `cla_pt1m_instant` | Cloud amount | 1/8 |
| `clap1m` | Normal total cloudiness | % |
| `clap1m_p30y_avg` | Normal total cloudiness | % |
| `clcbst_pt10m_instant` | CB |  |
| `clh5_pt1m_instant` | Height of base of 5. lowest cloud | m |
| `clhb` | Height of base of cloud | m |
| `clhb1_pt1m_instant` | Height of base of cloud | m |
| `clhb2_pt1m_instant` | Height of base of 2. lowest cloud | m |
| `clhb3_pt1m_instant` | Height of base of 3. lowest cloud | m |
| `clhb4_pt1m_instant` | Height of base of 4. lowest cloud | m |
| `clhb_pt1m_instant` | Height of base of cloud | m |
| `clhbc_pt1m_instant` | Height of base of cloud |  |
| `cloudheight` | Height of base of cloud | m |
| `clth_pt1m_instant` | Cloud type, high clouds |  |
| `cltl_pt1m_instant` | Cloud type, low clouds |  |
| `cltm_pt1m_instant` | Cloud type, medium clouds |  |
| `co_p1d_avg` | Hiilimonoksidi | ug/m3 |
| `co_pt1h_avg` | Carbon monoxide | ug/m3 |
| `dd_pt1m_std` | Leviämissuunnan hajonta | deg |
| `dewpoint` | Dew-point temperature | degC |
| `diff_1min` | Diffuse radiation | W/m2 |
| `diff_p1d_sum` | Diffuse radiation | kJ/m2 |
| `diff_pt1h_sum` | Diffuse radiation | kJ/m2 |
| `diff_pt1m_avg` | Diffuse radiation | W/m2 |
| `dilma` | Air temperature change | degC |
| `dipaine` | Pressure tendency | hPa |
| `dir_1min` | Direct solar radiation | W/m2 |
| `dir_p1d_sum` | Direct solar radiation | W/m2 |
| `dir_pt1h_sum` | Direct solar radiation | kJ/m2 |
| `dir_pt1m_avg` | Direct solar radiation | W/m2 |
| `dr_pt10m_avg` | Dose rate | µSv/h |
| `drs1_pt10m_avg` | Relative uncertainty | µSv/h |
| `dtiel` | Road surface temperature change | degC |
| `dtiel_2` | Road surface temperature change | degC |
| `dtiel_3` | Road surface temperature change | degC |
| `dtiel_4` | Road surface temperature change | degC |
| `dtsc_pt10m_avg` | DT stability class |  |
| `elecst` | Electricity |  |
| `elecst_pt1m_instant` | Electricity |  |
| `evpp1m` | Normal monthly mean vapour pressure | hPa |
| `evpp1m_p30y_avg` | Normal monthly mean vapour pressure | hPa |
| `fc` | Friction |  |
| `fc_pt1m_instant` | Friction |  |
| `fzfreq_pt1m_instant` | Jäätämisanturin tuottama taajuustieto | 1/s |
| `fzmm_pt1h_acc` | Jään kertymisnopeus | mm/h |
| `gfr_p1d_avg` | Routa | cm |
| `glob_1min` | Global radiation | W/m2 |
| `glob_p1d_sum` | Global radiation | kJ/m2 |
| `glob_pt10m_avg` | Global radiation | W/m2 |
| `glob_pt1h_avg` | Global radiation | W/m2 |
| `glob_pt1h_sum` | Kokonaissäteily | kJ/m2 |
| `glob_pt1m_avg` | Global radiation | W/m2 |
| `glob_u` | Global radiation | W/m2 |
| `globa_pt1m_avg` | Global radiation on tilted surface | W/m2 |
| `globp1m` | Global radiation | W/m2 |
| `globp1m_p30y_avg` | Global radiation | W/m2 |
| `globp1y` | Global radiation | W/m2 |
| `globp1y_p30y_avg` | Global radiation | W/m2 |
| `gr_p1d_instant` | State of the ground |  |
| `gr_pt1m_instant` | State of the ground |  |
| `grs1_pt1m_instant` | State of the ground (E) |  |
| `grs2_pt1m_instant` | State of the ground (E¿) |  |
| `grs_pt1m_instant` | State of the ground |  |
| `gwl_pt1m_avg` | Pohjavesi | m |
| `hdd_p1d_avg` | Lämmitystarve | degC |
| `hrrs_pt1s_avg` | HR-luotaus |  |
| `humidity` | Relative humidity | % |
| `ice_obs_pt1s_instant` | Manual ice observation |  |
| `ice_pt1s_instant` | Jään kokonaispaksuuksien keskiarvo | cm |
| `icest_pt10m_avg` | Jäätäminen |  |
| `ict_pt1m_avg` | Jäätä | cm |
| `ilma` | Air temperature | degC |
| `ilma_2` | Air temperature | degC |
| `ilma_3` | Air temperature | degC |
| `ipaine` | Pressure | hPa |
| `jaatj` | Icefrequency | Hz |
| `jaatj_2` | Icefrequency | Hz |
| `jaatj_3` | Icefrequency | Hz |
| `jaatj_4` | Icefrequency | Hz |
| `jaatp` | Freezing point temperature | degC |
| `jaatp_2` | Freezing point temperature | degC |
| `jaatp_3` | Freezing point temperature | degC |
| `jaatp_4` | Freezing point temperature | degC |
| `kastep` | Dew-point temperature | degC |
| `keli` | State of the road condition |  |
| `keli2` | State of the road condition |  |
| `keli_2` | State of the road condition |  |
| `keli_3` | State of the road condition |  |
| `keli_4` | State of the road condition |  |
| `kitka` | Friction |  |
| `kitka_3` | Friction |  |
| `kosm_2` | Surface moisture | mm |
| `kosma` | Surface moisture | mm |
| `koste_1` | Relative humidity | % |
| `koste_3` | Relative humidity | % |
| `kpero` | Dewpoint difference | degC |
| `ktuuli` | Wind speed | m/s |
| `li` | Ice layer | mm |
| `lidar_pt1s_avg` | Lidar-profiili |  |
| `ls` | Snow layer | mm |
| `lw` | Water layer | mm |
| `lwin_1min` | Long wave solar radiation | W/m2 |
| `lwin_p1d_sum` | Long wave solar radiation | kJ/m2 |
| `lwin_pt1h_sum` | Long wave solar radiation | kJ/m2 |
| `lwin_pt1m_avg` | Long wave solar radiation | W/m2 |
| `lwout_1min` | Long wave outgoing solar radiation | W/m2 |
| `lwout_p1d_sum` | Long wave outgoing solar radiation | kJ/m2 |
| `lwout_pt1h_sum` | Long wave outgoing solar radiation | kJ/m2 |
| `lwout_pt1m_avg` | Long wave outgoing solar radiation | W/m2 |
| `m500e_pt1m_instant` | M500 error code |  |
| `maal` | Road ground temperature | degC |
| `maal_2` | Road ground temperature | degC |
| `maal_3` | Road ground temperature | degC |
| `maal_4` | Road ground temperature | degC |
| `maximumtemperature` | Maximum temperature | degC |
| `minimumgroundtemperature06` | Ground minimum temperature | degC |
| `minimumtemperature` | Minimum temperature | degC |
| `modalwdi` | Direction of waves | deg |
| `mol_pt10m_avg` | Monin-Obukov length | 1/m |
| `ms` | Soil relative humidity | m3/m3 |
| `ms_1h_avg` | Soil relative humidity | m3/m3 |
| `ms_1h_max` | Soil maximum humidity | m3/m3 |
| `ms_1h_min` | Soil minimum humidity | m3/m3 |
| `ms_pt1h_avg` | Soil relative humidity | m3/m3 |
| `ms_pt1h_max` | Soil maximum humidity | m3/m3 |
| `ms_pt1h_min` | Soil minimum humidity | m3/m3 |
| `ms_pt1m_avg` | Soil relative humidity | m3/m3 |
| `mtk1_pt10m_avg` | Metek 1: means | m/s |
| `mtk2_pt10m_avg` | Metek 2: deviations | m/s |
| `mtk3_pt10m_avg` | Metek 3: Covariances | m2/s2 |
| `mtk4_pt10m_avg` | Metek 4: T measurements | K |
| `mtk5_pt10m_avg` | Metek 5: turbulence | K |
| `mtk6_pt10m_avg` | Metek 6: Friction velocity | m/s |
| `mtk7_pt10m_avg` | Metek 7: Vertical momentum | kg/ms2 |
| `mtuuli` | Gust speed | m/s |
| `n` | Cloud amount | 1/8 |
| `n_man` | Cloud amount | 1/8 |
| `ndpr001p1m` | Precipitation days 0.1 mm normal | # |
| `ndpr001p1m_p30y_avg` | Precipitation days 0.1 mm normal | # |
| `ndpr001p1y` | Precipitation days 0.1 mm normal | # |
| `ndpr001p1y_p30y_avg` | Precipitation days 0.1 mm normal | # |
| `ndpr010p1m` | Precipitation days 1.0 mm normal | # |
| `ndpr010p1m_p30y_avg` | Precipitation days 1.0 mm normal | # |
| `ndpr010p1y` | Precipitation days 1 mm normal | # |
| `ndpr010p1y_p30y_avg` | Precipitation days 1 mm normal | # |
| `ndpr100p1m` | Precipitation days 10 mm normal | # |
| `ndpr100p1m_p30y_avg` | Precipitation days 10 mm normal | # |
| `ndpr100p1y` | Precipitation days 10 mm normal | # |
| `ndpr100p1y_p30y_avg` | Precipitation days 10 mm normal | # |
| `ndtan0p1m` | Days with minimum temperature <0C | # |
| `ndtan0p1m_p30y_avg` | Days with minimum temperature <0C | # |
| `ndtan0p1y` | Days with minimum temperature <0C | # |
| `ndtan0p1y_p30y_avg` | Days with minimum temperature <0C | # |
| `ndtan10p1m` | Days with minimum temperature <-10C | # |
| `ndtan10p1m_p30y_avg` | Days with minimum temperature <-10C | # |
| `ndtan10p1y` | Days with minimum temperature <-10C | # |
| `ndtan10p1y_p30y_avg` | Days with minimum temperature <-10C | # |
| `ndtax0p1m` | Days with maximum temperature <0C | # |
| `ndtax0p1m_p30y_avg` | Days with maximum temperature <0C | # |
| `ndtax0p1y` | Days with maximum temperature <0C | # |
| `ndtax0p1y_p30y_avg` | Days with maximum temperature <0C | # |
| `ndtax25p1m` | Days with maximum temperature >25C | # |
| `ndtax25p1m_p30y_avg` | Days with maximum temperature >25C | # |
| `ndtax25p1y` | Days with maximum temperature >25C | # |
| `ndtax25p1y_p30y_avg` | Days with maximum temperature >25C | # |
| `ndtg0p1m` | Days with ground minimum temperature <0C | # |
| `ndtg0p1m_p30y_avg` | Days with ground minimum temperature <0C | # |
| `net_1min` | Radiation balance | W/m2 |
| `net_p1d_sum` | Radiation balance | W/m2 |
| `net_pt10m_avg` | Radiation balance | W/m2 |
| `net_pt1h_avg` | Radiation balance | W/m2 |
| `net_pt1h_sum` | Säteilytase | kJ/m2 |
| `net_pt1m_avg` | Radiation balance | W/m2 |
| `no2_exceed_pt1h_avg` | Typpidioksidin raja-arvon ylitys | ug/m3 |
| `no2_p1d_avg` | Typpidioksidi | ug/m3 |
| `no2_pt1h_avg` | Nitrogen dioxide | ug/m3 |
| `no_p1d_avg` | Typpimonoksidi | ug/m3 |
| `no_pt1h_avg` | Nitrogen monoxide | ug/m3 |
| `nox_p1d_avg` | Typen oksidit | ugNO2/m3 |
| `nox_pt1h_avg` | Nitrogen oxides | ugNO2/m3 |
| `o3_8h_exceed_pt1h_avg` | Otsonin 8h raja-arvon ylitys | ug/m3 |
| `o3_exceed_pt1h_avg` | Otsonin raja-arvon ylitys | ug/m3 |
| `o3_p1d_avg` | Otsoni | ug/m3 |
| `o3_pt1h_avg` | Ozone | ug/m3 |
| `ot_pt1m_avg` | Voltage | µV |
| `ozone_pt1m_avg` | OTSONI | DU |
| `oztot_p1d_avg` | Ozone | DU |
| `p0_pt1m_avg` | Pressure | hPa |
| `p_sea` | Pressure (msl) | hPa |
| `pa0p1m` | Air pressure normal | hPa |
| `pa0p1m_p30y_avg` | Air pressure normal | hPa |
| `pa_10m_dif` | Pressure tendency | hPa |
| `pa_p1d_avg` | Air pressure | hPa |
| `pa_pt10m_avg` | Pressure tendency | hPa |
| `pa_pt1h_avg` | Air pressure | hPa |
| `pa_pt1m_avg` | Pressure (msl) | hPa |
| `pa_pt3h_avg` | Pressure change | hPa |
| `paa_pt3h_avg` | Pressure tendency |  |
| `pap1m` | Air pressure normal | hPa |
| `pap1m_p30y_avg` | Air pressure normal | hPa |
| `pap1y` | Air pressure normal | hPa |
| `pap1y_p30y_avg` | Air pressure normal | hPa |
| `pap_pt1s_avg` | Ilmanpaine | hPa |
| `par_pt1h_avg` | PAR-radiation | umol/sm2 |
| `par_pt1m_avg` | PAR-radiation | umol/sm2 |
| `parin_pt10m_avg` | PAR in-radiation | umol/sm2 |
| `parout_pt10m_avg` | PAR out-radiation | umol/sm2 |
| `pm10_p1d_avg` | Hengitettävät hiukkaset | ug/m3 |
| `pm10_p1d_exceed_p1d_avg` | PM10 päiväarvon raja-arvoylitys | ug/m3 |
| `pm10_pt1h_avg` | Particulate matter < 10 µm | ug/m3 |
| `pm25_p1d_avg` | Pienhiukkaset | ug/m3 |
| `pm25_p1d_exceed_p1d_avg` | Pienhiukkasten vuorokausikeskiarvon ohjearvon ylitys | ug/m3 |
| `pm25_pt1h_avg` | Particulate matter < 2.5 µm | ug/m3 |
| `po` | Pressure | hPa |
| `pra_1h_acc` | Precipitation amount | mm |
| `pra_p1m_sum` | Monthly precipitation amount | mm |
| `pra_pt10m_acc` | Precipitation amount | mm |
| `pra_pt12h_acc` | Precipitation amount | mm |
| `pra_pt1h_acc` | Precipitation amount | mm |
| `pra_pt24h_acc` | Precipitation amount | mm |
| `pra_pt24h_sum` | Precipitation amount | mm |
| `pra_pt3h_acc` | Precipitation amount | mm |
| `pra_pt6h_acc` | Precipitation amount | mm |
| `prao_24h_acc` | Precipitation amount (opt) | mm |
| `prao_pt12h_acc` | Precipitation amount (optical) | mm |
| `prao_pt1h_acc` | Precipitation amount (otical) | mm |
| `prao_pt24h_acc` | Precipitation amount (opt) | mm |
| `prap1m` | Normal monthly precipitation | mm |
| `prap1m_p30y_avg` | Normal monthly precipitation | mm |
| `prap1y` | Normal yearly precipitation | mm |
| `prap1y_p30y_avg` | Normal yearly precipitation | mm |
| `prat_pt12h_acc` | Precipitation amount (tipping) | mm |
| `prat_pt1h_acc` | Precipitation amount (tipping) | mm |
| `prclst` | Precipitation/cloudiness |  |
| `prclst_pt1m_instant` | Precipitation/cloudiness |  |
| `prd_pt10m_acc` | Precipitation duration | min |
| `prd_pt1h_acc` | Precipitation duration | min |
| `prd_pt1m_acc` | Precipitation duration | s |
| `precipitation1h` | Precipitation amount | mm |
| `precipitationform` | Weather codes (AIY) |  |
| `presentweather` | Present weather (auto) |  |
| `pressure` | Pressure (msl) | hPa |
| `pri` | Precipitation intensity | mm/h |
| `pri_pt10m_avg` | Precipitation intensity | mm/h |
| `pri_pt1h_max` | Maximum precipitation intensity | mm/h |
| `pri_pt1m_avg` | Precipitation intensity | mm/h |
| `prio_pt10m_avg` | Precipitation intensity (optical) | mm/h |
| `prio_pt1h_max` | Maximum precipitation intensity (optical) | mm/h |
| `pron_pt10m_acc` | Precipitation on/off |  |
| `prst1` | Precipitation state |  |
| `prst1_pt1m_instant` | Precipitation state |  |
| `prst2` | Precipitation state |  |
| `prst2_pt1m_instant` | Precipitation state |  |
| `psing` | Surfacesignal | V |
| `psing_2` | Surfacesignal | V |
| `psing_3` | Surfacesignal | V |
| `psing_4` | Surfacesignal | V |
| `pt_pt1m_avg` | Voltage | V |
| `q123tmbenzene_pt1s_avg` | 1,2,3-trimetyylibentseeni | ug/m3 |
| `q124tmbenzene_pt1s_avg` | 1,2,4-trimetyylibentseeni | ug/m3 |
| `q135tmbenzene_pt1s_avg` | 1,3,5-trimetyylibentseeni | ug/m3 |
| `q13butadiene_pt1s_avg` | 1,3-butadiene | ug/m3 |
| `q1butene_pt1s_avg` | 1-buteeni | ug/m3 |
| `q1pentene_pt1s_avg` | 1-penteeni | ug/m3 |
| `q224tmpentane_pt1s_avg` | 2,2,4-trimetyylipentaani | ug/m3 |
| `q2etyylitolueeni_pt1s_avg` | 2-etyylitolueeni | ug/m3 |
| `q2m13butadiene_pt1s_avg` | 2-metyyli-1,3-butadieeni | ug/m3 |
| `q2mbutane_pt1s_avg` | 2-metyylibutaani | ug/m3 |
| `q2mpentane_pt1s_avg` | 2-methylpentaani | ug/m3 |
| `q2mpropene_pt1s_avg` | 2-metyylipropeeni | ug/m3 |
| `q2pentene_pt1s_avg` | 2-penteeni | ug/m3 |
| `q3etyylitolueeni_pt1s_avg` | 3-etyylitolueeni | ug/m3 |
| `q3mpentane_pt1s_avg` | 3-methylpentaani | ug/m3 |
| `q4etyylitolueeni_pt1s_avg` | 4-etyylitolueeni | ug/m3 |
| `qacedep_pt1s_avg` | asenafteeni kokonaislaskeumassa | ug/m2/day |
| `qacepm10_pt1s_avg` | asenafteeni PM10 | ng/m3 |
| `qacldep_pt1s_avg` | asenaftyleeni kokonaislaskeumassa | ug/m2/day |
| `qaclpm10_pt1s_avg` | asenaftyleeni PM10 | ng/m3 |
| `qairvolemep_pt1s_avg` | ilmamäärä (EMEP suodatin) | m3 |
| `qairvolpm10hm_pt1s_avg` | ilmamäärä (PM10 raskasmetallit) | m3 |
| `qairvolpm10pah_pt1s_avg` | ilmamäärä (PM10 PAH) | m3 |
| `qairvolpm25_pt1s_avg` | ilmamaara (PM2.5 ionit) | m3 |
| `qalpm10_pt1s_avg` | alumiini PM10 | ng/m3 |
| `qalprec_pt1s_avg` | alumiini kokonaislaskeumassa | ug/l |
| `qandep_pt1s_avg` | antraseeni kokonaislaskeumassa | ug/m2/day |
| `qanpm10_pt1s_avg` | antraseeni PM10 | ng/m3 |
| `qaspm10_pt1s_avg` | arseeni PM10 | ng/m3 |
| `qasprec_pt1s_avg` | arseeni kokonaislaskeumassa | ug/l |
| `qbaadep_pt1s_avg` | bentso(a)antraseeni kokonaislaskeumassa | ug/m2/day |
| `qbaapm10_pt1s_avg` | bentso(a)antraseeni PM10 | ng/m3 |
| `qbapairaerosol_pt1s_avg` | bentso(a)pyreeni (air+aerosol) | ng/m3 |
| `qbapdep_pt1s_avg` | bentso(a)pyreeni kokonaislaskeumassa | ug/m2/day |
| `qbappm10_pt1s_avg` | bentso(a)pyreeni PM10 | ng/m3 |
| `qbbfadep_pt1s_avg` | bentso(b)fluoranteeni kokonaislaskeumassa | ug/m2/day |
| `qbbfapm10_pt1s_avg` | bentso(b)fluoranteeni PM10 | ng/m3 |
| `qbbjkfadep_pt1s_avg` | bentso(b,j,k)fluoranteeni kokonaislaskeumassa | ug/m2/day |
| `qbbjkfapm10_pt1s_avg` | bentso(b,j,k)fluoranteeni PM10 | ng/m3 |
| `qbcpm25_pt1h_avg` | musta hiili PM2.5 | ug/m3 |
| `qbcpm25_pt1s_avg` | musta hiili PM2.5 | ug/m3 |
| `qbenzene_pt1s_avg` | bentseeni | ug/m3 |
| `qbghipdep_pt1s_avg` | bentso(ghi)peryleeni kokonaislaskeumassa | ug/m2/day |
| `qbghippm10_pt1s_avg` | bentso(ghi)peryleeni PM10 | ng/m3 |
| `qbjfadep_pt1s_avg` | bentso(j)fluoranteeni kokonaislaskeumassa | ug/m2/day |
| `qbjfapm10_pt1s_avg` | bentso(j)fluoranteeni PM10 | ng/m3 |
| `qbkfadep_pt1s_avg` | bentso(k)fluoranteeni kokonaislaskeumassa | ug/m2/day |
| `qbkfapm10_pt1s_avg` | bentso(k)fluoranteeni PM10 | ng/m3 |
| `qc2butene_pt1s_avg` | cis-2-buteeni | ug/m3 |
| `qc2pentene_pt1s_avg` | cis-2-penteeni | ug/m3 |
| `qcaaerosol_pt1s_avg` | kalsium  (EMEP-suodatin) | ug/m3 |
| `qcapm25_pt1s_avg` | kalsium PM2.5 | ug/m3 |
| `qcaprec_pt1s_avg` | kalsium kokonaislaskeumassa | mg/l |
| `qcdpm10_pt1s_avg` | kadmium PM10 | ng/m3 |
| `qcdprec_pt1s_avg` | kadmium kokonaislaskeumassa | ug/l |
| `qchrdep_pt1s_avg` | kryseeni kokonaislaskeumassa | ug/m2/day |
| `qchrpm10_pt1s_avg` | kryseeni PM10 | ng/m3 |
| `qchrtpdep_pt1s_avg` | kryseeni+trifenyleeni kokonaislaskeumassa | ug/m2/day |
| `qchrtppm10_pt1s_avg` | kryseeni+trifenyleeni PM10 | ng/m3 |
| `qclaerosol_pt1s_avg` | kloridi  (EMEP-suodatin) | ug/m3 |
| `qclpm25_pt1s_avg` | kloridi PM2.5 | ug/m3 |
| `qclprec_pt1s_avg` | kloridi kokonaislaskeumassa | mg/l |
| `qcopm10_pt1s_avg` | koboltti PM10 | ng/m3 |
| `qcoprec_pt1s_avg` | koboltti kokonaislaskeumassa | ug/l |
| `qcrpm10_pt1s_avg` | kromi PM10 | ng/m3 |
| `qcrprec_pt1s_avg` | kromi kokonaislaskeumassa | ug/l |
| `qcupm10_pt1s_avg` | kupari PM10 | ng/m3 |
| `qcuprec_pt1s_avg` | kupari kokonaislaskeumassa | ug/l |
| `qcyclohexane_pt1s_avg` | sykloheksaani | ug/m3 |
| `qdbacahapm10_pt1s_avg` | dibentso(ah+ac)antraseeni PM10 | ng/m3 |
| `qdbahacadep_pt1s_avg` | dibentso(ac+ah)antraseeni kokonaislaskeumassa | ug/m2/day |
| `qdbahadep_pt1s_avg` | dibentso(ah)antraseeni kokonaislaskeumassa | ug/m2/day |
| `qdbahapm10_pt1s_avg` | dibentso(ah)antraseeni PM10 | ng/m3 |
| `qecpm25_pt1s_avg` | alkuainehiili PM2.5 | ug/m3 |
| `qetbe_pt1s_avg` | etyylitertiääributyylieetteri | ug/m3 |
| `qethane_pt1s_avg` | etaani | ug/m3 |
| `qethene_pt1s_avg` | eteeni | ug/m3 |
| `qethylbenzene_pt1s_avg` | etyylibentseeni | ug/m3 |
| `qethyne_pt1s_avg` | etyyni | ug/m3 |
| `qfadep_pt1s_avg` | fluoranteeni kokonaislaskeumassa | ug/m2/day |
| `qfapm10_pt1s_avg` | fluoranteeni PM10 | ng/m3 |
| `qfepm10_pt1s_avg` | rauta PM10 | ng/m3 |
| `qfeprec_pt1s_avg` | rauta kokonaislaskeumassa | ug/l |
| `qfldep_pt1s_avg` | fluoreeni kokonaislaskeumassa | ug/m2/day |
| `qflpm10_pt1s_avg` | fluoreeni PM10 | ng/m3 |
| `qheptane_pt1s_avg` | heptaani | ug/m3 |
| `qhexane_pt1s_avg` | heksaani | ug/m3 |
| `qhgegm_pt1s_avg` | alkuainemuotoinen elohopeahöyry | ng/m3 |
| `qhgpm10_pt1s_avg` | hiukkasiin sitoutunut elohopea | ng/m3 |
| `qhgprec_pt1s_avg` | elohopea kokonaislaskeumassa | ng/l |
| `qhgrgm_pt1s_avg` | reaktiivinen kaasumainen elohopea | ng/m3 |
| `qhgtgm_pt1s_avg` | kaasumaisen elohopean kokonaismäärä | ng/m3 |
| `qhno3nair_pt1s_avg` | typpihappo-N (EMEP-suodatin) | ugN/m3 |
| `qhno3no3nairaero_pt1s_avg` | kokonaisnitraatti-N  (EMEP-suodatin) | ugN/m3 |
| `qhprec_pt1s_avg` | vetyionikonsentraatio kokonaislaskeumassa | umol/l |
| `qibutane_pt1s_avg` | i-butaani | ug/m3 |
| `qipdep_pt1s_avg` | indeno(1,2,3-cd)pyreeni kokonaislaskeumassa | ug/m2/day |
| `qippm10_pt1s_avg` | indeno(1,2,3-cd)pyreeni PM10 | ng/m3 |
| `qkaerosol_pt1s_avg` | kalium  (EMEP-suodatin) | ug/m3 |
| `qkpm25_pt1s_avg` | kalium PM2.5 | ug/m3 |
| `qkprec_pt1s_avg` | kalium kokonaislaskeumassa | mg/l |
| `qmgaerosol_pt1s_avg` | magnesium  (EMEP-suodatin) | ug/m3 |
| `qmgpm25_pt1s_avg` | magnesium PM2.5 | ug/m3 |
| `qmgprec_pt1s_avg` | magnesium kokonaislaskeumassa | mg/l |
| `qmnpm10_pt1s_avg` | mangaani PM10 | ng/m3 |
| `qmnprec_pt1s_avg` | mangaani kokonaislaskeumassa | ug/l |
| `qmopm10_pt1s_avg` | molybdeeni PM10 | ng/m3 |
| `qmpxylene_pt1s_avg` | m,p-ksyleeni | ug/m3 |
| `qnaaerosol_pt1s_avg` | natrium  (EMEP-suodatin) | ug/m3 |
| `qnafdep_pt1s_avg` | naftaleeni kokonaislaskeumassa | ug/m2/day |
| `qnafpm10_pt1s_avg` | naftaleeni PM10 | ng/m3 |
| `qnapm25_pt1s_avg` | natrium PM2.5 | ug/m3 |
| `qnaprec_pt1s_avg` | natrium kokonaislaskeumassa | mg/l |
| `qnbutane_pt1s_avg` | n-butaani | ug/m3 |
| `qnh3nair_pt1s_avg` | ammoniakki-N  (EMEP-suodatin) | ugN/m3 |
| `qnh3nh4nairaero_pt1s_avg` | kokonaisammonium-N  (EMEP-suodatin) | ugN/m3 |
| `qnh4naerosol_pt1s_avg` | ammonium-N  (EMEP-suodatin) | ugN/m3 |
| `qnh4pm25_pt1s_avg` | ammonium PM2.5 | ug/m3 |
| `qnh4prec_pt1s_avg` | ammonium kokonaislaskeumassa | mgN/l |
| `qnipm10_pt1s_avg` | nikkeli PM10 | ng/m3 |
| `qniprec_pt1s_avg` | nikkeli kokonaislaskeumassa | ug/l |
| `qno2_pt1s_avg` | Typpidioksidi | ug/m3 |
| `qno3naerosol_pt1s_avg` | nitraatti-N  (EMEP-suodatin) | ugN/m3 |
| `qno3pm25_pt1s_avg` | nitraatti PM2.5 | ug/m3 |
| `qno3prec_pt1s_avg` | nitraatti kokonaislaskeumassa | mgN/l |
| `qnoctane_pt1s_avg` | n-oktaani | ug/m3 |
| `qocpm25_pt1s_avg` | orgaaninen hiili PM2.5 | ug/m3 |
| `qoxylene_pt1s_avg` | o-ksyleeni | ug/m3 |
| `qpbpm10_pt1s_avg` | lyijy PM10 | ng/m3 |
| `qpbprec_pt1s_avg` | lyijy kokonaislaskeumassa | ug/l |
| `qpentane_pt1s_avg` | pentaani | ug/m3 |
| `qphedep_pt1s_avg` | fenantreeni kokonaislaskeumassa | ug/m2/day |
| `qphepm10_pt1s_avg` | fenantreeni PM10 | ng/m3 |
| `qphprec_pt1s_avg` | kokonaislaskeuman happamuus | pH |
| `qprchg_pt1s_avg` | elohopealaskeuman sademäärä | mm |
| `qprchm_pt1s_avg` | metallilaskeuman sademäärä | mm |
| `qprcions_pt1s_avg` | laskeumanäytteen sademäärä | mm |
| `qprcpah_pt1s_avg` | PAH-laskeumakeräyksen sademäärä | l |
| `qpropane_pt1s_avg` | propaani | ug/m3 |
| `qpropene_pt1s_avg` | propeeni | ug/m3 |
| `qpropylbenzene_pt1s_avg` | propyylibentseeni | ug/m3 |
| `qpropyne_pt1s_avg` | propyyni | ug/m3 |
| `qpydep_pt1s_avg` | pyreeni kokonaislaskeumassa | ug/m2/day |
| `qpypm10_pt1s_avg` | pyreeni PM10 | ng/m3 |
| `qsbpm10_pt1s_avg` | antimoni PM10 | ng/m3 |
| `qsjkprec_pt1s_avg` | kokonaislaskeuman sähkönjohtokyky | uS/cm |
| `qso2sair_pt1s_avg` | rikkidioksidi-S (EMEP-suodatin) | ugS/m3 |
| `qso4pm25_pt1s_avg` | sulfaatti PM2.5 | ug/m3 |
| `qso4prec_pt1s_avg` | sulfaatti kokonaislaskeumassa | mgS/l |
| `qso4saerosol_pt1s_avg` | sulfaatti-S  (EMEP-suodatin) | ugS/m3 |
| `qstyrene_pt1s_avg` | styreeni | ug/m3 |
| `qt2butene_pt1s_avg` | trans-2-buteeni | ug/m3 |
| `qt2pentene_pt1s_avg` | trans-2-penteeni | ug/m3 |
| `qtoluene_pt1s_avg` | tolueeni | ug/m3 |
| `qvpm10_pt1s_avg` | vanadiini PM10 | ng/m3 |
| `qvprec_pt1s_avg` | vanadiini kokonaislaskeumassa | ug/l |
| `qxylene_pt1s_avg` | ksyleeni | ug/m3 |
| `qznpm10_pt1s_avg` | sinkki PM10 | ng/m3 |
| `qznprec_pt1s_avg` | sinkki kokonaislaskeumassa | ug/l |
| `r_1h` | Precipitation amount | mm |
| `rbp_pt1s_avg` | beta | µGy/h |
| `refl_1min` | Reflected radiation | W/m2 |
| `refl_p1d_sum` | Reflected radiation | kJ/m2 |
| `refl_pt10m_avg` | Reflected radiation | W/m2 |
| `refl_pt1h_avg` | Reflected radiation | W/m2 |
| `refl_pt1h_sum` | Heijastunutsäteily | kJ/m2 |
| `refl_pt1m_avg` | Reflected radiation | W/m2 |
| `relativehumidity` | Relative humidity | % |
| `rgp_pt1s_avg` | Gamma | µGy/h |
| `rh` | Relative humidity | % |
| `rh00p1m` | Normal relative humidity 00 utc | % |
| `rh00p1m_p30y_avg` | Normal relative humidity 00 utc | % |
| `rh00p1y` | Normal relative humidity 00 utc | % |
| `rh00p1y_p30y_avg` | Normal relative humidity 00 utc | % |
| `rh06p1m` | Normal relative humidity 00 utc | % |
| `rh06p1m_p30y_avg` | Normal relative humidity 00 utc | % |
| `rh06p1y` | Normal relative humidity 00 utc | % |
| `rh06p1y_p30y_avg` | Normal relative humidity 00 utc | % |
| `rh12p1m` | Normal relative humidity 00 utc | % |
| `rh12p1m_p30y_avg` | Normal relative humidity 00 utc | % |
| `rh12p1y` | Normal relative humidity 00 utc | % |
| `rh12p1y_p30y_avg` | Normal relative humidity 00 utc | % |
| `rh18p1m` | Normal relative humidity 00 utc | % |
| `rh18p1m_p30y_avg` | Normal relative humidity 00 utc | % |
| `rh18p1y` | Normal relative humidity 00 utc | % |
| `rh18p1y_p30y_avg` | Normal relative humidity 00 utc | % |
| `rh_2` | Relative humidity | % |
| `rh_3` | Relative humidity | % |
| `rh_p1d_avg` | Relative humidity | % |
| `rh_pt10m_avg` | Relative humidity | % |
| `rh_pt1h_avg` | Relative humidity | % |
| `rh_pt1m_avg` | Relative humidity | % |
| `rh_pt3m_avg` | Relative humidity | % |
| `rhc_pt1h_avg` | Canoby relative humidity | % |
| `rhc_pt1m_avg` | Canoby relative humidity | % |
| `rhp1m` | Normal relative humidity | % |
| `rhp1m_p30y_avg` | Normal relative humidity | % |
| `rhp1y` | Normal relative humidity | % |
| `rhp1y_p30y_avg` | Normal relative humidity | % |
| `rhp_pt1s_avg` | Relative humidity | % |
| `ri_10min` | Precipitation intensity | mm/h |
| `rint` | Precipitation intensity | mm/h |
| `rrcode_pt24h_rank` | Weather codes (AIY) |  |
| `rrday` | Precipitation amount | mm |
| `rrmon` | Monthly precipitation amount | mm |
| `rscal` | Alert of the road condition |  |
| `rscal3` | Alert of the road condition |  |
| `rscal3_pt1m_instant` | Alert of the road condition |  |
| `rscal_2` | Alert of the road condition |  |
| `rscal_3` | Alert of the road condition |  |
| `rscal_4` | Alert of the road condition |  |
| `rscal_pt1m_instant` | Alert of the road condition |  |
| `rscc` | Conductivity | V |
| `rscc_2` | Conductivity | V |
| `rscc_3` | Conductivity | V |
| `rscc_4` | Conductivity | V |
| `rscc_pt1m_instant` | Conductivity | V |
| `rscif` | Icefrequency | Hz |
| `rscif_2` | Icefrequency | Hz |
| `rscif_3` | Icefrequency | Hz |
| `rscif_4` | Icefrequency | Hz |
| `rscif_pt1m_instant` | Icefrequency | Hz |
| `rscss` | Surfacesignal | V |
| `rscss_2` | Surfacesignal | V |
| `rscss_3` | Surfacesignal | V |
| `rscss_4` | Surfacesignal | V |
| `rscss_pt1m_instant` | Surfacesignal | V |
| `rscsst` | Station Status |  |
| `rscsst_pt1m_instant` | Station Status |  |
| `rscst` | State of the road condition |  |
| `rscst3` | State of the road condition |  |
| `rscst3_pt1m_instant` | State of the road condition |  |
| `rscst_2` | State of the road condition |  |
| `rscst_3` | State of the road condition |  |
| `rscst_4` | State of the road condition |  |
| `rscst_pt1m_instant` | State of the road condition |  |
| `rshu` | Surface moisture | mm |
| `rshu_2` | Surface moisture | mm |
| `rshu_pt1m_instant` | Surface moisture | mm |
| `rsil` | Ice layer | mm |
| `rsil_pt1m_instant` | Ice layer | mm |
| `rssl` | Snow layer | mm |
| `rssl_pt1m_instant` | Snow layer | mm |
| `rst` | Precipitation state |  |
| `rstdd_pt1m_instant` | Surface dewpoint difference | degC |
| `rsum` | Precipitation amount (opt) | mm |
| `rsum1h` | Precipitation amount | mm |
| `rswl` | Water layer | mm |
| `rswl_pt1m_instant` | Water layer | mm |
| `sade` | Precipitation/cloudiness |  |
| `savc` | Salt concentration | g/l |
| `savc_2` | Salt concentration | g/l |
| `savc_pt1m_instant` | Salt concentration | g/l |
| `sawc` | Salt amount | g/m2 |
| `sawc_2` | Salt amount | g/m2 |
| `sawc_pt1m_instant` | Salt amount | g/m2 |
| `scell_pt1h_avg` | Solar cell current | A |
| `sealevel` | Water level | mm |
| `senst` | Sensor error |  |
| `senst_pt1m_instant` | Sensor error |  |
| `sjoht` | Conductivity | V |
| `sjoht_2` | Conductivity | V |
| `sjoht_3` | Conductivity | V |
| `sjoht_4` | Conductivity | V |
| `smax_pt1s_acc` | Max energy | m2/Hz |
| `smax_pt1s_instant` | Max energy | m2/Hz |
| `snd15p1m` | Normal snow depth (15.) | cm |
| `snd15p1m_p30y_avg` | Normal snow depth (15.) | cm |
| `snd31p1m` | Normal snow depth (ld) | cm |
| `snd31p1m_p30y_avg` | Normal snow depth (ld) | cm |
| `snd_p1d_instant` | Snow depth | cm |
| `snd_pt10m_avg` | Snow depth | cm |
| `snd_pt10m_std` | Hajonta | cm |
| `snd_pt1m_instant` | Snow depth | cm |
| `sndice_pt1m_avg` | Lumensyvyyden keskiarvo jäällä | cm |
| `snow` | Snow depth | cm |
| `snow06` | Snow depth | cm |
| `snow_aws` | Snow depth | cm |
| `snow_ice_pt1s_instant` | Kohvajään paksuus | cm |
| `snowdepth` | Snow depth | cm |
| `snowdepth06` | Snow depth | cm |
| `snqn_pt10m_instant` | Laatuluku |  |
| `sns_pt1m_instant` | Snow state |  |
| `so2_exceed_pt1h_avg` | Rikkidioksidin raja-arvon ylitys | ug/m3 |
| `so2_p1d_avg` | Rikkidioksidi | ug/m3 |
| `so2_p1d_exceed_p1d_avg` | Rikkidioksidin päiväarvon raja-arvoylitys | ug/m3 |
| `so2_pt1h_avg` | Sulphur dioxide | ug/m3 |
| `stila` | Precipitation state |  |
| `stst` | Station Status |  |
| `sund_1min` | Sunshine duration | s |
| `sund_p1d_sum` | Sunshine duration | h |
| `sund_p1m_sum` | Sunshine duration | h |
| `sund_pt1h_sum` | Sunshine duration | h |
| `sund_pt1m_acc` | Sunshine duration | s |
| `sundp1m` | Normal sunshine duration | h |
| `sundp1m_p30y_avg` | Normal sunshine duration | h |
| `sundp1y` | Normal sunshine duration | h |
| `sundp1y_p30y_avg` | Normal sunshine duration | h |
| `suom` | Salt amount | g/m2 |
| `suom_2` | Salt amount | g/m2 |
| `suov` | Salt concentration | g/l |
| `suov_2` | Salt concentration | g/l |
| `svel_pt1h_avg` | Sound velocity | m/s |
| `svel_pt1s_instant` | Sound velocity | m/s |
| `svelp_pt1s_avg` | Äänennopeus vedessä | m/s |
| `swe_pt1m_avg` | Vesiarvo | kg/m2 |
| `t` | Air temperature | degC |
| `t2m` | Air temperature | degC |
| `ta` | Air temperature | degC |
| `ta00p1m` | Normal temperature 00 utc | degC |
| `ta00p1m_p30y_avg` | Normal temperature 00 utc | degC |
| `ta00p1y` | Normal temperature 00 utc | degC |
| `ta00p1y_p30y_avg` | Normal temperature 00 utc | degC |
| `ta06p1m` | Normal temperature 06 utc | degC |
| `ta06p1m_p30y_avg` | Normal temperature 06 utc | degC |
| `ta06p1y` | Normal temperature 06 utc | degC |
| `ta06p1y_p30y_avg` | Normal temperature 06 utc | degC |
| `ta12p1m` | Normal temperature 12 utc | degC |
| `ta12p1m_p30y_avg` | Normal temperature 12 utc | degC |
| `ta12p1y` | Normal temperature 12 utc | degC |
| `ta12p1y_p30y_avg` | Normal temperature 12 utc | degC |
| `ta18p1m` | Normal temperature 18 utc | degC |
| `ta18p1m_p30y_avg` | Normal temperature 18 utc | degC |
| `ta18p1y` | Normal temperature 18 utc | degC |
| `ta18p1y_p30y_avg` | Normal temperature 18 utc | degC |
| `ta_10m_dif` | Air temperature change | degC |
| `ta_2` | Air temperature | degC |
| `ta_24h_avg` | Air temperature | degC |
| `ta_24h_max` | Maximum temperature | degC |
| `ta_24h_min` | Minimum temperature | degC |
| `ta_3` | Air temperature | degC |
| `ta_p1d_avg` | Air temperature | degC |
| `ta_p1m_avg` | Monthly mean temperature | degC |
| `ta_pt10m_avg` | Air temperature | degC |
| `ta_pt10m_diffeb` | Air temperature change | degC |
| `ta_pt12h_max` | Maximum temperature | degC |
| `ta_pt12h_min` | Minimum temperature | degC |
| `ta_pt1h_avg` | Air temperature | degC |
| `ta_pt1h_max` | Highest temperature | degC |
| `ta_pt1h_min` | Lowest temperature | degC |
| `ta_pt1m_avg` | Air temperature | degC |
| `ta_pt24h_max` | Maximum temperature | degC |
| `ta_pt24h_min` | Minimum temperature | degC |
| `ta_pt3m_avg` | Air temperature | degC |
| `taft` | Safety temperature | degC |
| `taft_2` | Safety temperature | degC |
| `taft_pt1m_instant` | Safety temperature | degC |
| `tamaxp1m` | Normal maximum temperature | degC |
| `tamaxp1m_p30y_avg` | Normal maximum temperature | degC |
| `tamaxp1y` | Normal maximum temperature | degC |
| `tamaxp1y_p30y_avg` | Normal maximum temperature | degC |
| `taminp1m` | Normal minimum temperature | degC |
| `taminp1m_p30y_avg` | Normal minimum temperature | degC |
| `taminp1y` | Normal minimum temperature | degC |
| `taminp1y_p30y_avg` | Normal minimum temperature | degC |
| `tap1m` | Normal air temperature | degC |
| `tap1m_p30y_avg` | Normal air temperature | degC |
| `tap1y` | Normal air temperature | degC |
| `tap1y_p30y_avg` | Normal air temperature | degC |
| `tap_pt1s_avg` | Air temperature | degC |
| `tc_pt1h_avg` | Canoby stemperature | degC |
| `tc_pt1h_max` | Canoby maximum stemperature | degC |
| `tc_pt1h_min` | Canoby minimum temperature | degC |
| `tc_pt1m_avg` | Canoby stemperature | degC |
| `tcg3_pt1m_avg` | CG3 temperature | degC |
| `tcg4_pt1m_avg` | TCG4 temperature | degC |
| `tcgr3_pt1m_avg` | CGR3 temperature | degC |
| `tcgr4_pt1m_avg` | CGR4 temperature | degC |
| `tcnr4_pt1m_avg` | CNR4 temperature | degC |
| `td` | Dew-point temperature | degC |
| `td_pt10m_avg` | Dew-point temperature | degC |
| `td_pt1m_avg` | Dew-point temperature | degC |
| `td_pt3m_avg` | Dew-point temperature | degC |
| `tday` | Air temperature | degC |
| `tdd` | Dewpoint difference | degC |
| `tdd_pt1m_instant` | Dewpoint difference | degC |
| `tdp_pt1s_avg` | Dew point profile | degC |
| `temperature` | Air temperature | degC |
| `tfp_pt1m_avg` | Freezing point temperature | degC |
| `tg_pt12h_min` | Ground minimum temperature | degC |
| `tg_pt1h_avg` | Ground minimum temperature | degC |
| `tg_pt1m_avg` | Ground temperature | degC |
| `thc_pt10m_avg` | Comfort temperature | degC |
| `thc_pt1m_avg` | Comfort temperature | degC |
| `thc_pt3m_avg` | Comfort temperature | degC |
| `tie` | Road Surface temperature | degC |
| `tie_2` | Road Surface temperature | degC |
| `tie_3` | Road Surface temperature | degC |
| `tie_4` | Road Surface temperature | degC |
| `tmax` | Maximum temperature | degC |
| `tmax06` | Maximum temperature | degC |
| `tmax18` | Maximum temperature | degC |
| `tmin` | Minimum temperature | degC |
| `tmin06` | Minimum temperature | degC |
| `tmin18` | Minimum temperature | degC |
| `tmon` | Monthly mean temperature | degC |
| `totalcloudcover` | Cloud amount | 1/8 |
| `trb_pt10m_avg` | Wind turbulence | m/s |
| `trb_pt1m_avg` | Road base temperature | degC |
| `trfp` | Freezing point temperature | degC |
| `trfp_2` | Freezing point temperature | degC |
| `trfp_3` | Freezing point temperature | degC |
| `trfp_4` | Freezing point temperature | degC |
| `trg` | Road ground temperature | degC |
| `trg_2` | Road ground temperature | degC |
| `trg_3` | Road ground temperature | degC |
| `trg_4` | Road ground temperature | degC |
| `trg_pt1m_avg` | Road ground temperature | degC |
| `trs` | Road Surface temperature | degC |
| `trs_10min_dif` | Road surface temperature change | degC |
| `trs_10min_dif_2` | Road surface temperature change | degC |
| `trs_10min_dif_3` | Road surface temperature change | degC |
| `trs_10min_dif_4` | Road surface temperature change | degC |
| `trs_2` | Road Surface temperature | degC |
| `trs_3` | Road Surface temperature | degC |
| `trs_4` | Road Surface temperature | degC |
| `trs_pt10m_diffeb` | Road surface temperature change | degC |
| `trs_pt1m_avg` | Road Surface temperature | degC |
| `trsc_p1d_avg` | Haisevat rikkiyhdisteet | ugS/m3 |
| `trsc_pt1h_avg` | Odorous sulphur compounds | ugS/m3 |
| `ts` | Soil temperature | degC |
| `ts_1h_avg` | Soil stemperature | degC |
| `ts_1h_max` | Soil maximum stemperature | degC |
| `ts_1h_min` | Soil minimum temperature | degC |
| `ts_pt10m_avg` | Soil temperature | degC |
| `ts_pt1h_avg` | Soil stemperature | degC |
| `ts_pt1h_max` | Soil maximum stemperature | degC |
| `ts_pt1h_min` | Soil minimum temperature | degC |
| `ts_pt1m_avg` | Soil temperature | degC |
| `tsl501a_pt1m_avg` | SL501A temperature | degC |
| `tsn_pt10m_avg` | Snow temperature | degC |
| `tsn_pt12h_min` | Ground minimum temperature | degC |
| `tsn_pt1m_avg` | Ground temperature | degC |
| `tsp_pt1h_avg` | Total suspended particulates | ug/m3 |
| `tsuunt` | Wind direction | deg |
| `ttech_pt1h_avg` | Tecnical temperature | degC |
| `ttech_pt1m_avg` | Tecnical temperature | degC |
| `turl` | Safety temperature | degC |
| `turl_2` | Safety temperature | degC |
| `tw` | Water temperature | degC |
| `tw_p1d_avg` | Water temperature | degC |
| `tw_p1d_max` | Water temperature | degC |
| `tw_p1d_min` | Water temperature | degC |
| `tw_p1m_avg` | Water temperature | degC |
| `tw_p1m_max` | Water temperature | degC |
| `tw_p1m_min` | Water temperature | degC |
| `tw_pt1h_avg` | Water stemperature | degC |
| `tw_pt1h_max` | Water maximum stemperature | degC |
| `tw_pt1h_min` | Water minimum temperature | degC |
| `twater` | Water temperature | degC |
| `twet_pt1m_avg` | Wet-bulb temperature | degC |
| `twp1mavg_p30y_avg` | Meriveden pintalämpötila, 30v. vertailujakson kkkeskiarvojen ka | degC |
| `twp1mmax_p30y_avg` | Meriveden pintalämpötila, 30v. vertailujakson kkmaksimien ka | degC |
| `twp1mmax_p30y_max` | Meriveden pintalämpötila, 30v. vertailujakson ylin kkmaksimi | degC |
| `twp1mmin_p30y_avg` | Meriveden pintalämpötila, 30v. vertailujakson kkminimimien ka | degC |
| `twp1mmin_p30y_min` | Meriveden pintalämpötila, 30v. vertailujakson alin kkminimi | degC |
| `twp_pt1s_avg` | Veden lämpötila | degC |
| `tz_pt1s_acc` | Zero crossing period | s |
| `tz_pt1s_instant` | Zero crossing period | s |
| `uap_pt1s_avg` | Absolute humidity | g/m3 |
| `uep_pt1s_avg` | Vapour pressure | hPa |
| `urp_pt1s_avg` | Mixing ratio | g/kg |
| `uvb_p1d_sum` | Ultraviolet irradiance | index |
| `uvb_pt1h_avg` | Ultraviolet irradiance | index |
| `uvb_pt1h_sum` | Ultraviolet irradiance | index |
| `uvb_pt1m_avg` | Ultraviolet irradiance | index |
| `uvb_u` | Ultraviolet irradiance | index |
| `uvbdiff_pt1m_avg` | Diffuse ultraviolet irradiance | index |
| `uvi_pt1m_instant` | UVI index |  |
| `varo` | Alert of the road condition |  |
| `varo3` | Alert of the road condition |  |
| `varo3_3` | Alert of the road condition |  |
| `varo_2` | Alert of the road condition |  |
| `varo_4` | Alert of the road condition |  |
| `virta` | Electricity |  |
| `vis` | Horizontal visibility | m |
| `vis_2` | Horizontal visibility | m |
| `vis_pt1m_avg` | Horizontal visibility | m |
| `visibility` | Horizontal visibility | m |
| `vrgmass_pt10m_avg` | VRG mass | mm |
| `vsaa` | Present weather (PWD) |  |
| `w1_pt6h_rank` | Past weather (1) |  |
| `w1a_pt1h_rank` | Past weather 1 (auto) |  |
| `w1a_pt6h_rank` | Past weather 1 (auto) |  |
| `w2_pt6h_rank` | Past weather (2) |  |
| `w2a_pt1h_rank` | Past weather 2 (auto) |  |
| `w2a_pt6h_rank` | Past weather 2 (auto) |  |
| `watlev` | Water level | mm |
| `wavehs` | Wave height | m |
| `wawa` | Present weather (auto) |  |
| `wawa2` | Present weather (PWD) |  |
| `wawa2_pt1m_rank` | Present weather (PWD) |  |
| `wawa_pt1h_rank` | Present weather (auto) |  |
| `wawa_pt1m_rank` | Present weather (auto) |  |
| `wcon_pt1h_avg` | Conductivity | S/m |
| `wcon_pt1s_instant` | Conductivity | S/m |
| `wconp_pt1s_avg` | Veden sähkönjohtavuus | mS/cm |
| `wd` | Wind direction | deg |
| `wd045p1m` | Wind distribution, Northeast | % |
| `wd045p1m_p1m_avg` | Wind distribution, Northeast | % |
| `wd045p1y` | Wind distribution, Northeast | % |
| `wd045p1y_p1m_avg` | Wind distribution, Northeast | % |
| `wd090p1m` | Wind distribution, East | % |
| `wd090p1m_p1m_avg` | Wind distribution, East | % |
| `wd090p1y` | Wind distribution, East | % |
| `wd090p1y_p1m_avg` | Wind distribution, East | % |
| `wd135p1m` | Wind distribution, Southeast | % |
| `wd135p1m_p1m_avg` | Wind distribution, Southeast | % |
| `wd135p1y` | Wind distribution, Southeast | % |
| `wd135p1y_p1m_avg` | Wind distribution, Southeast | % |
| `wd180p1m` | Wind distribution, South | % |
| `wd180p1m_p1m_avg` | Wind distribution, South | % |
| `wd180p1y` | Wind distribution, South | % |
| `wd180p1y_p1m_avg` | Wind distribution, South | % |
| `wd225p1m` | Wind distribution, Southwest | % |
| `wd225p1m_p1m_avg` | Wind distribution, Southwest | % |
| `wd225p1y` | Wind distribution, Southwest | % |
| `wd225p1y_p1m_avg` | Wind distribution, Southwest | % |
| `wd270p1m` | Wind distribution, West | % |
| `wd270p1m_p1m_avg` | Wind distribution, West | % |
| `wd270p1y` | Wind distribution, West | % |
| `wd270p1y_p1m_avg` | Wind distribution, West | % |
| `wd315p1m` | Wind distribution, Northwest | % |
| `wd315p1m_p1m_avg` | Wind distribution, Northwest | % |
| `wd315p1y` | Wind distribution, Northwest | % |
| `wd315p1y_p1m_avg` | Wind distribution, Northwest | % |
| `wd360p1m` | Wind distribution, North | % |
| `wd360p1m_p1m_avg` | Wind distribution, North | % |
| `wd360p1y` | Wind distribution, North | % |
| `wd360p1y_p1m_avg` | Wind distribution, North | % |
| `wd_10m_avg` | Wind direction | deg |
| `wd_10min` | Wind direction | deg |
| `wd_2m_avg` | Wind direction | deg |
| `wd_pt10m_avg` | Wind direction | deg |
| `wd_pt10m_std` | Deviation of wind direction | deg |
| `wd_pt1h_avg` | Wind direction | deg |
| `wd_pt1m_avg` | Wind direction | deg |
| `wd_pt2m_avg` | Wind direction | deg |
| `wd_ptsm_avg` | Wind direction | deg |
| `wda_pt10m_avg` | Toispuoleinen tuulen suunta | deg |
| `wda_pt2m_avg` | Toispuoleinen tuulen suunta | deg |
| `wdc_pt10m_avg` | Tuulen suunta,jatkuva | deg |
| `wdp_pt1s_avg` | Wind direction | deg |
| `weton_pt1m_instant` | Surface humidity |  |
| `wfl_pt1m_avg` | Virtaama | m3/s |
| `wg` | Gust speed | m/s |
| `wg_10m_max` | Gust speed | m/s |
| `wg_10min` | Gust speed | m/s |
| `wg_2m_max` | Gust speed | m/s |
| `wg_pt10m_max` | Gust speed | m/s |
| `wg_pt1h_max` | Greatest gust speed | m/s |
| `wg_pt2m_max` | Gust speed | m/s |
| `wga_pt10m_max` | Toispuoleinen puuskanopeus | m/s |
| `wga_pt2m_max` | Toispuoleinen puuskanopeus | m/s |
| `wgenl_pt1h_avg` | Generator current | A |
| `wh_pt1m_instant` | Sea roll |  |
| `wh_pt1s_acc` | Wave height | m |
| `wh_pt1s_instant` | Wave height | m |
| `whd_pt1s_acc` | Direction of waves | deg |
| `whd_pt1s_instant` | Direction of waves | deg |
| `whdd` | Deviation of wave direction | deg |
| `whdd_pt1s_acc` | Deviation of wave direction | deg |
| `whdd_pt1s_instant` | Deviation of wave direction | deg |
| `wheat_pt1m_avg` | Wind sensor heating | A |
| `winddirection` | Wind direction | deg |
| `windgust` | Gust speed | m/s |
| `windspeedms` | Wind speed | m/s |
| `wlev_p1m_avg` | Water level | mm |
| `wlev_p1m_max` | Water maximum level | mm |
| `wlev_p1m_min` | Water minimum level | mm |
| `wlev_p1y_avg` | Water level | mm |
| `wlev_p1y_max` | Water maximum level | mm |
| `wlev_p1y_min` | Water minimum level | mm |
| `wlev_pt1h_max` | Water maximum level | mm |
| `wlev_pt1h_min` | Water minimum level | mm |
| `wlev_pt1s_instant` | Water level | mm |
| `wlev_pt24h_max` | Water maximum level | mm |
| `wlev_pt24h_min` | Water minimum level | mm |
| `wlevc_pt1s_instant` | Control water level | mm |
| `wlevkm1_pt1s_instant` | KM1 control | mm |
| `wlevkm2_pt1s_instant` | KM2 control | mm |
| `wlevn2kp1mavg_p30y_avg` | Vedenkorkeuden 30v vertailujakson kuukausikeskiarvo, N2000 | mm |
| `wlevn2kp1mavg_p30y_max` | Vedenkorkeuden 30v vertailujakson suurin kk-keskiarvo, N2000 | mm |
| `wlevn2kp1mavg_p30y_min` | Vedenkorkeuden 30v vertailujakson pienin kk-keskiarvo, N2000 | mm |
| `wlevn2kp1mmax_p30y_avg` | Vedenkorkeuden 30v vertailujakson kk-maksimien keskiarvo, N2000 | mm |
| `wlevn2kp1mmax_p30y_max` | Vedenkorkeuden 30v vertailujakson suurin kuukausimaksimi, N2000 | mm |
| `wlevn2kp1mmin_p30y_avg` | Vedenkorkeuden 30v vertailujakson kk-minimien keskiarvo, N2000 | mm |
| `wlevn2kp1mmin_p30y_min` | Vedenkorkeuden 30v vertailujakson pienin kuukausiminimi, N2000 | mm |
| `wlevn2kp1yavg_p30y_avg` | Vedenkorkeuden 30v vertailujakson keskiarvo, N2000 | mm |
| `wlevn2kp1yavg_p30y_max` | Vedenkorkeuden 30v vertailujakson suurin vuosikeskiarvo, N2000 | mm |
| `wlevn2kp1yavg_p30y_min` | Vedenkorkeuden 30v vertailujakson pienin vuosikeskiarvo, N2000 | mm |
| `wlevn2kp1ymax_p30y_avg` | Vedenkorkeuden 30v vertailujakson vuosimaksimien keskiarvo, N2K | mm |
| `wlevn2kp1ymax_p30y_max` | Vedenkorkeuden 30v vertailujakson suurin vuosimaksimi, N2000 | mm |
| `wlevn2kp1ymin_p30y_avg` | Vedenkorkeuden 30v vertailujakson vuosiminimien keskiarvo, N2000 | mm |
| `wlevn2kp1ymin_p30y_min` | Vedenkorkeuden 30v vertailujakson pienin vuosiminimi, N2000 | mm |
| `wlevp1h_p30y_p001` | Vedenkorkeuden 30v vertailujakson prosenttipiste 0.1 | mm |
| `wlevp1h_p30y_p010` | Vedenkorkeuden 30v vertailujakson prosenttipiste 1 | mm |
| `wlevp1h_p30y_p050` | Vedenkorkeuden 30v vertailujakson prosenttipiste 5 | mm |
| `wlevp1h_p30y_p250` | Vedenkorkeuden 30v vertailujakson prosenttipiste 25 | mm |
| `wlevp1h_p30y_p500` | Vedenkorkeuden 30v vertailujakson prosenttipiste 50 | mm |
| `wlevp1h_p30y_p750` | Vedenkorkeuden 30v vertailujakson prosenttipiste 75 | mm |
| `wlevp1h_p30y_p950` | Vedenkorkeuden 30v vertailujakson prosenttipiste 95 | mm |
| `wlevp1h_p30y_p990` | Vedenkorkeuden 30v vertailujakson prosenttipiste 99 | mm |
| `wlevp1h_p30y_p999` | Vedenkorkeuden 30v vertailujakson prosenttipiste 99.9 | mm |
| `wlevp1hp1m_p30y_p001` | Vedenkorkeuden 30v vertailujakson kk prosenttipiste 0.1 | mm |
| `wlevp1hp1m_p30y_p010` | Vedenkorkeuden 30v vertailujakson kk prosenttipiste 1 | mm |
| `wlevp1hp1m_p30y_p050` | Vedenkorkeuden 30v vertailujakson kk prosenttipiste 5 | mm |
| `wlevp1hp1m_p30y_p250` | Vedenkorkeuden 30v vertailujakson kk prosenttipiste 25 | mm |
| `wlevp1hp1m_p30y_p500` | Vedenkorkeuden 30v vertailujakson kk prosenttipiste 50 | mm |
| `wlevp1hp1m_p30y_p750` | Vedenkorkeuden 30v vertailujakson kk prosenttipiste 75 | mm |
| `wlevp1hp1m_p30y_p950` | Vedenkorkeuden 30v vertailujakson kk prosenttipiste 95 | mm |
| `wlevp1hp1m_p30y_p990` | Vedenkorkeuden 30v vertailujakson kk prosenttipiste 99 | mm |
| `wlevp1hp1m_p30y_p999` | Vedenkorkeuden 30v vertailujakson kk prosenttipiste 99.9 | mm |
| `wlevp1mavg_p30y_avg` | Vedenkorkeuden 30v vertailujakson kuukausikeskiarvo, MW | mm |
| `wlevp1mavg_p30y_max` | Vedenkorkeuden 30v vertailujakson suurin kuukausikeskiarvo, MW | mm |
| `wlevp1mavg_p30y_min` | Vedenkorkeuden 30v vertailujakson pienin kuukausikeskiarvo, MW | mm |
| `wlevp1mmax_p30y_avg` | Vedenkorkeuden 30v vertailujakson kk-maksimien keskiarvo, MW | mm |
| `wlevp1mmax_p30y_max` | Vedenkorkeuden 30v vertailujakson suurin kuukausimaksimi, MW | mm |
| `wlevp1mmin_p30y_avg` | Vedenkorkeuden 30v vertailujakson kuukausiminimien keskiarvo, MW | mm |
| `wlevp1mmin_p30y_min` | Vedenkorkeuden 30v vertailujakson pienin kuukausiminimi, MW | mm |
| `wlevp1yavg_p30y_avg` | Vedenkorkeuden 30v vertailujakson keskiarvo, MW | mm |
| `wlevp1yavg_p30y_max` | Vedenkorkeuden 30v vertailujakson suurin vuosikeskiarvo, MW | mm |
| `wlevp1yavg_p30y_min` | Vedenkorkeuden 30v vertailujakson pienin vuosikeskiarvo, MW | mm |
| `wlevp1ymax_p30y_avg` | Vedenkorkeuden 30v vertailujakson vuosimaksimien keskiarvo, MW | mm |
| `wlevp1ymax_p30y_max` | Vedenkorkeuden 30v vertailujakson suurin vuosimaksimi, MW | mm |
| `wlevp1ymin_p30y_avg` | Vedenkorkeuden 30v vertailujakson vuosiminimien keskiarvo, MW | mm |
| `wlevp1ymin_p30y_min` | Vedenkorkeuden 30v vertailujakson pienin vuosiminimi, MW | mm |
| `wlevp_pt1s_instant` | Punttikorkeus | mm |
| `wliv_pt1s_instant` | Water level | mm |
| `wo2p_pt1s_avg` | Veden happipitoisuus | ml/l |
| `wo2pctp_pt1s_avg` | Veden happipitoisuus | % |
| `wpre_pt1h_avg` | Water pressure | dbar |
| `wpre_pt1s_instant` | Water pressure | dbar |
| `wprep_pt1s_avg` | Vedenpaine | dba |
| `ws` | Wind speed | m/s |
| `ws045p1m` | Wind speed, Northeast | m/s |
| `ws045p1m_p1m_avg` | Wind speed, Northeast | m/s |
| `ws045p1y` | Wind speed, Northeast | m/s |
| `ws045p1y_p1y_avg` | Wind speed, Northeast | m/s |
| `ws090p1m` | Wind speed, East | m/s |
| `ws090p1m_p1m_avg` | Wind speed, East | m/s |
| `ws090p1y` | Wind speed, East | m/s |
| `ws090p1y_p1y_avg` | Wind speed, East | m/s |
| `ws0p1m` | Calm normal | % |
| `ws0p1m_p1m_avg` | Calm normal | % |
| `ws0p1y` | Calm normal | % |
| `ws0p1y_p1y_avg` | Calm normal | % |
| `ws135p1m` | Wind speed, Southeast | m/s |
| `ws135p1m_p1m_avg` | Wind speed, Southeast | m/s |
| `ws135p1y` | Wind speed, Southeast | m/s |
| `ws135p1y_p1y_avg` | Wind speed, Southeast | m/s |
| `ws180p1m` | Wind speed, South | m/s |
| `ws180p1m_p1m_avg` | Wind speed, South | m/s |
| `ws180p1y` | Wind speed, South | m/s |
| `ws180p1y_p1y_avg` | Wind speed, South | m/s |
| `ws225p1m` | Wind speed, Southwest | m/s |
| `ws225p1m_p1m_avg` | Wind speed, Southwest | m/s |
| `ws225p1y` | Wind speed, Southwest | m/s |
| `ws225p1y_p1y_avg` | Wind speed, Southwest | m/s |
| `ws270p1m` | Wind speed, West | m/s |
| `ws270p1m_p1m_avg` | Wind speed, West | m/s |
| `ws270p1y` | Wind speed, West | m/s |
| `ws270p1y_p1y_avg` | Wind speed, West | m/s |
| `ws315p1m` | Wind speed, Northwest | m/s |
| `ws315p1m_p1m_avg` | Wind speed, Northwest | m/s |
| `ws315p1y` | Wind speed, Northwest | m/s |
| `ws315p1y_p1y_avg` | Wind speed, Northwest | m/s |
| `ws360p1m` | Wind speed, North | m/s |
| `ws360p1m_p1m_avg` | Wind speed, North | m/s |
| `ws360p1y` | Wind speed, North | m/s |
| `ws360p1y_p1y_avg` | Wind speed, North | m/s |
| `ws_10m_avg` | Wind speed | m/s |
| `ws_10min` | Wind speed | m/s |
| `ws_2m_avg` | Wind speed | m/s |
| `ws_pt10m_avg` | Wind speed | m/s |
| `ws_pt10m_std` | Deviation of wind speed | m/s |
| `ws_pt1h_avg` | Wind speed | m/s |
| `ws_pt1h_max` | Maximum wind speed | m/s |
| `ws_pt1h_min` | Minimum wind speed | m/s |
| `ws_pt1m_avg` | Wind speed | m/s |
| `ws_pt2m_avg` | Wind speed | m/s |
| `ws_pt3h_max` | Greatest Wind speed | m/s |
| `ws_pt3m_avg` | Wind speed | m/s |
| `wsa_pt10m_avg` | Toispuoleinen tuulen nopeus | m/s |
| `wsa_pt2m_avg` | Toispuoleinen tuulen nopeus, 2 minuutin keskiarvo | m/s |
| `wsal_pt1h_avg` | Salinity | PSS-78 |
| `wsal_pt1m_instant` | Salinity | PSS-78 |
| `wsalp_pt1s_avg` | Veden suolaisuus | PSU |
| `wsc_pt10m_avg` | Tuulen nopeus,jatkuva | m/s |
| `wsigp_pt1s_avg` | Veden tiheys | kg/m3sigmatheta |
| `wsp1m` | Wind speed | m/s |
| `wsp1m_p1m_avg` | Wind speed | m/s |
| `wsp1y` | Wind speed | m/s |
| `wsp1y_p1y_avg` | Wind speed | m/s |
| `wsp_pt1s_avg` | Wind speed | m/s |
| `wspd` | Wind speed | m/s |
| `wst_pt3h_rank` | Time of greatest wind speed |  |
| `wsym_pt1m_instant` | Weather symbol |  |
| `wtp` | Modal period | s |
| `wtp_pt1s_acc` | Modal period | s |
| `wtp_pt1s_instant` | Modal period | s |
| `ww_aws` | Present weather (auto) |  |
| `ww_comb` | Present weather (auto) |  |
| `ww_pt1m_rank` | Present weather |  |
