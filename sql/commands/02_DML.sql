USE pedidos_domicilios;

-- INSERT: agregar un cliente
INSERT INTO cliente (nombre, direccion, telefono)
VALUES ('Pedro', 'Calle 50 #8-15', '3004445566');

-- UPDATE: cambiar su teléfono
UPDATE cliente SET telefono = '3009998877' WHERE nombre = 'Pedro';

-- DELETE: borrarlo
DELETE FROM cliente WHERE nombre = 'Pedro';