# Diccionario de datos

| Tabla | Columna | Tipo | Llave | Descripción |
|---|---|---|---|---|
| cliente | id | INT | PK | Identificador del cliente |
| cliente | nombre | VARCHAR(50) | | Nombre del cliente |
| cliente | direccion | VARCHAR(100) | | Dirección de entrega |
| cliente | telefono | VARCHAR(15) | | Teléfono de contacto |
| producto | id | INT | PK | Identificador del producto |
| producto | nombre | VARCHAR(50) | | Nombre del producto |
| producto | precio | DECIMAL(10,2) | | Precio de venta |
| producto | stock | INT | | Unidades disponibles |
| producto | descripcion | VARCHAR(100) | | Descripción (agregada con ALTER en 01_DDL) |
| pedido | id | INT | PK | Identificador del pedido |
| pedido | fecha | DATE | | Fecha en que se hizo el pedido |
| pedido | estado | VARCHAR(20) | | Pendiente, en camino o entregado |
| pedido | id_cliente | INT | FK | Cliente que hizo el pedido (cliente.id) |
| detalle_pedido | id | INT | PK | Identificador del detalle |
| detalle_pedido | cantidad | INT | | Unidades del producto en el pedido |
| detalle_pedido | id_pedido | INT | FK | Pedido al que pertenece (pedido.id) |
| detalle_pedido | id_producto | INT | FK | Producto pedido (producto.id) |
| pago | id | INT | PK | Identificador del pago |
| pago | metodo | VARCHAR(20) | | Tarjeta, efectivo, nequi, etc. |
| pago | monto | DECIMAL(10,2) | | Valor pagado |
| pago | id_pedido | INT | FK | Pedido que se pagó (pedido.id) |
| repartidor | id | INT | PK | Identificador del repartidor |
| repartidor | nombre | VARCHAR(50) | | Nombre del repartidor |
| repartidor | telefono | VARCHAR(15) | | Teléfono del repartidor |
| entrega | id | INT | PK | Identificador de la entrega |
| entrega | estado | VARCHAR(20) | | En camino o entregado |
| entrega | id_pedido | INT | FK | Pedido que se entrega (pedido.id) |
| entrega | id_repartidor | INT | FK | Repartidor asignado (repartidor.id) |