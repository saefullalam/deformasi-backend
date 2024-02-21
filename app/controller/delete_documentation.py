import pyodbc 
import json
import uuid
import os
from flask import request

def delete_documentation():
    try:
        if request.method == 'POST':
            data = request.json
            conn = pyodbc.connect('DRIVER={'+os.environ['DRIVER']+'};Server='+os.environ['SERVER']+';Database='+os.environ['DATABASE']+';Port='+os.environ['PORT']+';UID='+os.environ['SQL_USERNAME']+';PWD='+os.environ['SQL_PASSWORD'])
            cursor = conn.cursor()
            cursor.execute(f"""
                                DELETE [App].[dbo].[Dokumentasi]
                                WHERE [ID]='{data['ID']}'
            """
            )
            cursor.commit()
            return f"""Data berhasil dihapus!

Tanggal    : {data["Tanggal"]}
"""
    except:
        return """gagal menghapus data, mohon refresh browser"""
    
    # return res[0]