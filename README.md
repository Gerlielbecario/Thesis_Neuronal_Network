# Thesis_Neuronal_Network
All the code that I am using for my MSc thesis

El esquema de trabajo es el siguiente:

1. [Datos Brutos](work/Datos_Brutos)


Dentro de esta carpeta todo lo realizado es con los datos brutos. Tanto analisis como subsets.

Tenemos 2 carpetas:

[gfs](work/Datos_Brutos/gfs): Los datos de gfs tienen una resolucion de 0.25º de grilla y 
son pronosticos para los proximos 10 dias. O sea que cada archivo tiene 10 pronosticos. Son archivos de tipo grib. Los mismos no se encuentran en esta carpeta pero todo lo referido a ellos si.

    1. [extrae_pronostico.py](work/Datos_Brutos/gfs/extrae_pronostico.py) : Es un codigo que se encarga de realizar un subset de los datos brutos. 

[gsmap](work/Datos_Brutos/gsmap): Los datos de gsmap son de tipo dat.gz binario y necesitan ser interpretados. Los mismos no se hayan dentro de esta carpeta. Tienen una resolucion de 0.1º.

