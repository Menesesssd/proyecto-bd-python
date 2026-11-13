import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="", database="pedidos_domicilios")
cursor = conexion.cursor()

# Transacción 1: se confirma con commit
cursor.execute("INSERT INTO cliente (nombre, direccion, telefono) VALUES ('Prueba', 'Calle 1 #2-3', '3000000000')")
conexion.commit()
print("Transacción 1: cliente guardado con COMMIT")

cursor.execute("DELETE FROM cliente WHERE nombre = 'Prueba'")
conexion.commit()
print("Cliente de prueba borrado")

# Transacción 2: se deshace con rollback
cursor.execute("SELECT precio FROM producto WHERE id = 1")
print("Precio antes:", cursor.fetchone()[0])

cursor.execute("UPDATE producto SET precio = 0 WHERE id = 1")
cursor.execute("SELECT precio FROM producto WHERE id = 1")
print("Precio durante la transacción:", cursor.fetchone()[0])

conexion.rollback()
cursor.execute("SELECT precio FROM producto WHERE id = 1")
print("Precio después de ROLLBACK:", cursor.fetchone()[0])

conexion.close()