# Thesis_Neuronal_Network
All the code that I am using for my MSc thesis

El esquema de trabajo es el siguiente:

## Índice 

1. [Datos Brutos](#Datos-Brutos)
   - [gfs](#gfs)
   - [gsmap](#gsmap)

2. [Datos Sudamerica](#Datos-Sudamerica)


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
    
    2. test_gsmap.py : Es un codigo que permite graficar estos archivos utilizando funciones de
    gsmap_tool.py
    
    3. auto_MATRICES_DIARIAS.py: Es un codigo que usando funciones de gsmap_tool permite realizar
    el subset de todos los datos brutos. Se eligio sudamerica, pero podria ser otra region.

   ### [Datos Sudamerica](work/Datos_Sudamerica)

    1. grafica_npz.py : Este es un codigo que devuelve que se halla dentro del archivo a su vez permite seleccionar una seccion para graficar
   dentro de la delimitada. Devuelve las dimensiones del archivo original y el graficado.

   #### [gfs](work/Datos_Sudamerica/gfs_interpolado)

   En esta carpeta se hallan codigos y lo referido a la interpolacion de archivos gfs

   



