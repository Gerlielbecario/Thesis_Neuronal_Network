#Este codigo realiza el calculo de la metrica 
#Equitable threat Score

#https://confluence.ecmwf.int/display/FUG/Section+6.2.3+Equitable+Threat+Score

#En muy pocas palabras permite evaluar la confibialidad de un pronostico en 
#un area. Lo especial que tiene esta metrica es que teoricamente nos permite
#desprendernos de el factor espacial.
#Yo podria comparar el ETS de un pais, con el de otro pais distante, y en 
#resumidas cuentas este valor me seguiria siendo util.


import numpy as np
import os




def ETS(Umbrales,Matriz_stack):

     #Calculamos el ETS por umbrales
     indices_ets = []

     for umbral in range(0,len(Umbrales)):

          #TP,FN,FP,TN
          tp,fn,fp,tn = Matriz_stack[umbral].ravel()

          #Numero de casos totales
          N = tp + fp + tn + fn
          H = tp #Hits
          O = tp + fp 
          F = tp + fn  
          R = O*(F/N)
          #ets
          ETS = (H-R)/(O+F-H-R)
          indices_ets.append(ETS)
          
     return indices_ets