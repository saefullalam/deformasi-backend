import pyodbc 
import json
import uuid
import os
from flask import request

def insert_documentation():
    try:
        if request.method == 'POST':
            data = request.json
            
            data_tanggal = data['Tanggal']
            data_image = data['Image'].split(',')[1]
            id = str(uuid.uuid4())
            conn = pyodbc.connect('DRIVER={'+os.environ['DRIVER']+'};Server='+os.environ['SERVER']+';Database='+os.environ['DATABASE']+';Port='+os.environ['PORT']+';UID='+os.environ['SQL_USERNAME']+';PWD='+os.environ['SQL_PASSWORD'])
            cursor = conn.cursor()
            cursor.execute(f"""
                                INSERT INTO [App].[dbo].[Dokumentasi] ([ID],[Tanggal], [Image])
                                VALUES 
                                ('{id}','{data_tanggal}','{data_image}')        
            """
            )
            cursor.commit()
           
            return f"""Data berhasil diinput!

Tanggal    : {data["Tanggal"]}
"""
    except:
        return """Data error, cek kembali input data!"""
    
    # return res[0]