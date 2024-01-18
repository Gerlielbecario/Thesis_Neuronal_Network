#Librerias

import numpy as np
import os
from scipy.interpolate import interp2d

#--------------------------------------

#Extraccion de array de latitudes y longitudes de un archivo gsmap

#La carpeta donde se almacenan los archivos de gsmap
folder_gsmap = '/home/fernando.huaranca/datosmunin3/Gsmap_24hs'

#Un archivo random
file_gsmap = 'Gsmap_R0.1_24hs_2000-01-04.npz'

#Path
path_gsmap = os.path.join(folder_gsmap,file_gsmap)

#Abro archivo

npz_gsmap = np.load(path_gsmap)

#Extraigo mis variables de interes
#Al extraerlo se debe hacer una correcion en los datos esto debido a que 


latitudes_gsmap = npz_gsmap['latitudes']
longitudes_gsmap = npz_gsmap['longitudes']

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

        #Path del archivo del bucle
        path = os.path.join(folder,file)

        #Porcentaje
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
        nueva_pp = f(longitudes_gsmap, latitudes_gsmap)

        #Ya el archivo se llama file.npz por eso no se agrega un .npz al final

        out_path = f'/home/fernando.huaranca/datosmunin3/GFS_24hs_interpolado_a_gsmap/{file}'

        #Generas un .npz con el mismo nombre que tenian antes
        np.savez(out_path,pp_daily = nueva_pp, latitudes = latitudes_gsmap,longitudes = longitudes_gsmap)

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
