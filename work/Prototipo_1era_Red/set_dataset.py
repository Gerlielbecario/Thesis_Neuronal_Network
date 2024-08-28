import numpy as np
import torch
from torch.utils.data import Dataset
from sklearn.model_selection import train_test_split

#Funcion para abrir los datos .npz y extraer las variables que elegimos, y lo guardamos en un diccionario
def get_data( input_data_file, var_input, var_target, train_ratio, val_ratio, test_ratio, data_aug )   :
    
    data_from_file  = np.load( input_data_file ) 
    Data=dict()
    Input = data_from_file[var_input]
    Target = data_from_file[var_target]
    
    #En este caso tanto el input como el target tiene las mismas dimensiones, por eso podemos usarlas para ambos
    Data["nx"], Data["ny"], Data["len_total"]  = Input.shape
    
    indices = range(Data["len_total"]) #Con el largo del dataset cuento cuantos hay y genero un vector de indices

    #Separo en los conjuntos de Entrenamiento y un conjunto que será Validacion/Testing
    train_ids, rest_ids = train_test_split(indices, test_size=1 - train_ratio , shuffle=False )
    #Ahora a ese conjunto restante lo divido en Validacion y testing propiamente.
    val_ids, test_ids   = train_test_split(rest_ids, test_size=test_ratio/(test_ratio + val_ratio) , shuffle=False ) 

    #Guardo e imprimo por pantalla la cantidad de datos en cada conjunto
    Data["len_train"], Data["len_val"], Data["len_test"] = len(train_ids), len(val_ids), len(test_ids)
    print('Training set starts at :', str( np.min( train_ids) ) , ' and ends at: ', str( np.max( train_ids ) ) )
    print('Validation set starts at :', str( np.min( val_ids ) ) , ' and ends at: ', str( np.max( val_ids ) ) )
    print('Testing set starts at: ', str( np.min( test_ids ) ) , ' and ends at: ', str( np.max( test_ids ) ) )
    
    #Cantidad de datos de entrenamiento
   # train_ids = train_ids[:400]
    
    #Aplicamos data augmentation
    if data_aug == False:
        train_x_data = Input[:,:,train_ids]
        train_y_data = Target[:,:,train_ids]
    else:
        train_x_data, train_y_data = augment_data(Input[:,:,train_ids], Target[:,:,train_ids])
 
    val_x_data = Input[:,:,val_ids]
    val_y_data = Target[:,:,val_ids]

    
    test_x_data = Input[:,:,test_ids]
    test_y_data = Target[:,:,test_ids]

    Data["xmin"], Data["xmax"] = np.append(train_x_data,val_x_data,axis=2).min() , np.append(train_x_data,val_x_data,axis=2).max()
    Data["ymin"], Data["ymax"] = np.append(train_y_data,val_y_data,axis=2).min() , np.append(train_y_data,val_y_data,axis=2).max()
    
    return Data, train_x_data, train_y_data, val_x_data, val_y_data, test_x_data, test_y_data

class set_up_data(Dataset):
    "Para utilizarse con el DataLoader de PyTorch"
    def __init__(self,Data, Input, Target):
        self.x_data = Input

        self.y_data = Target
        #Parametros para la normalizacion
        self.xmin, self.xmax = Data["xmin"], Data["xmax"]
        self.ymin, self.ymax = Data["ymin"], Data["ymax"]

        #Normalizacion de los datos
        self.x_data = norm( self.x_data, self.xmin, self.xmax)
        self.y_data = norm( self.y_data, self.ymin, self.ymax)

    def __len__(self):
        "Denoto el numero total de muestras"
        return self.x_data.shape[2]
        
    def __getitem__(self,index):
        x = torch.tensor(self.x_data[:,:,index], dtype=torch.float)
        y = torch.tensor(self.y_data[:,:,index], dtype=torch.float)
        return x, y

#Funciones de normalizacion
def norm( data , datamin , datamax ):
    #return 2.0*(data-datamin)/(datamax-datamin)-1.0 #Normalizacion [-1,1]
    #return (data-datamin)/(datamax-datamin) #Normalizacion [0,1]
    return data
    
def denorm( data , datamin , datamax) :
    #return 0.5*(data+1.0)*(datamax-datamin)+datamin #Normalizacion [-1,1]
    #return (data)*(datamax-datamin)+datamin #Normalizacion [0,1]
    return data

#Funcion para hacer Data Augmentation rotando las imagenes
def augment_data( Input_data , Target_data) :
    
    nx_input, ny_input, nt = np.shape( Input_data )
    Aug_Input = np.zeros( (nx_input , ny_input, 4*nt ) )
    
    nx_target,ny_target,_ = np.shape( Target_data )
    Aug_Target = np.zeros( (nx_target , ny_target, 4*nt ) )
    
    Aug_Input[:,:,0:nt] = Input_data 
    Aug_Target[:,:,0:nt] = Target_data    

    Aug_Input[:,:,nt:2*nt] = np.flip( Input_data) 
    Aug_Target[:,:,nt:2*nt] = np.flip( Target_data)    

    Aug_Input[:,:,2*nt:3*nt] = np.fliplr( Input_data) 
    Aug_Target[:,:,2*nt:3*nt] = np.fliplr( Target_data)    

    Aug_Input[:,:,3*nt:4*nt] = np.flip( np.fliplr( Input_data ) )
    Aug_Target[:,:,3*nt:4*nt] = np.flip( np.fliplr( Target_data ) ) 

    return Aug_Input, Aug_Target
