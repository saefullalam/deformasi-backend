import pyodbc 
import json
import uuid
import os
from flask import request

def delete_data():
    try:
        if request.method == 'POST':
            data = request.json
            id = str(uuid.uuid4())
            conn = pyodbc.connect('DRIVER={'+os.environ['DRIVER']+'};Server='+os.environ['SERVER']+';Database='+os.environ['DATABASE']+';Port='+os.environ['PORT']+';UID='+os.environ['SQL_USERNAME']+';PWD='+os.environ['SQL_PASSWORD'])
            cursor = conn.cursor()
            cursor.execute(f"""
                                DELETE [App].[dbo].[RawData]
                                WHERE [ID]='{data['ID']}'
            """
            )
            cursor.commit()
            return f"""Data berhasil dihapus!

Tanggal    : {data["Tanggal"]}
Nama Patok : {data["Patok"]}
Northing   : {data["Northing"]}
Easting    : {data["Easting"]}
Elevasi    : {data["Elevasi"]}
"""
    except:
        return """gagal menghapus data, mohon refresh browser"""
    
    # return res[0]