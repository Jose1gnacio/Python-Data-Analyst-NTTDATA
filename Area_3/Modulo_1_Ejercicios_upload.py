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
import numpy as np

ruta_archivo = 'puntos_de_acceso_wifi_Mexico.csv'

# Cargar el archivo CSV con NumPy
data = np.genfromtxt(ruta_archivo, delimiter=',', dtype=None, encoding='utf-8', names=True)

# Mostrar los datos
print(data)        