import mysql.connector
conexion = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "Cine")

#print(conexion)

cursor = conexion.cursor()

cursor.execute("show databases")
for base in cursor:
    print(base)

#2.3.1
#cursor.execute("CREATE DATABASE Cine;")

#2.3.2
#cursor.execute('CREATE TABLE peliculas (id_pelicula INT AUTO_INCREMENT PRIMARY KEY, Titulo VARCHAR(50), Año INT(4), Presupuesto INT)')

#2.3.3
""" sql_insert = "INSERT INTO peliculas (Titulo, Año, Presupuesto) VALUES (%s, %s, %s)"
peliculas = [
    ("El padrino", 1972, 6000000), 
    ("Tiburón", 1975, 9000000), 
    ("Los cazafantasmas", 1984, 30000000), 
    ("El exorcista", 1973, 12000000), 
    ("Pulp Fiction", 1994, 8000000)
]

cursor.executemany(sql_insert, peliculas)
conexion.commit() """

#2.3.4
""" consulta_sql = "SELECT Titulo FROM peliculas"
cursor.execute(consulta_sql)

print("Títulos de las películas: ")
for resultado in cursor:
    print(resultado) """

#2.3.5
""" consulta_sql = "SELECT Titulo FROM peliculas WHERE titulo LIKE 'E%'"
cursor.execute(consulta_sql)

print("Títulos de las películas: ")
for resultado in cursor:
    print(resultado) """

#2.3.6
""" consulta_sql = "SELECT * FROM peliculas WHERE Año < 1980"
cursor.execute(consulta_sql)

print("Títulos de las películas: ")
for resultado in cursor:
    print(resultado) """

#2.3.7
""" consulta_sql = "SELECT SUM(Presupuesto) FROM peliculas"
cursor.execute(consulta_sql)

print("El presupuesto total es: ")
for resultado in cursor:
    print(resultado) """

#2.3.8
""" consulta_sql = "SELECT Titulo, Presupuesto FROM peliculas ORDER BY Presupuesto DESC LIMIT 1"
cursor.execute(consulta_sql)

print("La película mas cara es: ")
for (titulo, presupuesto) in cursor:
    print(f"Título: {titulo} \nPresupuesto: {presupuesto}") """

#2.3.9
""" consulta_sql = "SELECT Titulo FROM peliculas ORDER BY Titulo ASC"
cursor.execute(consulta_sql)

print("Películas ordenadas alfabeticamente: ")
for resultado in cursor:
    print(resultado) """

#2.3.10
""" consulta_sql = "DELETE FROM peliculas WHERE Año < 1980"
cursor.execute(consulta_sql)
conexion.commit() """
















