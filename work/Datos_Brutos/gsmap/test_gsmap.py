import gsmap_tool as gsmap 
import glob
import matplotlib.pyplot as plt

data_path ='/home/jruiz/datosmunin3/datos/Datos_GSMAP/daily_G_v8/'
ini_lon=280.0
end_lon=320.0
ini_lat=-60.0
end_lat=10.0

file_list = glob.glob( data_path + '/gsmap_gauge.2015*.0.1d.daily.00Z-23Z.v8.0000.0.dat.gz' )

for ifile , my_file in enumerate( file_list ) :
    print(ifile,my_file)

    if ifile == 0 :
       accum_data , lon , lat = gsmap.read_gsmap_subset( my_file , ini_lon , end_lon , ini_lat , end_lat )
    else          :
       tmp_data , lon , lat = gsmap.read_gsmap_subset( my_file , ini_lon , end_lon , ini_lat , end_lat ) 
       accum_data = accum_data + tmp_data 

accum_data = accum_data / ( ifile + 1 )

plt.pcolor( lon , lat , accum_data )
plt.show()
plt.savefig('test.png')


