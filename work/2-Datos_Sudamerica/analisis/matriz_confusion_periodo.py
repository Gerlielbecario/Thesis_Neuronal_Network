from sklearn.metrics import confusion_matrix
import numpy as np

def matriz_confusion_periodo(Modelo,Observado,Umbrales):
    
    #Lista donde se almacenan las matrices de confusion
    matrices = []

    for umbral in Umbrales:
       
        #Reshapeamos datos del modelo a 1d
        mod = Modelo.ravel() >= umbral
      #  print('El shape del modelo de reshapeado')

        #Reshapeamos datos de observaciones a 1d
        obs = Observado.ravel() >= umbral
        
        #Creamos las matrices de confusión para distintos umbrales
        #En orden de filas TP,FN,FP,TN
        cm = confusion_matrix(y_true=obs,y_pred=mod,labels=[True,False])
        
        #Agregamos las matrices de confusion de distintos umbrales a la lista
        matrices.append(cm)

    #Agregamos las matrices en la primer dimension 
    matriz_umbrales = np.stack(matrices,axis=0)
    
    return matriz_umbrales
