import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="", database="pedidos_domicilios")
cursor = conexion.cursor()

cursor.execute("INSERT INTO pago (metodo, monto, id_pedido) VALUES ('efectivo', 20000, 1)")
conexion.commit()
nuevo = cursor.lastrowid
print("Agregado, id:", nuevo)

cursor.execute("UPDATE pago SET monto = 25000 WHERE id = " + str(nuevo))
conexion.commit()
print("Cambiado")

cursor.execute("DELETE FROM pago WHERE id = " + str(nuevo))
conexion.commit()
print("Borrado")

conexion.close()