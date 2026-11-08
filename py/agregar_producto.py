import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="", database="pedidos_domicilios")
cursor = conexion.cursor()

cursor.execute("INSERT INTO producto (nombre, precio, stock) VALUES ('Perro caliente', 9000, 40)")
conexion.commit()

print("Producto agregado")
conexion.close()