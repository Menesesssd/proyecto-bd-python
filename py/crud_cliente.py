import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="", database="pedidos_domicilios")
cursor = conexion.cursor()

cursor.execute("INSERT INTO cliente (nombre, direccion, telefono) VALUES ('Pedro', 'Calle 1 #2-3', '3001234567')")
conexion.commit()
nuevo = cursor.lastrowid
print("Agregado, id:", nuevo)

cursor.execute("UPDATE cliente SET nombre = 'Pedro Cambiado' WHERE id = " + str(nuevo))
conexion.commit()
print("Cambiado")

cursor.execute("DELETE FROM cliente WHERE id = " + str(nuevo))
conexion.commit()
print("Borrado")

conexion.close()