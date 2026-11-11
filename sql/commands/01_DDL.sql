USE pedidos_domicilios;

-- CREATE: crear una tabla nueva
CREATE TABLE IF NOT EXISTS categoria (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(50)
);

-- ALTER: agregar una columna a la tabla producto
ALTER TABLE producto ADD COLUMN IF NOT EXISTS descripcion VARCHAR(100);

-- DROP: borrar la tabla de ejemplo
DROP TABLE IF EXISTS categoria;