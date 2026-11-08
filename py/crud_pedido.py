import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="", database="pedidos_domicilios")
cursor = conexion.cursor()

cursor.execute("INSERT INTO pedido (fecha, estado, id_cliente) VALUES ('2026-11-08', 'prueba', 1)")
conexion.commit()
nuevo = cursor.lastrowid
print("Agregado, id:", nuevo)

cursor.execute("UPDATE pedido SET estado = 'prueba cambiada' WHERE id = " + str(nuevo))
conexion.commit()
print("Cambiado")

cursor.execute("DELETE FROM pedido WHERE id = " + str(nuevo))
conexion.commit()
print("Borrado")

conexion.close()