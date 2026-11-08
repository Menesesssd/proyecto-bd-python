import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="", database="pedidos_domicilios")
cursor = conexion.cursor()

cursor.execute("UPDATE producto SET precio = 4500 WHERE nombre = 'Gaseosa'")
conexion.commit()

print("Producto cambiado")
conexion.close()