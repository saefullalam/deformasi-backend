import pyodbc 
import os
import json

def select_data(startDate,endDate):
    conn = pyodbc.connect('DRIVER={'+os.environ['DRIVER']+'};Server='+os.environ['SERVER']+';Database='+os.environ['DATABASE']+';Port='+os.environ['PORT']+';UID='+os.environ['SQL_USERNAME']+';PWD='+os.environ['SQL_PASSWORD'])
    cursor = conn.cursor()
    cursor.execute(f"""
                        SELECT 
                            [ID]
                            ,CONVERT(VARCHAR,CONVERT(DATE,[Tanggal])) [Tanggal]
                            ,[NamaPatok]
                            ,[Northing]
                            ,[Easting]
                            ,[Elevasi]
                        FROM [App].[dbo].[RawData]
                        WHERE [Tanggal] BETWEEN '{startDate}' AND '{endDate}'
    """
    ) 

    res = list(cursor.fetchall())
    jsonList = []
    for x in res:
        jsonList.append({
        'id'                 : x[0],
        'tanggal'            : x[1],
        'namapatok'          : x[2],
        'northing'           : x[3],
        'easting'            : x[4],
        'elevasi'            : x[5],
        })
    return json.dumps(jsonList)
    # return res[0]