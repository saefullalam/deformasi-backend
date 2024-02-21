import pyodbc 
import json
import os

def select_tindakan(startDate,endDate):
    conn = pyodbc.connect('DRIVER={'+os.environ['DRIVER']+'};Server='+os.environ['SERVER']+';Database='+os.environ['DATABASE']+';Port='+os.environ['PORT']+';UID='+os.environ['SQL_USERNAME']+';PWD='+os.environ['SQL_PASSWORD'])
    cursor = conn.cursor()
    cursor.execute(f"""
                        SELECT [ID],CONVERT(VARCHAR,CONVERT(DATE,[Tanggal])) [Tanggal],[SaranTindakan]
                        FROM [App].[dbo].[SaranTindakan]
                        WHERE [Tanggal] BETWEEN '{startDate}' AND '{endDate}'
                            """
    ) 

    res = list(cursor.fetchall())
    jsonList = []
    for x in res:
        jsonList.append({
        'id'                            : x[0],
        'tanggal'                       : x[1],
        'sarantindakan'                 : x[2]
        })
    return json.dumps(jsonList)
    # return res[0]