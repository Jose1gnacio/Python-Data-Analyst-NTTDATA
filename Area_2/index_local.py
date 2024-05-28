from pymongo import MongoClient
 
client = MongoClient()
 
print('1.- BBDD Existentes: ', client.list_database_names())
 
db = client["prueba"]
print('2.- BBDD Actual:', db)