""" from pymongo import MongoClient
 
client = MongoClient()
 
print('1.- BBDD Existentes: ', client.list_database_names())
 
db = client["prueba"]
print('2.- BBDD Actual:', db) """


""" import pymongo
#Información necesaria para conectarnos a MongoDB
MONGO_HOST="localhost"
MONGO_PORT="27017"
MONGO_TIME_OUT=1000 #Por defecto necesita un time out para realizar la conexión

MONGO_URL_LOCAL="mongodb://"+MONGO_HOST+":"+MONGO_PORT+"/" #Aquí puedes poner cualquier dirección. Esta dirección te conectará con el localhost (Compass). Al final del código explicaremos como conectar Compass con Atlas para poder trabajar con las bases de datos que creamos en la unidad MongoDB.
MONGO_URL_CLOUD="mongodb+srv://joseignacio:Ignacio01@cluster0.buvsnzb.mongodb.net/" #Recuerda que aquí tendrás que sustituir <username> por tu nombre de usuario y <password> por tu contraseña


MONGO_BASEDATOS="sample_training"
MONGO_COLECCION="companies"

try:
    cliente=pymongo.MongoClient(MONGO_URL_CLOUD,serverSelectionTimeoutMS=MONGO_TIME_OUT)
    #Pedimos la información de conexión
    cliente.server_info()
    #Mostramos mensaje de conexión correcta
    print("Conexion con mongo exitosa")
    #Vamos a conectarnos a la BBDD pasándole el nombre de la BBDD y obtenemos ese objeto dentro de una variable
    baseDatos=cliente[MONGO_BASEDATOS]
    coleccion=baseDatos[MONGO_COLECCION]

    for documento in coleccion.find():
        print(documento)
    #Cerramos la conexión
    cliente.close()
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Fallo al conectarse a mongodb "+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb "+errorConexion) """

import pymongo

MONGO_HOST="localhost"
MONGO_PORT="27017"
MONGO_TIME_OUT=1000 

MONGO_URL_LOCAL="mongodb://"+MONGO_HOST+":"+MONGO_PORT+"/" 
MONGO_URL_CLOUD="mongodb+srv://joseignacio:Ignacio01@cluster0.buvsnzb.mongodb.net/" 


MONGO_BASEDATOS="sample_training"
MONGO_COLECCION="companies"

#2.4.1
""" try:
    cliente=pymongo.MongoClient(MONGO_URL_CLOUD,serverSelectionTimeoutMS=MONGO_TIME_OUT)
    cliente.server_info()
    #print("Conexion con mongo exitosa")

    baseDatos=cliente[MONGO_BASEDATOS]
    coleccion=baseDatos[MONGO_COLECCION]

    
    for documento in coleccion.find({}, {"name": 1, "number_of_employees": 1, "_id": 0}):
        nombre = documento.get("name")
        numero_empleados = documento.get("number_of_employees")
        print(f"Compañía: {nombre} - Número de empleados: {numero_empleados}")
    
    cliente.close()
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Fallo al conectarse a mongodb "+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb "+errorConexion) """

#2.4.2
""" try:
    cliente=pymongo.MongoClient(MONGO_URL_CLOUD,serverSelectionTimeoutMS=MONGO_TIME_OUT)
    cliente.server_info()
    #print("Conexion con mongo exitosa")

    baseDatos=cliente[MONGO_BASEDATOS]
    coleccion=baseDatos[MONGO_COLECCION]
    
    total_documentos = coleccion.count_documents({})
    print(f"\nTotal de documentos en la colección '{MONGO_COLECCION}': {total_documentos}")

    
    cliente.close()
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo excedido "+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb "+errorConexion) """

#2.4.3
""" try:
    cliente=pymongo.MongoClient(MONGO_URL_CLOUD,serverSelectionTimeoutMS=MONGO_TIME_OUT)
    cliente.server_info()
    #print("Conexion con mongo exitosa")

    baseDatos=cliente[MONGO_BASEDATOS]
    coleccion=baseDatos[MONGO_COLECCION]

    filter = {"number_of_employees": {"$gt": 250}}
    for documento in coleccion.find(filter, {"name": 1, "number_of_employees": 1}):
        nombre = documento.get("name")
        numero_empleados = documento.get("number_of_employees")
        print(f"Compañía: {nombre} - Número de empleados: {numero_empleados}")    
        
    cliente.close()
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo excedido "+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb "+errorConexion) """

#2.4.4
try:
    cliente=pymongo.MongoClient(MONGO_URL_CLOUD,serverSelectionTimeoutMS=MONGO_TIME_OUT)
    cliente.server_info()
    #print("Conexion con mongo exitosa")

    baseDatos=cliente[MONGO_BASEDATOS]
    coleccion=baseDatos[MONGO_COLECCION]

    filter = {"number_of_employees": {"$gt": 250}}
    for documento in coleccion.find(filter, {"name": 1, "number_of_employees": 1}):
        nombre = documento.get("name")
        numero_empleados = documento.get("number_of_employees")
        print(f"Compañía: {nombre} - Número de empleados: {numero_empleados}")    
        
    cliente.close()
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo excedido "+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb "+errorConexion)







