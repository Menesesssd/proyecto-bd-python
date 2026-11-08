import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="", database="pedidos_domicilios")
cursor = conexion.cursor()

cursor.execute("SHOW TABLES")
for tabla in cursor.fetchall():
    print(tabla[0])

conexion.close()