import pyodbc 
import json
import uuid
import os
from flask import request

def insert_patokm():
    try:
        if request.method == 'POST':
            data = request.json
            print(data)
            id = str(uuid.uuid4())
            conn = pyodbc.connect('DRIVER={'+os.environ['DRIVER']+'};Server='+os.environ['SERVER']+';Database='+os.environ['DATABASE']+';Port='+os.environ['PORT']+';UID='+os.environ['SQL_USERNAME']+';PWD='+os.environ['SQL_PASSWORD'])
            cursor = conn.cursor()
            cursor.execute(f"""
                                INSERT INTO [App].[dbo].[Patok_m] ([ID], [NamaPatok])
                                VALUES 
                                ('{id}','{data['Patok']}')        
            """
            )
            cursor.commit()
           
            return f"""Data berhasil diinput!
Nama Patok    : {data["Patok"]}
"""
    except:
        return """Data error, cek kembali input data!"""
    
    # return res[0]