import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="", database="pedidos_domicilios")
cursor = conexion.cursor()

cursor.execute("INSERT INTO entrega (estado, id_pedido, id_repartidor) VALUES ('prueba', 1, 1)")
conexion.commit()
nuevo = cursor.lastrowid
print("Agregado, id:", nuevo)

cursor.execute("UPDATE entrega SET estado = 'prueba cambiada' WHERE id = " + str(nuevo))
conexion.commit()
print("Cambiado")

cursor.execute("DELETE FROM entrega WHERE id = " + str(nuevo))
conexion.commit()
print("Borrado")

conexion.close()