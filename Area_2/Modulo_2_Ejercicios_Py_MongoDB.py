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

from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymongo

MONGO_HOST="localhost"
MONGO_PORT="27017"
MONGO_TIME_OUT=1000 

MONGO_URL_LOCAL="mongodb://"+MONGO_HOST+":"+MONGO_PORT+"/" 
MONGO_URL_CLOUD="mongodb+srv://joseignacio:Ignacio01@cluster0.buvsnzb.mongodb.net/" 




#2.4.1
""" MONGO_BASEDATOS="sample_training"
    MONGO_COLECCION="companies"
    try:
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
""" MONGO_BASEDATOS="sample_training"
    MONGO_COLECCION="companies"
    try:
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
""" MONGO_BASEDATOS="sample_training"
    MONGO_COLECCION="companies"
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
    print("Fallo al conectarse a mongodb "+errorConexion) """

#2.4.4
""" MONGO_BASEDATOS="sample_training"
MONGO_COLECCION="inspections"

cliente=pymongo.MongoClient(MONGO_URL_CLOUD,serverSelectionTimeoutMS=MONGO_TIME_OUT)
cliente.server_info()

baseDatos=cliente[MONGO_BASEDATOS]
coleccion=baseDatos[MONGO_COLECCION]

def mostrarDatos():
    try:
        registros=tabla.get_children()
        for registro in registros:
            tabla.delete(registro)
        for documento in coleccion.find():
            tabla.insert('',0,text=documento["business_name"],values=documento["certificate_number"])

        cliente.close()   
    except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
        print("Tiempo exedido "+errorTiempo)
    except pymongo.errors.ConnectionFailure as errorConexion:
        print("Fallo al conectarse a mongodb "+errorConexion)
    
 
ventana=Tk()
tabla=ttk.Treeview(ventana,columns=2)
tabla.grid(row=1,column=0,columnspan=2)
tabla.heading("#0",text="Nombre de la empresa")
tabla.heading("#1",text="Número de certificado")

mostrarDatos()
 
#Mostramos la ventana
ventana.mainloop() """

#2.4.5
""" MONGO_BASEDATOS="sample_training"
MONGO_COLECCION="zips"

try:
    cliente=pymongo.MongoClient(MONGO_URL_CLOUD,serverSelectionTimeoutMS=MONGO_TIME_OUT)
    cliente.server_info()

    baseDatos=cliente[MONGO_BASEDATOS]
    coleccion=baseDatos[MONGO_COLECCION]

    nuevo_documento = {
        "city": "Madrid",
        "zip": "458971",
        "loc": [40.342553, -3.171997],
        "pop": 11111,
        "state": "SP"
    }

    resultado = coleccion.insert_one(nuevo_documento)
    if resultado.inserted_id:
        print("El nuevo documento se insertó correctamente:")
        print(nuevo_documento)
    else:
        print("Hubo un error al insertar el documento.")


    cliente.close()   
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo exedido "+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb "+errorConexion)
     """

#2.4.6
""" MONGO_BASEDATOS="sample_training"
MONGO_COLECCION="zips"

try:
    cliente=pymongo.MongoClient(MONGO_URL_CLOUD,serverSelectionTimeoutMS=MONGO_TIME_OUT)
    cliente.server_info()

    baseDatos=cliente[MONGO_BASEDATOS]
    coleccion=baseDatos[MONGO_COLECCION]

    filter = {"city": "Madrid"}
    documentos = coleccion.find(filter)

    for documento in documentos:
        print(documento)
   

    cliente.close()   
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo exedido "+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb "+errorConexion) """
    
#2.4.7
MONGO_BASEDATOS="sample_training"
MONGO_COLECCION="zips"

cliente=pymongo.MongoClient(MONGO_URL_CLOUD,serverSelectionTimeoutMS=MONGO_TIME_OUT)
cliente.server_info()

baseDatos=cliente[MONGO_BASEDATOS]
coleccion=baseDatos[MONGO_COLECCION]

def mostrarDatos():
    try:
        registros=tabla.get_children()
        for registro in registros:
            tabla.delete(registro)
        for documento in coleccion.find({"city": "BREMEN"}):
            zip_code = documento.get("zip", "Desconocido")
            pop = documento.get("pop", "Desconocido")
            tabla.insert('', 0, text=zip_code, values=(pop,))
            

        cliente.close()   
    except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
        print("Tiempo exedido "+errorTiempo)
    except pymongo.errors.ConnectionFailure as errorConexion:
        print("Fallo al conectarse a mongodb "+errorConexion)
    
 
ventana=Tk()
ventana.title("Zips and population of Bremen")
tabla=ttk.Treeview(ventana,columns=2)
tabla.grid(row=1,column=0,columnspan=2)
tabla.heading("#0",text="Zips")
tabla.heading("#1",text="Population")

mostrarDatos()

ventana.mainloop()
