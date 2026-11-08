import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="", database="pedidos_domicilios")
cursor = conexion.cursor()

cursor.execute("DELETE FROM producto WHERE nombre = 'Perro caliente'")
conexion.commit()

print("Producto borrado")
conexion.close()