from app import app
from app.controller import generateMaps, select_data, insert_data, delete_data, select_deformasi, \
                            insert_documentation,select_documentation,insert_sarantindakan,select_patok, \
                            select_tindakan, index,delete_sarantindakan,delete_documentation,select_patokm,insert_patokm,delete_patokm

app.route('/', methods=['GET']) (index.index)
app.route('/maps/<TanggalData>', methods=['GET']) (generateMaps.getImage)

app.route('/select_patok/<Tanggal>', methods=['GET']) (select_patok.select_patok)
app.route('/select_patokm', methods=['GET','POST']) (select_patokm.select_patokm)
app.route('/select_documentation/<Tanggal>/<Urutan>', methods=['GET','POST']) (select_documentation.select_documentation)
app.route('/select/<startDate>/<endDate>',methods=['POST']) (select_data.select_data)
app.route('/select_sarantindakan/<startDate>/<endDate>',methods=['POST']) (select_tindakan.select_tindakan)
app.route('/selectdeformasi/<startDate>/<endDate>',methods=['POST','GET']) (select_deformasi.select_deformasi)

app.route('/deletedata',methods=['POST']) (delete_data.delete_data)
app.route('/delete_patokm',methods=['POST']) (delete_patokm.delete_patokm)
app.route('/delete_sarantindakan',methods=['POST']) (delete_sarantindakan.delete_sarantindakan)
app.route('/delete_documentation',methods=['POST']) (delete_documentation.delete_documentation)


app.route('/insertdata',methods=['POST']) (insert_data.insert_data)
app.route('/insertpatokm',methods=['POST']) (insert_patokm.insert_patokm)
app.route('/insertdocumentation',methods=['POST']) (insert_documentation.insert_documentation)
app.route('/insertsarantindakan',methods=['POST']) (insert_sarantindakan.insert_sarantindakan)

# app.route('/materi/<file>', methods=['GET']) (reader.html_reader)