#3.1.1
""" import csv

ruta_archivo = 'C:/Users/josei/Desktop/apellidos_mas_frecuentes_pais_Argentina.csv'

with open(ruta_archivo, newline='', encoding='utf-8') as csv_file:
    lector_csv = csv.reader(csv_file)  
    
    for fila in lector_csv:
        print(fila) """



#3.1.2
""" import csv

ruta_archivo = 'C:/Users/josei/Desktop/apellidos_mas_frecuentes_pais_Argentina.csv'

with open(ruta_archivo, newline='', encoding='utf-8') as csv_file:
    lector_csv = csv.reader(csv_file) 

    next(lector_csv)  
    
    for fila in lector_csv:
        if float(fila[1]) > 0.1:
            print(fila[0]) """


#3.1.3
""" import numpy as np

ruta_archivo = 'C:/Users/josei/Desktop/apellidos_mas_frecuentes_pais_Argentina.csv'

data = np.genfromtxt(ruta_archivo, delimiter=',', dtype=None, encoding='utf-8', names=True)

apellidos = data['apellido']
porcentajes = data['porcentaje_de_poblacion_portadora']
rankings = data['ranking']

print("Apellidos:")
print(apellidos)
print("\nPorcentajes de población portadora:")
print(porcentajes)
print("\nRankings:")
print(rankings) """

#3.1.6
""" import pandas as pd

ruta_archivo = 'C:/Users/josei/Desktop/puntos_de_acceso_wifi_Mexico.csv'

data = pd.read_csv(ruta_archivo)

print(data) """

#3.1.7
""" import numpy as np

ruta_archivo = 'C:/Users/josei/Desktop/puntos_de_acceso_wifi_Mexico.csv'

data = np.genfromtxt(ruta_archivo, delimiter=',', dtype=None, encoding='utf-8', names=True)
print(data.dtype)
# Mostrar los datos
print(data) """

#3.1.8
""" import numpy as np

ruta_archivo = 'C:/Users/josei/Desktop/puntos_de_acceso_wifi_Mexico.csv'

data = np.genfromtxt(ruta_archivo, delimiter=',', dtype=None, encoding='utf-8', names=True)

id = data['\ufeffid']
programa = data['programa']
fecha_instalacion = data['fecha_instalacion']
latitud = data['latitud']
longitud = data['longitud']
colonia = data['colonia']
alcaldia = data['alcaldia']

print("id:")
print(id)
print("\nPrograma:")
print(programa)
print("\nFecha de instalación:")
print(fecha_instalacion)
print("\nLatitud:")
print(latitud)
print("\nLongitud:")
print(longitud)
print("\nColonia:")
print(colonia)
print("\nAlcaldia:")
print(alcaldia) """

#3.1.9
""" import numpy as np

ruta_archivo = 'C:/Users/josei/Desktop/puntos_de_acceso_wifi_Mexico.csv'

data = np.genfromtxt(ruta_archivo, delimiter=',', dtype=None, encoding='utf-8', names=True)

alcaldias_unicas = np.unique(data['alcaldia'])

for alcaldia in alcaldias_unicas:
    print(alcaldia) """

#3.1.10
""" import json

ruta_archivo = 'C:/Users/josei/Desktop/Catálogo de información pública.json'

with open(ruta_archivo, 'r', encoding='utf-8') as contenido:
    data = json.load(contenido)

print(json.dumps(data, indent=1, ensure_ascii=False)) """

#3.1.11
""" import numpy as np

# Ruta del archivo CSV (descargado manualmente)
ruta_archivo = 'C:/Users/josei/Desktop/BBDD_Funcionarios_Publicos_2020.csv'

# Cargar el archivo CSV en un array de Numpy
data = np.genfromtxt(ruta_archivo, delimiter=';', dtype=None, encoding='utf-8', names=True)

print(data.dtype) """

#3.1.11
""" import ssl
import numpy as np
import urllib.request
import io

ssl = ssl._create_unverified_context()

http_request = urllib.request.urlopen(
    "https://www.consejotransparencia.cl/transparencia_activa/datoabierto/archivosFiscalizacion/BBDD_Funcionarios_Publicos_2020.csv",  context=ssl)

data = np.genfromtxt(io.BytesIO(http_request.read()), delimiter=";", dtype=str, encoding="utf-8-sig", unpack=True)

data_transposed = data.T

for column in data_transposed:
    print(column) """

#3.1.12
""" import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

ruta_archivo = 'https://www.consejotransparencia.cl/transparencia_activa/datoabierto/archivosFiscalizacion/BBDD_Funcionarios_Publicos_2020.csv'

columnas_deseadas = ['ID_Encuestado', 'P1_1', 'P2_4']
data = pd.read_csv(ruta_archivo, usecols=columnas_deseadas, delimiter=';', encoding='utf-8')

print(data.head()) """

#3.1.13
""" import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

ruta_archivo = 'https://www.consejotransparencia.cl/transparencia_activa/datoabierto/archivosFiscalizacion/BBDD_Funcionarios_Publicos_2020.csv'

df = pd.read_csv(ruta_archivo, delimiter=';', encoding='utf-8')

valor = df.loc[319, 'P7_4']

print("El valor en la fila 319 de la columna P7_4 es:", valor) """

#3.1.14
""" import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

ruta_archivo = 'https://www.consejotransparencia.cl/transparencia_activa/datoabierto/archivosFiscalizacion/BBDD_Funcionarios_Publicos_2020.csv'

df = pd.read_csv(ruta_archivo, delimiter=';', encoding='utf-8')

ruta_guardado = 'C:\\Users\\josei\\Documents\\NTT DATA CLASES\\Área 3 - Material de clases\\Modulo_1\\Funcionarios_Chile.csv'  

df.to_csv(ruta_guardado, index=False, sep=';', encoding='utf-8')

print(f"El archivo CSV ha sido guardado en: {ruta_guardado}") """




