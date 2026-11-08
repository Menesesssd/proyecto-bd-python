# Proyecto Bases de Datos - Tercer corte (Python)

Base de datos de Pedidos y Domicilios, manejada desde Python.

## Requisitos
- XAMPP con MySQL encendido
- Python 3
- Librería PyMySQL

## Instalación
    python -m pip install pymysql

## Contenido
- sql/pedidos_domicilios.sql : script de la base de datos
- py/conexion.py : prueba la conexión
- py/tablas.py : muestra las tablas
- py/leer_<tabla>.py : lee todos los datos de una tabla
- py/crud_<tabla>.py : agrega, cambia y borra una fila de prueba en una tabla

Tablas: cliente, detalle_pedido, entrega, pago, pedido, producto, repartidor.

## Cómo ejecutar
1. Encender MySQL en XAMPP.
2. Importar sql/pedidos_domicilios.sql.
3. Ejecutar los scripts desde la carpeta del proyecto:

    python py\conexion.py
    python py\leer_cliente.py
    python py\crud_cliente.py

## Integrantes
- Alejandro Meneses