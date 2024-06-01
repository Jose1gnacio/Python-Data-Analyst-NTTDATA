import os
from dotenv import load_dotenv
import pymongo
from datetime import datetime


# Cargar variables de entorno desde el archivo .env
load_dotenv()

""" MONGO_HOST= "localhost"
MONGO_PORT= "27017"
MONGO_TIME_OUT= 1000  """

#MONGO_URL_LOCAL= "mongodb://"+MONGO_HOST+":"+MONGO_PORT+"/" 

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

""" 
    # 3.1 Insertar un criminal
    coleccion.insert_one(nuevo_criminal)
    print("Datos del criminal insertados correctamente.")

    # 3.2 Insertar varios criminales
    for criminal in criminales:
        coleccion.insert_one(criminal)
        print(f"Datos del criminal {criminal['nombre']} insertados correctamente.")   

 """

# Función para conectar con MongoDB
def conectar_mongodb():
    try:
        MONGO_URL_CLOUD = os.getenv("MONGO_URL_CLOUD")
        cliente = pymongo.MongoClient(MONGO_URL_CLOUD)
        baseDatos = cliente["delincuencia"]
        coleccion = baseDatos["criminales"]
        return coleccion
    except Exception as e:
        print("Error al conectar con MongoDB:", e)
        return None

# Función para buscar criminales entre fechas de nacimiento
def buscar_por_fecha():
    coleccion = conectar_mongodb()
    if coleccion is not None:  # Verificamos si la colección no es None
        fecha_inicio_str = input("Ingrese la fecha de inicio en formato YYYY-MM-DD: ")
        fecha_fin_str = input("Ingrese la fecha de fin en formato YYYY-MM-DD: ")
        try:
            fecha_inicio = datetime.strptime(fecha_inicio_str, '%Y-%m-%d')
            fecha_fin = datetime.strptime(fecha_fin_str, '%Y-%m-%d')
            criminales_nacimiento_entre_fechas = coleccion.find({
                'f_nacimiento': {'$gte': fecha_inicio, '$lte': fecha_fin}
            })

            for criminal in criminales_nacimiento_entre_fechas:
                print(criminal)
        except ValueError:
            print("Formato de fecha incorrecto. Utilice el formato YYYY-MM-DD.")

# Función para buscar criminales por delito
def buscar_por_delito():
    coleccion = conectar_mongodb()
    if coleccion is not None:
        descripcion_delito = input("Ingrese el delito a buscar: ")
        try:
            # Utilizamos una consulta en la colección para encontrar los registros que contengan el delito especificado
            delitos_encontrados = coleccion.find({'delitos': descripcion_delito})

            # Mostramos los delitos encontrados
            for delito in delitos_encontrados:
                print(delito)
        except Exception as e:
            print("Error al buscar el delito:", e)

# Función para buscar criminales por peso y estatura
def buscar_por_estatura_peso():
    coleccion = conectar_mongodb()
    if coleccion is not None:
        estatura = int(input("Ingrese la estatura (en centímetros) a buscar: "))
        peso = int(input("Ingrese el peso (en kilogramos) a buscar: "))
        try:
            # Utilizamos una consulta en la colección para encontrar los registros que cumplan con la condición de estatura y peso
            delincuentes_encontrados = coleccion.find({
                'estatura': {'$lt': estatura},  # Estatura menor que el valor ingresado
                'peso': {'$gt': peso}           # Peso mayor que el valor ingresado
            })

            # Mostramos los delincuentes encontrados
            for delincuente in delincuentes_encontrados:
                print(delincuente)
        except Exception as e:
            print("Error al buscar delincuentes por estatura y peso:", e)

# Función para listar todos los criminales
def mostrar_todos_los_criminales():
    coleccion = conectar_mongodb()
    if coleccion is not None:
        try:
            # Utilizamos find sin condiciones para obtener todos los documentos en la colección
            criminales = coleccion.find()

            # Mostramos los criminales encontrados
            for criminal in criminales:
                print(criminal)
        except Exception as e:
            print("Error al listar criminales:", e)

