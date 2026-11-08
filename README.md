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
- py/productos.py : lee los productos
- py/agregar_producto.py : agrega un producto
- py/cambiar_producto.py : cambia el precio de un producto
- py/borrar_producto.py : borra un producto

## Cómo ejecutar
1. Encender MySQL en XAMPP.
2. Importar sql/pedidos_domicilios.sql.
3. Ejecutar los scripts desde la carpeta del proyecto:

    python py\conexion.py
    python py\productos.py

## Integrantes
- Alejandro Meneses