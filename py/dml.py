import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="", database="pedidos_domicilios")
cursor = conexion.cursor()

cursor.execute("INSERT INTO cliente (nombre, direccion, telefono) VALUES ('Pedro', 'Calle 50 #8-15', '3004445566')")
conexion.commit()
print("Cliente agregado")

cursor.execute("UPDATE cliente SET telefono = '3009998877' WHERE nombre = 'Pedro'")
conexion.commit()
print("Teléfono cambiado")

cursor.execute("DELETE FROM cliente WHERE nombre = 'Pedro'")
conexion.commit()
print("Cliente borrado")

conexion.close()