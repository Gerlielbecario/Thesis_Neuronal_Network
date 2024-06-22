from sklearn.model_selection import train_test_split
import numpy as np
import torch
from torch.utils.data import Dataset

#Construye un objeto que contiene los datos
class set_up_data(Dataset):
#    "Para utilizarse con el DataLoader de PyTorch"
    def __init__(self,Data, Input, Target):
        self.x_data = Input

        self.y_data = Target
       #Parametros para la normalizacion
        self.xmin, self.xmax = Data["xmin"], Data["xmax"]
        self.ymin, self.ymax = Data["ymin"], Data["ymax"]

        #Normalizacion de los datos
        #Basicamente esta diciendo:
        #argumentos: Input, normalizo min, normalizo max    
        self.x_data = norm( self.x_data, self.xmin, self.xmax)
        self.y_data = norm( self.y_data, self.ymin, self.ymax)

    def __len__(self):
#        "Denoto el numero total de muestras"
        return self.x_data.shape[0]

    #Aca lo transformo a tensor finalmente  
        
    def __getitem__(self,index):
        x = torch.tensor(self.x_data[index,:,:], dtype=torch.float)
        y = torch.tensor(self.y_data[index,:,:], dtype=torch.float)
        return x, y

#Funciones de normalizacion la que uso arriba
def norm( data , datamin , datamax ):
    #return 2.0*(data-datamin)/(datamax-datamin)-1.0 #Normalizacion [-1,1]
    return (data-datamin)/(datamax-datamin) #Normalizacion [0,1]
    #return data
    
def denorm( data , datamin , datamax) :
    #return 0.5*(data+1.0)*(datamax-datamin)+datamin #Normalizacion [-1,1]
    return (data)*(datamax-datamin)+datamin #Normalizacion [0,1]
    #return data

