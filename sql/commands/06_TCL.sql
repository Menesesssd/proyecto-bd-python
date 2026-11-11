USE pedidos_domicilios;

-- Transacción 1: se confirma con COMMIT
START TRANSACTION;
INSERT INTO cliente (nombre, direccion, telefono)
VALUES ('Laura', 'Calle 100 #15-20', '3005556677');
COMMIT;

-- Transacción 2: se deshace con ROLLBACK
START TRANSACTION;
UPDATE producto SET precio = 0;
ROLLBACK;