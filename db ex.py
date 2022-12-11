import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\KimHyeonggyu\inclass221114.accdb')
cursor = conn.cursor()
cursor.execute('select * from products')
   
for row in cursor.fetchall():
    print (row)