USE pedidos_domicilios;

-- SELECT: ver todos los clientes
SELECT * FROM cliente;

-- WHERE: ver solo los pedidos pendientes
SELECT * FROM pedido WHERE estado = 'pendiente';

-- JOIN: ver el nombre del cliente junto a su pedido
SELECT cliente.nombre, pedido.fecha, pedido.estado
FROM pedido
JOIN cliente ON pedido.id_cliente = cliente.id;

-- GROUP BY: cuántos productos lleva cada pedido
SELECT id_pedido, SUM(cantidad) AS total_productos
FROM detalle_pedido
GROUP BY id_pedido;