# Función para agrega un criminal
def agregar_criminal():
    coleccion = conectar_mongodb()
    if coleccion is not None:
        try:
            nombre = input("Ingrese el nombre del criminal: ")
            apellidos = input("Ingrese los apellidos del criminal: ")
            cuadra = input("Ingrese la cuadra donde opera el criminal: ")
            delitos = input("Ingrese los delitos cometidos por el criminal (separados por coma): ").split(',')
            estatura = float(input("Ingrese la estatura del criminal en centímetros: "))
            peso = float(input("Ingrese el peso del criminal en kilogramos: "))
            fecha_nacimiento_str = input("Ingrese la fecha de nacimiento del criminal en formato YYYY-MM-DD: ")
            fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, '%Y-%m-%d')
            
            nuevo_criminal = {
                '_id': obtener_proximo_id(coleccion),  # Puedes implementar una función para obtener el próximo ID disponible
                'nombre': nombre,
                'apellidos': apellidos,
                'cuadra': cuadra,
                'delitos': delitos,
                'estatura': estatura,
                'peso': peso,
                'f_nacimiento': fecha_nacimiento
            }

            coleccion.insert_one(nuevo_criminal)
            print("Datos del criminal insertados correctamente.")
        except ValueError:
            print("Error: Verifique los datos ingresados.")

# Función para obtener el próximo ID disponible
def obtener_proximo_id():
    coleccion = conectar_mongodb()
    # Obtiene el último ID en la colección
    ultimo_criminal = coleccion.find_one({}, sort=[('_id', -1)])
    
    if ultimo_criminal is not None:
        proximo_id = ultimo_criminal['_id'] + 1
    else:
        # Si la colección está vacía, asigna el ID 1 al primer criminal
        proximo_id = 1
    
    return proximo_id

# Función para editar un criminal
def editar_criminal():
    coleccion = conectar_mongodb()
    if coleccion is not None:
        try:
            id_criminal = int(input("Ingrese el ID del criminal que desea editar: "))
            criminal = coleccion.find_one({'_id': id_criminal})

            if criminal is None:
                print("No se encontró ningún criminal con el ID proporcionado.")
                return

            print("Criminal encontrado:")
            print(criminal)

            print("Seleccione el parámetro que desea editar:")
            print("1. Nombre")
            print("2. Apellidos")
            print("3. Cuadra")
            print("4. Delitos")
            print("5. Estatura")
            print("6. Peso")
            print("7. Fecha de nacimiento")
            opcion = int(input("Ingrese el número correspondiente al parámetro: "))

            if opcion == 1:
                nuevo_valor = input("Ingrese el nuevo nombre: ")
                campo = 'nombre'
            elif opcion == 2:
                nuevo_valor = input("Ingrese los nuevos apellidos: ")
                campo = 'apellidos'
            elif opcion == 3:
                nuevo_valor = input("Ingrese la nueva cuadra: ")
                campo = 'cuadra'
            elif opcion == 4:
                nuevo_valor = input("Ingrese los nuevos delitos (separados por coma): ").split(',')
                campo = 'delitos'
            elif opcion == 5:
                nuevo_valor = float(input("Ingrese la nueva estatura en centímetros: "))
                campo = 'estatura'
            elif opcion == 6:
                nuevo_valor = float(input("Ingrese el nuevo peso en kilogramos: "))
                campo = 'peso'
            elif opcion == 7:
                nuevo_valor = input("Ingrese la nueva fecha de nacimiento en formato YYYY-MM-DD: ")
                nuevo_valor = datetime.strptime(nuevo_valor, '%Y-%m-%d')
                campo = 'f_nacimiento'
            else:
                print("Opción no válida.")
                return

            coleccion.update_one({'_id': id_criminal}, {'$set': {campo: nuevo_valor}})
            print("Criminal actualizado correctamente.")

        except ValueError:
            print("Error: Verifique los datos ingresados.")

def buscar_por_id():
    coleccion = conectar_mongodb()
    if coleccion is not None:
        descripcion_delito = int(input("Ingrese el id: "))
        try:
            # Utilizamos una consulta en la colección para encontrar los registros que contengan el delito especificado
            delitos_encontrados = coleccion.find({'_id': descripcion_delito})

            # Mostramos los delitos encontrados            
            print(delitos_encontrados)
        except Exception as e:
            print("Error al buscar el delito:", e)

if __name__ == "__main__":
    #obtener_proximo_id()
    editar_criminal()
    #buscar_por_id()