#Este es un codigo al que se le da dos listas. 
#Las listas tienen las direcciones de los archivos de las carpetas

import pandas as pd


def limpia_fecha(Files):

    #Lista donde almacenar los nombres de las fechas
    fechas_limpias = []
    
    for file in Files:
        
        #Es la manera de extraer las fechas del nombre de los archivos
        fecha = file.split('/')[-1].split('_')[-1].split('.')[0]
        
        fechas_limpias.append(fecha)

    return fechas_limpias

def devuelve_periodo_comun(lista1,lista2):

    lista_one= limpia_fecha(lista1)

    lista_two = limpia_fecha(lista2)

    #Genero dos dataframe con el mismo nombre de columna
    df1 = pd.DataFrame({'Archivos':lista_one})
    df2 = pd.DataFrame({'Archivos':lista_two})

    #Dataframe con nombres de archivos en comun
    df3 = pd.merge(df1['Archivos'],df2['Archivos'],on='Archivos')

    df3 = df3.sort_values(by='Archivos')

    periodo_comun = df3['Archivos'].to_list()

    return periodo_comun


