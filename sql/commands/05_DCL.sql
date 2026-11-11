-- CREATE USER: crear un usuario cajero
CREATE USER IF NOT EXISTS 'cajero'@'localhost' IDENTIFIED BY '1234';

-- GRANT: darle permiso de ver e insertar en la base de datos
GRANT SELECT, INSERT ON pedidos_domicilios.* TO 'cajero'@'localhost';

-- REVOKE: quitarle el permiso de insertar
REVOKE INSERT ON pedidos_domicilios.* FROM 'cajero'@'localhost';