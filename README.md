# Proyecto Bases de Datos - Tercer corte (Python)

Base de datos de Pedidos y Domicilios, manejada desde Python con PyMySQL.

## Requisitos
- XAMPP con MySQL encendido
- Python 3
- Librería PyMySQL

## Instalación
    python -m pip install -r requirements.txt

## Contenido
- sql/pedidos_domicilios.sql : la base de datos completa
- sql/pedidos_domicilios_insert.sql : datos de prueba
- sql/commands/ : comandos SQL por tipo (01_DDL a 06_TCL)
- docs/ : diagrama entidad-relación y diccionario de datos
- py/conexion.py : prueba la conexión
- py/tablas.py : muestra las tablas
- py/ddl.py, dml.py, dql.py, vdl.py, dcl.py, tcl.py : un script por cada archivo de sql/commands
- `py/leer_<tabla>.py` : lee todos los datos de una tabla
- `py/crud_<tabla>.py` : agrega, cambia y borra una fila de prueba en una tabla

Tablas: cliente, detalle_pedido, entrega, pago, pedido, producto, repartidor.

## Cómo ejecutar
1. Encender MySQL en XAMPP.
2. Importar sql/pedidos_domicilios.sql en phpMyAdmin.
3. Ejecutar los scripts desde la carpeta del proyecto, en este orden:

    python py\conexion.py
    python py\ddl.py
    python py\dml.py
    python py\dql.py
    python py\vdl.py
    python py\dcl.py
    python py\tcl.py

Notas:
- dcl.py se conecta como root, porque crear usuarios y dar permisos requiere una cuenta administradora.
- Los scripts dejan la base igual que antes de correrlos: lo que agregan, lo borran al final.

## Integrantes
- Alejandro Meneses
- Juan Esteban Ravagli
- Dilan Forero