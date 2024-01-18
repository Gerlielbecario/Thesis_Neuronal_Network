#Este es un codigo que lee los archivos del CONJUNTO DE DATOS 1
#y los interpola de manera que tengan las mismas dimensiones que
#el conjunto de datos2. Generando un nuevo conjunto de datos que
#llamremos CONJUNTO DE DATOS 3

#Librerias

import numpy as np
import os
from scipy.interpolate import interp2d

#Primero cargamos los arrays de latitudes y longitudes que utilizaremos
#Para realizar la interpolacion. Nuestra nueva grilla.

folder_grilla = '/home/fernando.huaranca/test_forecast/interpolacion'
file_grilla = 'shape_a_interpolar.npz'
path_grilla = os.path.join(folder_grilla,file_grilla)

#Extraemos los arrays del archivo
grilla = np.load(path_grilla)

nuevas_latitudes = grilla['nuevas_latitudes']
nuevas_longitudes = grilla['nuevas_longitudes']

print('Finalizo la carga de la grilla')

#--------------------------------------


#Cargo los archivos de GFS_24 (QUE NO ESTAN INTERPOLADOS)

folder = '/home/fernando.huaranca/datosmunin3/GFS_24hs'
FileS = os.listdir(folder)


#Lista para almacenar archivos erroneos

fallidos = []

#Porcentaje
i = 0
total = len(FileS)

#-------------------------------------------------
for file in FileS:

    try:

        #Cargo el file
        print('Cargando: ',file)
        path = os.path.join(folder,file)

        i = i + 1 
        porcentaje = (i/total) * 100


        #Abro archivo
        print('Leyendo: ',file)
        datos = np.load(path)

        print('Comienza extraccion de variables ')

        #Extraigo el array que quiero interpolar
        pp = datos['pp_daily']
        lat = datos['latitudes']
        lon = datos['longitudes']

        # Crear una función de interpolación lineal
        #O sea creas una f(x,y) en base a tus datos
        f = interp2d(lon, lat, pp, kind='linear')

        # Evaluar la función de interpolación en la nueva grilla
        #f(nuevas_longitudes,nuevas_latitudes)
        nueva_pp = f(nuevas_longitudes, nuevas_latitudes)

        #Ya el archivo se llama file.npz por eso no se agrega un .npz al final

        out_path = f'/home/fernando.huaranca/datosmunin3/GFS_24hs_interpolado_a_gsmap/{file}'

        #Generas un .npz con el mismo nombre que tenian antes
        np.savez(out_path,pp_daily = nueva_pp, latitudes = nuevas_latitudes,longitudes = nuevas_longitudes)

        f = 0
        nueva_pp = 0

    except Exception as e:
        print(f'Error al procesar el archivo {file}: {str(e)}')
        fallidos.append(file)
        # Aquí puedes almacenar el nombre del archivo con errores en un registro si es necesario.

    print('SE HA COMPLETADO UN: ',porcentaje,'%')
    print('Cantidad de errores: ',len(fallidos))

    


print('Proceso finalizado')

print('Lista de Archivos fallidos')
print('Cantidad: ',len(fallidos))
print(fallidos)
