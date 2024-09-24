import numpy as np
import plots
import models
import set_dataset as ds
import pickle
from datetime import datetime
import train_utils as tu
import os
import default_conf as dc
import copy
import multiprocessing as mp

inicio_script = datetime.now()
print('Hora de inicio del script: ',inicio_script,'   UTC')

#Cuantos procesadores esta usando
os.environ['OMP_NUM_THREADS']="4"

#Cuantos experimentos esta haciendo a la vez
max_proc=2

TrainConf = dc.TrainConf #Get default configuration.

#-----Inputs---
TrainConf['DataPath'] ="/home/fernando.huaranca/datosmunin/regiones_R_025/medios.npz"
TrainConf['OutPath']  = "/home/fernando.huaranca/datosmunin2/Thesis_Neuronal_Network/work/Salidas/24sep_salidas/"

#Exp type

TrainConf['ModelClass'] = models.EncoderDecoder  #Determino el modelo a utilizar.
TrainConf['ExpName']    = 'MULTI-ENCODECO'

#####################################################
## Parameters to be tested >
TestParameters = dict()
RandomSeed   = [1029]  #As many random seed as initailization experiments we want to perform.
TestParameters['BatchSize'] = [100]         #As many batch sizes as we want to test
TestParameters['LearningRate'] = [ 1.0e-4]  #As many learning rates as we want to test
TestParameters['WeightDecay']  = [ 1.0e-7 ]     #As many Weight decay rates as we want to test
TestParameters['KernelSize']   = [3 ]
TestParameters['Pool']         = [2  ]
TestParameters['Bias']         = [False]
TestParameters['OutActivation']= ['Identity']#,'SiLU']
TestParameters['Channels']     = [  [1,64,64,128,256,512,256,128,64,1] ]

#Esto lo estoy probando yo. Es el numero al que multiplica el lr a partir de la epoca 20.
#TestParameters['Gamma'] = [0.1,0.01]
#TrainConf['MaxEpochs']= 1

#Build the base configuration 
ParameterList = TestParameters.keys()
TrainConfList = []
for ipar , mypar in enumerate( ParameterList ) :
    if mypar in TrainConf['ModelConf'].keys() :
        TrainConf['ModelConf'][mypar] = TestParameters[mypar][0]
    else :
        TrainConf[mypar] = TestParameters[mypar][0]

#Build the sequence of configuration dictionaries that will be pased to the meta_model_training function

ExpNumber = 0 
for ipar , mypar in enumerate( ParameterList ) :
    ParameterValueList = TestParameters[ mypar ]

    for iparval , myparval in enumerate( ParameterValueList ) :
 
        if ( iparval >= 1 or ipar == 0 ) :   #Avoid runing the base configuration several times.
            for myseed in RandomSeed :
                TrainConfList.append( copy.deepcopy( TrainConf ) )

                if mypar in TrainConfList[-1]['ModelConf'].keys() :
                    TrainConfList[-1]['ModelConf'][ mypar ] = myparval
                else :
                    TrainConfList[-1][ mypar ] = myparval 
                TrainConfList[-1]['RandomSeed'] = myseed
                TrainConfList[-1]['HyperParameter'] = mypar   #Store the hyper parameter being explored
                TrainConfList[-1]['ExpNumber'] = ExpNumber
                ExpNumber = ExpNumber + 1 

########################################################################################################

#print( TrainConfList[1] )
#print( len( TrainConfList ) )
#def dummy( input ) :
#    print(input['ExpNumber'])
#    return 0
print(' We will perform ' + str( len(TrainConfList) ) + ' experiments ')   
pool = mp.Pool( min( max_proc , len( TrainConfList ) ) )
pool.map( tu.meta_model_train , TrainConfList ) 
#pool.map( dummy , TrainConfList )

pool.close()

#------
fin_script = datetime.now()
print('Hora de final del script: ',fin_script,'  UTC')

print('.')
dif = fin_script - inicio_script

delta_horas = dif.total_seconds()/3600

print('El tiempo de ejecucion fue de: ',delta_horas,' horas.')
print('.')
print('.')
print('Proceso Completado!')
    

