import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="")
print("¡Conectado a MariaDB!")
conexion.close()