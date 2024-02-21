import pyodbc 
import json
import os

def select_patok(Tanggal):
    conn = pyodbc.connect('DRIVER={'+os.environ['DRIVER']+'};Server='+os.environ['SERVER']+';Database='+os.environ['DATABASE']+';Port='+os.environ['PORT']+';UID='+os.environ['SQL_USERNAME']+';PWD='+os.environ['SQL_PASSWORD'])
    cursor = conn.cursor()
    cursor.execute(f"""
                        SELECT 
                                a.[NamaPatok],
                                CASE
                                    WHEN b.[NamaPatok] IS NOT NULL THEN 'Sudah'
                                    ELSE 'Belum'
                                END [Available]
                        FROM [App].[dbo].[Patok_m] a
                        LEFT JOIN 
                            (	SELECT [NamaPatok]
                                FROM [App].[dbo].[RawData]
                                WHERE Tanggal='{Tanggal}' ) b
                            ON a.[NamaPatok] = b.[NamaPatok]
                        ORDER BY [Available],a.[NamaPatok]
    """
    ) 

    res = list(cursor.fetchall())
    jsonList = []
    for x in res:
        jsonList.append({
        'namapatok'            : x[0],
        'status'            : x[1],
        })
    return json.dumps(jsonList)
    # return res[0]