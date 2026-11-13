import pymysql

conexion = pymysql.connect(host="127.0.0.1", user="root", password="", database="pedidos_domicilios")
cursor = conexion.cursor()

cursor.execute("CREATE OR REPLACE VIEW v_pedidos_clientes AS SELECT cliente.nombre, pedido.fecha, pedido.estado FROM pedido JOIN cliente ON pedido.id_cliente = cliente.id")
print("Vista creada")

print("--- Consulta de la vista ---")
cursor.execute("SELECT * FROM v_pedidos_clientes")
for fila in cursor.fetchall():
    print(fila)

cursor.execute("DROP VIEW IF EXISTS v_pedidos_clientes")
print("Vista borrada")

conexion.close()