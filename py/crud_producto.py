import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="", database="pedidos_domicilios")
cursor = conexion.cursor()

cursor.execute("INSERT INTO producto (nombre, precio, stock) VALUES ('Empanada', 3000, 20)")
conexion.commit()
nuevo = cursor.lastrowid
print("Agregado, id:", nuevo)

cursor.execute("UPDATE producto SET precio = 3500 WHERE id = " + str(nuevo))
conexion.commit()
print("Cambiado")

cursor.execute("DELETE FROM producto WHERE id = " + str(nuevo))
conexion.commit()
print("Borrado")

conexion.close()