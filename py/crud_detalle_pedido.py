import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="", database="pedidos_domicilios")
cursor = conexion.cursor()

cursor.execute("INSERT INTO detalle_pedido (cantidad, id_pedido, id_producto) VALUES (2, 1, 1)")
conexion.commit()
nuevo = cursor.lastrowid
print("Agregado, id:", nuevo)

cursor.execute("UPDATE detalle_pedido SET cantidad = 5 WHERE id = " + str(nuevo))
conexion.commit()
print("Cambiado")

cursor.execute("DELETE FROM detalle_pedido WHERE id = " + str(nuevo))
conexion.commit()
print("Borrado")

conexion.close()