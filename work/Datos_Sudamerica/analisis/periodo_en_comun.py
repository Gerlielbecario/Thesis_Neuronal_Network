#ESTE ES UN CODIGO QUE CONTIENE UNA FUNCION A LA QUE SE LE DA
#DOS RUTAS DE CARPETAS Y DEVUELVE UNA LISTA CON LOS NOMBRES
#DE ARCHIVOS DE ELLAS EN COMUN

#Libreria 

import os 
import pandas as pd
from datetime import datetime

#

#Funcion que devuelve la fecha de los archivos
def obtener_fecha(nombre_archivo):
    try:
        fecha_str = nombre_archivo.split('.')[0]  # Suponiendo que el nombre del archivo es DD-MM-YYYY.ext
        fecha = datetime.strptime(fecha_str, "%d-%m-%Y")
        return fecha
    except ValueError:
        return None
    
#Genero dos dataframes para evaluar nombres de archivos en comun

#df1 = pd.DataFrame({'Archivos':GFS_files})
#df2 = pd.DataFrame({'Archivos':JAXA_files})

#Dataframe con nombres de archivos en comun
#df3 = pd.merge(df1['Archivos'],df2['Archivos'],on='Archivos')

#Lista de nombres repetidos en las 2 carpetas
#comunes = df3['Archivos'].to_list()

def periodo_comun(carpeta1,carpeta2):

    #Genera dos listas con los nombres de los archivos en la carpeta
    lista1 = os.listdir(carpeta1)
    lista2 = os.listdir(carpeta2)

    #Genero dos dataframe con el mismo nombre de columna
    df1 = pd.DataFrame({'Archivos':lista1})
    df2 = pd.DataFrame({'Archivos':lista2})

    #Dataframe con nombres de archivos en comun
    df3 = pd.merge(df1['Archivos'],df2['Archivos'],on='Archivos')

    #Lista de nombres repetidos en las 2 carpetas
    comunes = df3['Archivos'].to_list()

    return comunes 



