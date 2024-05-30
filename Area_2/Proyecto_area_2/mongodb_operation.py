import os
from dotenv import load_dotenv
import pymongo
from datetime import datetime

# Cargar variables de entorno desde el archivo .env
load_dotenv()

MONGO_HOST= "localhost"
MONGO_PORT= "27017"
MONGO_TIME_OUT= 1000 

MONGO_URL_LOCAL= "mongodb://"+MONGO_HOST+":"+MONGO_PORT+"/" 
MONGO_URL_CLOUD= os.getenv("MONGO_URL_CLOUD") 


MONGO_BASEDATOS="delincuencia"
MONGO_COLECCION="criminales"

# Datos de un criminal a insertar
nuevo_criminal = {
    '_id': 1,
    'nombre': 'AARON',
    'apellidos': 'WILLIAMS-BANKS',
    'cuadra': '072XX S SOUTH SHORE DR',
    'delitos': ['agresión sexual', 'robo con violencia'],
    'estatura': 185,
    'peso': 80,
    'f_nacimiento': datetime(1976, 3, 1)
}

# Lista de criminales
criminales = [
    {
        '_id': 2,
        'nombre': 'CARLOS',
        'apellidos': 'LOPEZ-MARTINEZ',
        'cuadra': '4054 W CULLERTON ST',
        'delitos': ['robo a mano armada', 'homicidio'],
        'estatura': 175,
        'peso': 70,
        'f_nacimiento': datetime(1985, 8, 12)
    },
    {
        '_id': 3,
        'nombre': 'MARIA',
        'apellidos': 'RODRIGUEZ-GONZALEZ',
        'cuadra': '4500 W JACKSON BLVD',
        'delitos': ['asalto', 'secuestro'],
        'estatura': 160,
        'peso': 55,
        'f_nacimiento': datetime(1990, 5, 24)
    },
    {
        '_id': 4,
        'nombre': 'PEDRO',
        'apellidos': 'SANCHEZ-HERNANDEZ',
        'cuadra': '2600 S HAMLIN AVE',
        'delitos': ['tráfico de drogas', 'extorsión'],
        'estatura': 180,
        'peso': 75,
        'f_nacimiento': datetime(1978, 2, 5)
    },
    {
        '_id': 5,
        'nombre': 'ANA',
        'apellidos': 'MARTINEZ-PEREZ',
        'cuadra': '8900 S HOUSTON AVE',
        'delitos': ['fraude', 'violación'],
        'estatura': 165,
        'peso': 60,
        'f_nacimiento': datetime(1982, 10, 18)
    }
]

try:
    cliente=pymongo.MongoClient(MONGO_URL_CLOUD,serverSelectionTimeoutMS=MONGO_TIME_OUT)
    cliente.server_info()
    #print("Conexion con mongo exitosa")

    baseDatos=cliente[MONGO_BASEDATOS]
    coleccion=baseDatos[MONGO_COLECCION]

    """ # 3.1 Insertar un criminal
    coleccion.insert_one(nuevo_criminal)
    print("Datos del criminal insertados correctamente.") """

    """ # 3.2 Insertar varios criminales
    for criminal in criminales:
        coleccion.insert_one(criminal)
        print(f"Datos del criminal {criminal['nombre']} insertados correctamente.") """
        
    """ # 3.3 Busqueda entre fehcas de nacimiento
    fecha_inicio = datetime(1980, 1, 1)
    fecha_fin = datetime(1990, 12, 31)

    criminales_nacimiento_entre_fechas = coleccion.find({
        'f_nacimiento': {'$gte': fecha_inicio, '$lte': fecha_fin}
    })

    for criminal in criminales_nacimiento_entre_fechas:
        print(criminal) """

    """ # 3.4 Busqueda criminales por delito
    criminales_robo_violencia = coleccion.find({
        'delitos': 'robo con violencia'
    })

    for criminal in criminales_robo_violencia:
        print(criminal) """

    """ # 3.5 Busqueda criminales por estatura y peso
    criminales_estatura_peso = coleccion.find({
        'estatura': {'$lte': 200},  # Menor o igual 
        'peso': {'$gte': 40}         # Mayor o igual 
    })

    for criminal in criminales_estatura_peso:
        print(criminal) """



    cliente.close()
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Fallo al conectarse a mongodb "+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb "+errorConexion)
