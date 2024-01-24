# Thesis_Neuronal_Network
All the code that I am using for my MSc thesis

El esquema de trabajo es el siguiente:

## Índice 

1. [Datos Brutos](#Datos-Brutos)
   - [gfs](#gfs)
   - [gsmap](#gsmap)

2. [Datos Sudamerica](#Datos-Sudamerica)
   - [salidas](#gfs-interpolado)



### Datos Brutos
Dentro de esta carpeta todo lo realizado es con los datos brutos. Tanto analisis como subsets.

Tenemos 2 carpetas:


#### [gfs](work/Datos_Brutos/gfs)
Los datos de gfs tienen una resolucion de 0.25º de grilla y son pronosticos para los proximos 10 dias. O sea que cada archivo tiene 10 pronosticos. Son archivos de tipo grib. Los mismos no se encuentran en esta carpeta pero todo lo referido a ellos si.

      1. extrae_pronostico.py : Es un codigo que se encarga de realizar un subset de los datos brutos. 

#### [gsmap](work/Datos_Brutos/gsmap)

Los datos de gsmap son de tipo dat.gz binario y necesitan ser interpretados. Los mismos no se hayan dentro de esta carpeta. Tienen una resolucion de 0.1º.

      1. gsmap_tool.py : Es un codigo que contiene funciones para operar con estos archivos binarios.
      Poder leerlos y realizar subsets. Solo contiene las funciones. 
    
      2. test_gsmap.py : Es un codigo que permite graficar estos archivos utilizando funciones de gsmap_tool.py
    
      3. crea_grilla.py : Es un codigo que lee un archivo GFS que devuelve un npz con los arrays de latitudes y 
      longitudes para la seccion de sudamerica. En este caso:
      
      Latitudes y longitudes (box)
      lat_north = 15
      lat_south = -59
      lon_east = 330
      lon_west = 260

      4. interp_gsmap_SA.py : Es un codigo que realiza el subset de los datos brutos de Gsmap. A su vez los
      multiplica por 24 de manera de tener datos diarios en unidades de mm/24hs. Y los interpola a las 
      dimensiones de 0.25. Usando el archivo creado con crea_grilla.py

   ### [Datos Sudamerica](work/Datos_Sudamerica)

      1. grafica_npz.py : Este es un codigo que devuelve que se halla dentro del archivo a su vez permite seleccionar una seccion para graficar
      dentro de la delimitada. Devuelve las dimensiones del archivo original y el graficado.

      #### [salidas](work/Datos_Sudamerica/salidas)



   
   



