import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="")
cursor = conexion.cursor()

cursor.execute("CREATE USER IF NOT EXISTS 'cajero'@'localhost' IDENTIFIED BY '1234'")
print("Usuario cajero listo")

cursor.execute("GRANT SELECT, INSERT ON pedidos_domicilios.* TO 'cajero'@'localhost'")
print("Permisos dados")

cursor.execute("REVOKE INSERT ON pedidos_domicilios.* FROM 'cajero'@'localhost'")
print("Permiso de insertar quitado")

cursor.execute("SHOW GRANTS FOR 'cajero'@'localhost'")
for fila in cursor.fetchall():
    print(fila)

conexion.close()