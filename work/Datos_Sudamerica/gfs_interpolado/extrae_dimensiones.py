#Este es un codigo de python que extrae la latitud y longitud de un archivo
#.npz y devuelve las latitudes y longitudes del conjunto2 para interpolar
#luego

#-----

import numpy as np
import os



folder = '/home/fernando.huaranca/datosmunin3/Gsmap_24hs'
file = '01-01-2000.npz'

path = os.path.join(folder,file)

#Abro archivo

datos = np.load(path)

#Extraigo mis variables de interes

lat = datos['latitudes']
lon = datos['longitudes']

#Almacena los datos en un .npz

out_path = '/home/fernando.huaranca/test_forecast/interpolacion/shape_a_interpolar.npz'
np.savez(out_path, nuevas_latitudes = lat,nuevas_longitudes = lon)




