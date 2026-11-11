USE pedidos_domicilios;

INSERT INTO cliente (nombre, direccion, telefono) VALUES
('Ana', 'Calle 10 #5-20', '3001112233'),
('Luis', 'Carrera 7 #45-10', '3002223344'),
('Marta', 'Calle 80 #12-30', '3003334455');

INSERT INTO producto (nombre, precio, stock) VALUES
('Hamburguesa', 15000, 50),
('Pizza', 28000, 30),
('Gaseosa', 4000, 100),
('Papas', 7000, 60);

INSERT INTO pedido (fecha, estado, id_cliente) VALUES
('2026-10-01', 'entregado', 1),
('2026-10-05', 'en camino', 2),
('2026-10-08', 'pendiente', 3);

INSERT INTO detalle_pedido (cantidad, id_pedido, id_producto) VALUES
(2, 1, 1),
(1, 1, 3),
(1, 2, 2),
(1, 3, 4);

INSERT INTO pago (metodo, monto, id_pedido) VALUES
('tarjeta', 34000, 1),
('efectivo', 28000, 2),
('nequi', 7000, 3);

INSERT INTO repartidor (nombre, telefono) VALUES
('Carlos', '3101112233'),
('Sofía', '3102223344');

INSERT INTO entrega (estado, id_pedido, id_repartidor) VALUES
('entregado', 1, 1),
('en camino', 2, 2);