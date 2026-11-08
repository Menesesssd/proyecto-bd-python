import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="", database="pedidos_domicilios")
cursor = conexion.cursor()

cursor.execute("INSERT INTO repartidor (nombre, telefono) VALUES ('Carlos', '3009998877')")
conexion.commit()
nuevo = cursor.lastrowid
print("Agregado, id:", nuevo)

cursor.execute("UPDATE repartidor SET nombre = 'Carlos Cambiado' WHERE id = " + str(nuevo))
conexion.commit()
print("Cambiado")

cursor.execute("DELETE FROM repartidor WHERE id = " + str(nuevo))
conexion.commit()
print("Borrado")

conexion.close()