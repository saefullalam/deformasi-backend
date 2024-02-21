import rasterio
import matplotlib.pyplot as plt
import pyodbc
import numpy as np
import matplotlib
import os
from rasterio.plot import show
from flask import send_file
matplotlib.use('Agg')

def getImage(TanggalData):
    def getDeformasi(Tgl):
        conn = pyodbc.connect('DRIVER={'+os.environ['DRIVER']+'};Server='+os.environ['SERVER']+';Database='+os.environ['DATABASE']+';Port='+os.environ['PORT']+';UID='+os.environ['SQL_USERNAME']+';PWD='+os.environ['SQL_PASSWORD'])
        cursor = conn.cursor()
        cursor.execute(f"""
                            SELECT CONVERT(VARCHAR,CONVERT(DATE,[Tanggal]))[Tanggal]
                                ,[NamaPatok]
                                ,[Easting]
                                ,[Northing]
                                ,[Elevasi]
                                ,[Pergeseran_Y]
                                ,[Pergeseran_X]
                                ,[Pergeseran_Z]
                                ,[Pergeseran_Total]
                                ,[Laju_Pergeseran]
                                ,[Arah_Pergeseran]
                                ,[Arah_Pergeseran_Label]
                                ,[Index]
                                ,CASE
                                    WHEN [Index] = 'Normal' THEN 'lime' 
                                    WHEN [Index] = 'Waspada' THEN 'yellow' 
                                    WHEN [Index] = 'Siaga' THEN 'orange' 
                                    WHEN [Index] = 'Awas' THEN 'red' 
                                    ELSE 'black'
                                END [Color]
                            FROM [App].[dbo].[Deformasi]
                            WHERE [Tanggal] = '{Tgl}'
                                    """
        ) 
        res = list(cursor.fetchall())
        Easting  = []
        Northing = []
        Pergeseran_X = []
        Pergeseran_Y = []
        Warna = []
        for x in res:
            if x[13]=='black':
                continue
            if x[2]==None or x[3]==None or x[5]==None or x[6]==None:
                continue
            Easting.append(x[2])
            Northing.append(x[3])
            Warna.append(x[13])
            if (x[5]>100 and x[5]<1000) or (x[6]>100 and x[6]<1000):
                Pergeseran_Y.append(x[5]/10)
                Pergeseran_X.append(x[6]/10)
            elif (x[5]>1000 and x[5]<10000) or (x[6]>1000 and x[6]<10000):
                Pergeseran_Y.append(x[5]/100)
                Pergeseran_X.append(x[6]/100)
            elif (x[5]>10000 and x[5]<100000) or (x[6]>10000 and x[6]<100000):
                Pergeseran_Y.append(x[5]/1000)
                Pergeseran_X.append(x[6]/1000)
            # elif (x[5]>1 and x[5]<10) or (x[6]>1 and x[6]<10):
            #     Pergeseran_Y.append(x[5]*10)
            #     Pergeseran_X.append(x[6]*10)
            
            else:
                print(x[13])
                Pergeseran_Y.append(x[5])
                Pergeseran_X.append(x[6])

        return Easting,Northing,Pergeseran_X,Pergeseran_Y,Warna


    src = rasterio.open(os.environ['BASEMAP_PATH'],mode='r')

    Easting, Northing, Pergeseran_X,Pergeseran_Y,Warna = getDeformasi(TanggalData)

    fig, ax = plt.subplots(figsize=(10,10))

    extent = [float(os.environ['BASEMAP_COORD_X_MIN']),
              float(os.environ['BASEMAP_COORD_X_MAX']),
              float(os.environ['BASEMAP_COORD_Y_MIN']),
              float(os.environ['BASEMAP_COORD_Y_MAX'])
             ]
    ax = rasterio.plot.show(src, ax=ax,with_bounds=False,extent=extent)
    ax.xaxis.set_tick_params(labelbottom=False)
    ax.yaxis.set_tick_params(labelleft=False)
    ax.set_xticks([])
    ax.set_yticks([])

    for x,y,dx,dy,c in zip(Easting,Northing,Pergeseran_X,Pergeseran_Y,Warna):
        ax.arrow(x,y,dx,dy,width=15,color=c)

    fig.savefig(os.environ['MAPS_RESULT_PATH'],dpi=int(os.environ['MAPS_RESULT_DPI']),bbox_inches='tight')
    return send_file(os.environ['MAPS_RESULT_PATH'], mimetype='image/gif')