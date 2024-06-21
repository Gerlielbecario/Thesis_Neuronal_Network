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