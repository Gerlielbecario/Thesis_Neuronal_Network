import numpy as np
import set_dataset as ds
from scipy.stats import spearmanr

def rmse( modeldata , targetdata ) :
    return np.sqrt( np.mean( (modeldata.flatten() - targetdata.flatten()) ** 2 ) )

def bias( modeldata , targetdata ) :
    return np.mean( modeldata.flatten() - targetdata.flatten() )

def corr_P( modeldata , targetdata ) :    
    return np.corrcoef( modeldata.flatten() , targetdata.flatten() )[0,1]

def corr_S( modeldata , targetdata ) :    
    return spearmanr( modeldata.flatten() , targetdata.flatten() )[0]

