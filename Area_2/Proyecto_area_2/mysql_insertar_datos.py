import mysql.connector


# Datos simulados para áreas comunitarias
areas_comunitarias_data = [
    ('Albany Park', 2023, 51361, 34350.45, 32.1, 9.4, 33.3, 19.3, 5.9),
    ('Archer Heights', 2023, 13142, 29550.78, 61.2, 2.3, 31.6, 2.8, 1.3),
    # Agrega más datos simulados según sea necesario
]

# Datos simulados para comisarías
comisarias_data = [
    ('Comisaría 1', 1, '123 Main St', '312-555-1234', 41.8781, -87.6298),  # Latitud y longitud de Chicago
    ('Comisaría 2', 2, '456 Elm St', '312-555-5678', 41.8837, -87.6303),  # Latitud y longitud de Chicago
    # Agrega más datos simulados según sea necesario
]

# Datos simulados para hospitales
hospitales_data = [
    ('Hospital 1', 1, '789 Oak St', '312-555-9012', 41.8917, -87.6076),  # Latitud y longitud de Chicago
    ('Hospital 2', 2, '901 Pine St', '312-555-3456', 41.8784, -87.6245),  # Latitud y longitud de Chicago
    # Agrega más datos simulados según sea necesario
]

# Datos simulados para delitos
delitos_data = [
    ('CASE12345', 'Robo a mano armada', True, 1, '500 Block of N Michigan Ave', 41.8914, -87.6243),  # Latitud y longitud de Chicago
    ('CASE67890', 'Robo de vehículo', False, 2, '700 Block of W 19th St', 41.8551, -87.6657),  # Latitud y longitud de Chicago
    # Agrega más datos simulados según sea necesario
]

# Función para insertar datos en las tablas
def insertar_datos():
    conexion = mysql.connector.connect(
        host ="localhost",
        user ="root",
        password ="",
        database ="chicago_safety_data"
    )
    cursor = conexion.cursor()

    # Insertar datos en areas_comunitarias
    cursor.executemany('''
        INSERT INTO areas_comunitarias (nombre, año, poblacion, ingresos, latinos, negros, blancos, asiaticos, otros)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''', areas_comunitarias_data)

    # Insertar datos en comisarias
    cursor.executemany('''
        INSERT INTO comisarias (nombre, area_comunitaria, direccion, telefono, latitud, longitud)
        VALUES (%s, %s, %s, %s, %s, %s)
    ''', comisarias_data)

    # Insertar datos en hospitales
    cursor.executemany('''
        INSERT INTO hospitales (nombre, area_comunitaria, direccion, telefono, latitud, longitud)
        VALUES (%s, %s, %s, %s, %s, %s)
    ''', hospitales_data)

    # Insertar datos en delitos
    cursor.executemany('''
        INSERT INTO delitos (num_caso, descripcion, arrestado, area_comunitaria, cuadra, latitud, longitud)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    ''', delitos_data)

    conexion.commit()
    cursor.close()
    conexion.close()

if __name__ == "__main__":
    insertar_datos()