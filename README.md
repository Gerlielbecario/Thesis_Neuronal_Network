# Thesis_Neuronal_Network
All the code that I am using for my MSc thesis

El esquema de trabajo es el siguiente:

## Índice 

1. [Datos Brutos](#Datos-Brutos)
   - [gfs](#gfs)
   - [gsmap](#gsmap)

2. [Datos Sudamerica](#Datos-Sudamerica)
   - [analisis](#analisis)
   - [salidas](#salidas)



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

   ### [Datos Sudamerica](work/2-Datos_Sudamerica)

      1. grafica_npz.py : Este es un codigo que devuelve que se halla dentro del archivo a su vez permite seleccionar una seccion para graficar
      dentro de la delimitada. Devuelve las dimensiones del archivo original y el graficado.

      2. explora_datos.ipynb :Es un notebook con una clase que permite realizar graficos em formato de tabla de nuestros datos rapidamente

      3. subset.ipynb: Es un notebook que permite realizar el subset de los datos de la region de sudamerica. De manera de obtener npz mas 
      pequeños. En este caso se tomo:

      #Region para el subset
      lat_north = -10
      lat_south = -20
      lon_east = 310
      lon_west = 300

      Dando un shape de 41x41

   #### [salidas](work/2-Datos_Sudamerica/salidas)

   Esta es una carpeta donde se almacenan las salidas del codigo explora_datos

   #### [analisis](work/2-Datos_Sudamerica/analisis)

   Esta es una carpeta donde se almacenan codigos relacionados al analisis de Datos de Sudamerica

      1. periodo_en_comun.py : Es un codigo al que se le da dos listas. Estas contienen los paths de los archivos de cada carpeta.
      Similar al os.listdir(). El codigo se encarga de encontrar los archivos en comun entre los dos periodos en las listas.

      2. matriz_confusion_periodo.py : Es un codigo que se encarga de realizar la matriz de confusión para los umbrales que se pidan.
      El formato en que se devuelven la matriz es: En filas lo observado en columnas el modelo.
         C o.o = TP
         C o.1 = FN
         C 1.0 = FP
         C 1.1 = TN

      Al aplicar un reshapeo a 1d pasa a devolver TP,FN,FP,TN

      3. funcion_ets.py : Es un codigo que toma matrices de confusión tridimensionales. La estructura es la de arriba y en la 3er 
      dimensión se encuentran los umbrales. Devuelve la métrica Equitable Threat Score (ETS) en una lista. Cada elemento de la lista
      es el ETS para cada umbral

      4. calculo_ets.py : Este es un codigo que realiza un subset de los datos ya interpolados de GFS y Gsmap. Realiza un subset
      de una región tropical y una región no tropical para evaluar el ETS de cada una de las regiones, para distintos umbrales. 
      De esta manera el output son dos listas o arrays, uno para cada region , con el largo de la cantidad de umbrales que se le pidio,
      y en cada elemento el ETS(umbral). ---Podria mejorarse el codigo ya que cree los stacks. Tambien podria agregarse que exporte los
      umbrales, asi es mas sencilla la lectura 

      5. lectura_ets.ipynb : Este es un notebook donde podemos plotear los npz que contienen como va evolucionando el ETS para los 
      distintos umbrales de precipitacion. --recordar lo que dijimos en (4) se puede mejroar la lectura de umbrales ya que para la 
      redaccion de la tesis seguramente lo use bastante.
      
   


   
   



