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

try:
    cliente=pymongo.MongoClient(MONGO_URL_CLOUD,serverSelectionTimeoutMS=MONGO_TIME_OUT)
    cliente.server_info()
    #print("Conexion con mongo exitosa")

    baseDatos=cliente[MONGO_BASEDATOS]
    coleccion=baseDatos[MONGO_COLECCION]

    coleccion.insert_one(nuevo_criminal)
    print("Datos del criminal insertados correctamente.")
        
    
    cliente.close()
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Fallo al conectarse a mongodb "+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb "+errorConexion)
