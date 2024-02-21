import pyodbc 
import json
import uuid
import pybase64
import os
from flask import send_file

def select_documentation(Tanggal,Urutan):
    if Urutan=='0':
        return send_file(os.environ['IMAGE_BLANK_PATH'], mimetype='image/gif')
    elif Urutan=='keteranganfix':
        return send_file(os.environ['IMAGE_KETERANGAN_PATH'], mimetype='image/gif')
    elif Urutan=='render':
        try:
            naming = str(uuid.uuid4())
            conn = pyodbc.connect('DRIVER={'+os.environ['DRIVER']+'};Server='+os.environ['SERVER']+';Database='+os.environ['DATABASE']+';Port='+os.environ['PORT']+';UID='+os.environ['SQL_USERNAME']+';PWD='+os.environ['SQL_PASSWORD'])
            cursor = conn.cursor()
            cursor.execute(f"""
                                SELECT [Image]
                                FROM [App].[dbo].[Dokumentasi]
                                WHERE [ID]='{Tanggal}'
                            """
            ) 
            
            res = list(cursor.fetchall())
            decoded_data=pybase64.b64decode((res[0][0]))
            result_path = f"E:\\Data Center App\\Documentation\\result_{naming[:5]}.png"
            
            img_file = open(result_path, 'wb')
            img_file.write(decoded_data)
            img_file.close()
            return send_file(result_path, mimetype='image/gif')
        except:
            return send_file(os.environ['IMAGE_BLANK_PATH'], mimetype='image/gif')
    elif Urutan=='select':
        try:
            conn = pyodbc.connect('DRIVER={'+os.environ['DRIVER']+'};Server='+os.environ['SERVER']+';Database='+os.environ['DATABASE']+';Port='+os.environ['PORT']+';UID='+os.environ['SQL_USERNAME']+';PWD='+os.environ['SQL_PASSWORD'])
            cursor = conn.cursor()
            cursor.execute(f"""
                                SELECT [ID],CONVERT(VARCHAR,CONVERT(DATE,[Tanggal])) [Tanggal],[Image]
                                FROM [App].[dbo].[Dokumentasi]
                                WHERE [Tanggal]='{Tanggal}'
                            """
            ) 

            res = list(cursor.fetchall())
            jsonList = []
            for x in res:
                jsonList.append({
                'id'                            : x[0],
                'tanggal'                       : x[1],
                'image'                 : x[2]
                })
            return json.dumps(jsonList)
        except:
            return json.dumps([])
    else:
        try:
            conn = pyodbc.connect('DRIVER={'+os.environ['DRIVER']+'};Server='+os.environ['SERVER']+';Database='+os.environ['DATABASE']+';Port='+os.environ['PORT']+';UID='+os.environ['SQL_USERNAME']+';PWD='+os.environ['SQL_PASSWORD'])
            cursor = conn.cursor()
            cursor.execute(f"""
                                SELECT [Image]
                                FROM [App].[dbo].[Dokumentasi]
                                WHERE [Tanggal]='{Tanggal}'
                            """
            ) 

            res = list(cursor.fetchall())
            decoded_data=pybase64.b64decode((res[int(Urutan)-1][0]))
            result_path = os.environ['IMAGE_TEMPORARY_PATH']+f"\\result_{Urutan}.png"
            img_file = open(result_path, 'wb')
            img_file.write(decoded_data)
            img_file.close()
            return send_file(result_path, mimetype='image/gif')
        except:
            return send_file(os.environ['IMAGE_BLANK_PATH'], mimetype='image/gif')