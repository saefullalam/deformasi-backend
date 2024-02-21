import pyodbc 
import json
import uuid
import os
from flask import request

def insert_sarantindakan():
    try:
        if request.method == 'POST':
            data = request.json
            id = str(uuid.uuid4())
            conn = pyodbc.connect('DRIVER={'+os.environ['DRIVER']+'};Server='+os.environ['SERVER']+';Database='+os.environ['DATABASE']+';Port='+os.environ['PORT']+';UID='+os.environ['SQL_USERNAME']+';PWD='+os.environ['SQL_PASSWORD'])
            cursor = conn.cursor()
            cursor.execute(f"""
                                INSERT INTO [App].[dbo].[SaranTindakan] ([ID],[Tanggal], [SaranTindakan])
                                VALUES 
                                ('{id}','{data['Tanggal']}','{data['Saran']}')        
            """
            )
            cursor.commit()
           
            return f"""Data berhasil diinput!

Tanggal    : {data["Tanggal"]}
Saran      : {data["Saran"]}
"""
    except:
        return """Data error, cek kembali input data!"""
    
    # return res[0]