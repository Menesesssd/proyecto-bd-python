USE pedidos_domicilios;

-- CREATE VIEW: crear una vista con cliente, fecha y estado
CREATE OR REPLACE VIEW v_pedidos_clientes AS
SELECT cliente.nombre, pedido.fecha, pedido.estado
FROM pedido
JOIN cliente ON pedido.id_cliente = cliente.id;

-- Consultar la vista como si fuera una tabla
SELECT * FROM v_pedidos_clientes;

-- DROP VIEW: borrar la vista
DROP VIEW IF EXISTS v_pedidos_clientes;