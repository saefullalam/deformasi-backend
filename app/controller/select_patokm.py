import pyodbc 
import json
import os

def select_patokm():
    conn = pyodbc.connect('DRIVER={'+os.environ['DRIVER']+'};Server='+os.environ['SERVER']+';Database='+os.environ['DATABASE']+';Port='+os.environ['PORT']+';UID='+os.environ['SQL_USERNAME']+';PWD='+os.environ['SQL_PASSWORD'])
    cursor = conn.cursor()
    cursor.execute(f"""
                        SELECT [ID],[NamaPatok]
                        FROM [App].[dbo].[Patok_m]
                            """
    ) 

    res = list(cursor.fetchall())
    jsonList = []
    for x in res:
        jsonList.append({
        'id'                            : x[0],
        'patok'                       : x[1],
        })
    return json.dumps(jsonList)
    # return res[0]