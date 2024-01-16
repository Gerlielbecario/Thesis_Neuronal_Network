import gzip
import numpy as np

sx=3600  #Number of points in longitude
sy=1200  #Number of points in latitude
res=0.1  #Horizontal resolution (degrees)

def read_gsmap( my_file ) :

   #Datos SQPE GSMaP NRT observacion inicial
   f = gzip.open( my_file ) # opening file for reading
   sqpe = np.copy( np.frombuffer( f.read() , dtype=np.float32 ) ) # reading a file
   sqpe = sqpe.reshape( sy , sx )
   sqpe = np.flip( sqpe , axis=0 )
   sqpe[np.where(sqpe < 0)] = np.nan

   return sqpe 

def get_gsmap_latlon( ) :

   #Dominio de los datos
   res = 0.1
   corner = [00.05, -59.95] #Esquina E-S de dominio global de GSMaP
   lon = np.arange(corner[0], corner[0] + sx * res, res)
   lat = np.arange(corner[1], corner[1] + sy * res, res)

   return lon , lat

def read_gsmap_subset( my_file , lon_min , lon_max , lat_min , lat_max ) :

   sqpe = read_gsmap( my_file ) 
   lon , lat = get_gsmap_latlon( )

   index_lon = np.where( (lon >= lon_min) & (lon <= lon_max) )[0]
   index_lat = np.where( (lat >= lat_min) & (lat <= lat_max) )[0]

   lon_subset = lon[ index_lon ] 
   lat_subset = lat[ index_lat ]

   sqpe_subset=sqpe[ index_lat.min():index_lat.max() , index_lon.min():index_lon.max() ]

   return sqpe_subset , lon_subset , lat_subset
