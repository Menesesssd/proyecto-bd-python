import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="", database="pedidos_domicilios")
cursor = conexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS categoria (id INT PRIMARY KEY AUTO_INCREMENT, nombre VARCHAR(50))")
print("Tabla categoria creada")

cursor.execute("ALTER TABLE producto ADD COLUMN IF NOT EXISTS descripcion VARCHAR(100)")
print("Columna descripcion revisada en producto")

cursor.execute("DROP TABLE IF EXISTS categoria")
print("Tabla categoria borrada")

conexion.close()