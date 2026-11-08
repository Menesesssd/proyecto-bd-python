import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="", database="pedidos_domicilios")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM producto")
for fila in cursor.fetchall():
    print(fila)

conexion.close()