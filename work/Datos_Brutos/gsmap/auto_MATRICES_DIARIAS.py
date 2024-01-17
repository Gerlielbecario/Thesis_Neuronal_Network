#este es el codigo para ejecutar que me devolvera el conjunto de datos2

#Este es un codigo al que se le entrega una lista de archivos en formato
#dat.gz binarios del satelite GsMAP JAXA y entrega en una ruta de salida
#archivos en formato .npz que contienen la siguiente informacion

#Un array con:
#------------ *Un array bidimensional con la precipitacion
#------------ *Un array con los valores de latitudes
#------------ *Un array con los valores de longitudes
#------------ *Un array con la fecha del archivo

#--------Librerias---------------------

#Librerias
import gsmap_tool as gsmap 
import os
from datetime import datetime
import numpy as np
import pandas as pd
import glob

#-----------Cargar archivos------------------------

#Carpeta
#folder = '/home/fernando.huaranca/datos/Datos_GSMAP/testeo_septiembre_fallados'

folder = '/home/fernando.huaranca/datos/Datos_GSMAP/daily_G_v8'
#Lista de archivos dentro de la carpeta
FileS = glob.glob(folder+'/*dat.gz')

print('Lista de archivos cargada')
#----------Limites--para-el-subset--------------------------------

#Region de sudamerica

ini_lon=260.0
end_lon=330.0
ini_lat=-65.0
end_lat=15.0


#Lista para almacenar archivos erroneos

fallidos = []

#Porcentaje
i = 0
total = len(FileS)
#------------------Bucle para procesar cada archivo---------------------

for file in FileS:

    #Ruta del archivo

    #print('Leyendo ruta:',file)
   


    #------------Subset-del-archivo----------------------------------

    print('Leyendo archivo: ',file)

    i = i + 1 
    porcentaje = (i/total) * 100  

    try:

        #Utilizamos la funcion para realizar un subset
        var = gsmap.read_gsmap_subset(file , ini_lon , end_lon , ini_lat , end_lat )
        
        print(f'Subset de {file} finalizado')

        #----------Extraemos-variables-de-interes--------------------

        print(f'Se inicia la extraccion de variables de interes')
        
        #Matriz bidimensional de precipitaciones diarias. Redondeamos
        #Dado que tenemos mm/h en nuestros datos lo multiplicamos por 24
        pp = np.round(var[0],3) * 24

        #Array con longitudes
        lon = var[1]

        #Array con latitudes
        lat = var[2]

        #Extraer la fecha del file
        fecha_str = file.split('.')[2]
        fecha_datetime = datetime.strptime(fecha_str, '%Y%m%d')

        # Formatear la fecha como YYYY-MM-DD
        name_file = fecha_datetime.strftime('%Y-%m-%d')


        print(f'Se extrajo las variables de {file} correctamente')

    
        #-----------Output--------------------------

        print(f'Se inicia la creacion de {name_file}.npz')

        #Ruta completa del archivo donde guardar los datos
        out_path = f'/home/fernando.huaranca/datosmunin3/Gsmap_24hs/Gsmap_R0.1_24hs_{name_file}.npz'

        # Guardar los arreglos en el archivo

        np.savez(out_path,pp_daily = pp, latitudes = lat,longitudes = lon,name = name_file)

        print(f'Archivo {name_file} creado y guardado correctamente')

    except Exception as e:
        print(f'Error al procesar el archivo {file}: {str(e)}')
        fallidos.append(file)

    print('SE HA COMPLETADO UN: ',porcentaje,'%')

print('Termino el proceso')



print('Lista de Archivos fallidos')
print('Cantidad: ',len(fallidos))
print(fallidos)

#Se genera un csv lista con los archivos fallidos
# Crea un DataFrame de Pandas con una sola columna
df = pd.DataFrame({'Archivos': fallidos})

# Guarda el DataFrame en un archivo CSV
nombre_archivo = "/home/fernando.huaranca/datosmunin3/archivos_fallados.csv"
df.to_csv(nombre_archivo, index=False)







