#Este es un codigo que realiza un subset de los datos ya interpolados de GFS y Gsmap
#Realiza un subset de una región tropical y una región no tropical para evaluar el ETS
#de cada una de las regiones, para distintos umbrales. 
#De esta manera el output son dos listas o arrays, uno para cada region , con el largo
#de la cantidad de umbrales que se le pidio, y en cada elemento el ETS(umbral). 


#Librerias
from periodo_en_comun import devuelve_periodo_comun
from funcion_ets import ETS
import numpy as np
import os
import pandas as pd
import glob
from matriz_confusion_periodo import matriz_confusion_periodo

#Paths de archivos de las carpetas
gfs_lista = glob.glob('/home/fernando.huaranca/datosmunin/GFS_24hs/*.npz')
gsmap_lista = glob.glob('/home/fernando.huaranca/datosmunin/Gsmap_24hs/*.npz')

#Archivos comunes entre los dos periodos. 
#En los testeos hay un archivo que no funciona por un error proveniente desde un comienzo, 
#un error de los datos de gfs de 1 dia. 
Files = devuelve_periodo_comun(gfs_lista,gsmap_lista)

#----------------------------------------------------------------------------------------

#Variable booleana para que la primera CM 
inicio = True

#Lista donde se almacenan los archivos que fallaron
fallidos = []

#Lista de umbrales (Aca podes ir modificando)
Umbrales = [0.01,0.5,1,3,5,10,15,20,25,50,75,100,120,130,140,150,160,170,180,190,200,220,250,270,300,330,350,390,400,450,500,550,600,650,700,750,800,850,900,1000,1100,1200]

#Carpetas donde se almacenan los datos de diferentes fuentes
folder_gfs = '/home/fernando.huaranca/datosmunin/GFS_24hs'
folder_gsmap = '/home/fernando.huaranca/datosmunin/Gsmap_24hs'

#-----Seleccionamos Areas------------------

#Area no tropical o de Clima de latitudes medias
lat_north_med = -20
lat_south_med =  -45
long_west_med = 285
long_east_med = 320

#Area Tropical o de Clima de latitudes tropicales
lat_north_trop = 7
lat_south_trop = -18
long_west_trop = 285
long_east_trop = 320


#------------------------------------------------------------------------------
#Extraemos las latitudes y longitudes de un archivo solo y luego usamos eso para
#todos los demas archivos

#Archivo unico
my_path_unico = '/home/fernando.huaranca/datosmunin/Gsmap_24hs/Gsmap_R0.25_24hs_2000-01-01.npz'
my_file_unico = np.load(my_path_unico)

#Extraemos las latitudes y longitudes de 1 archivo solo
latitudes = my_file_unico['latitudes']
longitudes = my_file_unico['longitudes']

#Definimos los indices y regiones 

#AREA DE CLIMA TROPICAL en LATITUDES ALTAS-------------------------
lat_index_trop = np.where((latitudes >= lat_south_trop) & (latitudes<=lat_north_trop))[0]
LAT_trop = latitudes[lat_index_trop] 

long_index_trop = np.where((longitudes >= long_west_trop) & (longitudes<=long_east_trop))[0]
LONG_trop = longitudes[long_index_trop]


#AREA DE CLIMA DE LATITUDES MEDIAS---------------
lat_index_med = np.where((latitudes >= lat_south_med) & (latitudes<=lat_north_med))[0]
LAT_med = latitudes[lat_index_med] 

long_index_med = np.where((longitudes >= long_west_med) & (longitudes<=long_east_med))[0]
LONG_med = longitudes[long_index_med]

#----------------------------------------------------------------------------------

#Para calcular porcentajes
k = 0 

#Cantidad de fechas 
total = len(Files)

#-------------------------------------------------------------------------

#Bucle aca le hace esto a cada archivo
for file in Files:
   
   #-----Porcentaje----------------
   k = k +1
   porcentaje = (k/total)*100
   print(file,'  ',porcentaje,' %')

   #----Paths------------------------
   #Cargamos los archivos 
   path_modelo = os.path.join(folder_gfs,f'GFS_R0.25_24hs_{file}.npz')
   path_observacion = os.path.join(folder_gsmap,f'Gsmap_R0.25_24hs_{file}.npz')

   #---Abrir con numpy los archivos-------------
   #Cargamos los archivos
   file_modelo = np.load(path_modelo)
   file_observacion = np.load(path_observacion)

   #---Cargamos las precipitaciones-----------------
   #Precipitaciones del GFS Modelo
   pp_modelo = file_modelo['pp_daily']
   
   #Precipitaciones del Gsmap Observaciones
   pp_observacion= file_observacion['pp_daily']

   
      
   #---------Realizamos el SUBSET-------------------------


   
   try:

      #----MODELO----------------------------------

      #Definimos la Matriz de Clima_Tropical con GFS
      CLIMA_TROP_gfs = pp_modelo[lat_index_trop.min():lat_index_trop.max()+1,long_index_trop.min():long_index_trop.max()+1]

      #Definimos la Matriz de Clima Tropical con Gsmap
      CLIMA_TROP_gsmap = pp_observacion[lat_index_trop.min():lat_index_trop.max()+1,long_index_trop.min():long_index_trop.max()+1]

      #----OBSERVACION----------------
         
      #Definimos la Matriz de Clima_Tropical con GFS
      CLIMA_MEDIOS_gfs = pp_modelo[lat_index_med.min():lat_index_med.max()+1,long_index_med.min():long_index_med.max()+1]

      #Definimos la Matriz de Clima Tropical con Gsmap
      CLIMA_MEDIOS_gsmap = pp_observacion[lat_index_med.min():lat_index_med.max()+1,long_index_med.min():long_index_med.max()+1]

      #-------------------------------------------------------------   
      if inicio:

         #Calculamos la matriz de confusion de nuestro primera fecha
         cm_tropical = matriz_confusion_periodo(CLIMA_TROP_gfs,CLIMA_TROP_gsmap,Umbrales)
         cm_medios = matriz_confusion_periodo(CLIMA_MEDIOS_gfs,CLIMA_MEDIOS_gsmap,Umbrales)
         inicio = False

      else:
         #Matriz de confusion y vamos sumando
         cm_tropical = matriz_confusion_periodo(CLIMA_TROP_gfs,CLIMA_TROP_gsmap,Umbrales) + cm_tropical
      
         cm_medios = matriz_confusion_periodo(CLIMA_MEDIOS_gfs,CLIMA_MEDIOS_gsmap,Umbrales) + cm_medios
      
   except Exception as e:

      #Muestro mensaje por pantalla
      print(f'Error al procesar el archivo {file}: {str(e)}')

      #Almacena los archivos fallidos en una lista
      fallidos.append(file)
   

#Calculo de ETS

ets_medios = ETS(Umbrales,cm_medios)
ets_tropicales = ETS(Umbrales,cm_tropical)


#Outputs---------------

df_fallados = pd.DataFrame({'Archivos':fallidos})
df_fallados.to_csv('/home/fernando.huaranca/datosmunin/salida_ets/fallados.csv',index=True)


#Aca va el outpath de mis npz. Luego cuando plotees tenes que saber donde esta lo que pltoeas
np.savez('/home/fernando.huaranca/datosmunin/salida_ets/ets_medios.npz',ETS = ets_medios)
np.savez('/home/fernando.huaranca/datosmunin/salida_ets/ets_tropical.npz',ETS = ets_tropicales)


print('El calculo ha sido realizado para ',len(Umbrales), 'umbrales')
print('Los Umbrales fueron: ',Umbrales)

print('PROCESO COMPLETADO!')