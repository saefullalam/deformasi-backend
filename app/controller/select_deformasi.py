import pyodbc 
import json
import os

def select_deformasi(startDate,endDate):
    conn = pyodbc.connect('DRIVER={'+os.environ['DRIVER']+'};Server='+os.environ['SERVER']+';Database='+os.environ['DATABASE']+';Port='+os.environ['PORT']+';UID='+os.environ['SQL_USERNAME']+';PWD='+os.environ['SQL_PASSWORD'])
    cursor = conn.cursor()
    cursor.execute(f"""
                        SELECT CONVERT(VARCHAR,CONVERT(DATE,[Tanggal]))
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
                            FROM [App].[dbo].[Deformasi]
                        WHERE [Tanggal] BETWEEN '{startDate}' AND '{endDate}'
    """
    ) 

    res = list(cursor.fetchall())
    jsonList = []
    for x in res:
        jsonList.append({
        'tanggal'            : x[0],
        'namapatok'          : x[1],
        'northing'           : x[2],
        'easting'            : x[3],
        'elevasi'            : x[4],
        'pergeserany'        : x[5],
        'pergeseranx'        : x[6],
        'pergeseranz'        : x[7],
        'pergeserantotal'    : x[8],
        'lajupergeseran'     : x[9],
        'arahpergeseran'     : x[10],
        'arahpergeseranlabel': x[11],
        'index'              : x[12]
        })
    return json.dumps(jsonList)
    # return res[0]