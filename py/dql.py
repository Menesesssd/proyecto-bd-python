import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="", database="pedidos_domicilios")
cursor = conexion.cursor()

print("--- Todos los clientes ---")
cursor.execute("SELECT * FROM cliente")
for fila in cursor.fetchall():
    print(fila)

print("--- Pedidos pendientes ---")
cursor.execute("SELECT * FROM pedido WHERE estado = 'pendiente'")
for fila in cursor.fetchall():
    print(fila)

print("--- Cliente junto a su pedido ---")
cursor.execute("SELECT cliente.nombre, pedido.fecha, pedido.estado FROM pedido JOIN cliente ON pedido.id_cliente = cliente.id")
for fila in cursor.fetchall():
    print(fila)

print("--- Productos por pedido ---")
cursor.execute("SELECT id_pedido, SUM(cantidad) AS total_productos FROM detalle_pedido GROUP BY id_pedido")
for fila in cursor.fetchall():
    print(fila)

conexion.close()