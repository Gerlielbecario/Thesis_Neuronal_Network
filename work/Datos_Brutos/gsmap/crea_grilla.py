#Cargamos librerias
import numpy as np
import os 
import xarray as xr

#Ruta de algun archivo .grib2 de GFS
path_archivo = '/home/fernando.huaranca/datos/DATOS_REFORECAST/apcp_sfc/apcp_sfc_2000010200_c00.grib2'

ds = xr.open_dataset(path_archivo)

lat = ds.latitude.values
lon = ds.longitude.values

#Latitudes y longitudes (box)
lat_north = 15
lat_south = -59
lon_east = 330
lon_west = 260

#Recorta la seccion de sudamerica o la que se desee
#LATITUDES

lat_index = np.where((lat <=lat_north) & (lat >= lat_south))[0]


lat = lat[lat_index]

#LONGITUDES
lon_index = np.where((lon >= lon_west) & (lon <= lon_east))[0]

lon = lon[lon_index]

np.savez('grid.npz',latitudes_gfs =lat,longitudes_gfs=lon)