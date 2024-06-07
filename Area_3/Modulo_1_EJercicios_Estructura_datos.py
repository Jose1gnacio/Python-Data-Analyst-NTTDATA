#3.2.1
""" import numpy as np

my_array = np.arange(9,25)

print(f'Array con los valores solicitados: {my_array}') """

#3.2.2
""" import numpy as np

my_array = np.arange(9,25)

print(f'Array con los valores solicitados: {my_array.size}') """

#3.2.3
""" import numpy as np

my_array = np.arange(9,25).reshape(2,8)

print(f'Array con los datos solicitados: {my_array}') """

#3.2.4
""" import numpy as np

my_array = np.arange(9,25).reshape(4,4)

print(f'Array con los datos solicitados: {my_array}') """

#3.2.5
""" import numpy as np

valores = [3, 5, 6, 1, 7, 9, 2, 3, 6]
my_array = np.array(valores)
for i in range(0, my_array.size):
    if my_array[i] > 5:
        print("A") """

#3.2.6
""" import numpy as np

array_1 = np.array([1, 2, 3])
array_2 = np.array([4, 5, 6])

array_3 = np.divide(array_1, array_2)

array_final = np.array([array_1, array_2, array_3])

print(array_final) """

#3.2.7
""" import numpy as np

array_1 = np.array([1, 2, 3])
array_2 = np.array([4, 5, 6])

arr_mult_1 = array_1 * 6
arr_mult_2 = array_2 * 6

print(f'Array 1 multiplicado por 6: {arr_mult_1} \nArray 2 multiplicado por 6: {arr_mult_2}') """

#3.2.8
""" import numpy as np

array_1 = np.array([1, 2, 3])
array_2 = np.array([4, 5, 6])

arr_mult_1 = array_1 * 6
arr_mult_2 = array_2 * 6

dim_array_1_mult = arr_mult_1.shape
dim_array_2_mult = arr_mult_2.shape

tipo_elementos_array_1_mult = arr_mult_1.dtype
tipo_elementos_array_2_mult = arr_mult_2.dtype

print(f'Dimensión de Array 1 multiplicado por 6: {dim_array_1_mult}')
print(f'Dimensión de Array 2 multiplicado por 6: {dim_array_2_mult}')
print(f'Tipo de los elementos de Array 1 multiplicado por 6: {tipo_elementos_array_1_mult}')
print(f'Tipo de los elementos de Array 2 multiplicado por 6: {tipo_elementos_array_2_mult}') """

#3.2.9
""" import pandas as pd

datos = [4, 8, 6, 2, 7, 8, 2, 1, 9]
serie = pd.Series(datos)

print(serie) """

#3.2.10
""" import pandas as pd

datos = [4, 8, 6, 2, 7, 8, 2, 1, 9]

indices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

serie = pd.Series(datos, index=indices)

print(serie) """

#3.2.11
""" import pandas as pd

datos = [4, 8, 6, 2, 7, 8, 2, 1, 9]

indices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

serie = pd.Series(datos, index=indices)

valor_e = serie['e']

print(valor_e) """

#3.2.12
""" import pandas as pd

serie_a = pd.Series([1, 3, 5, 8])
serie_b = pd.Series([4, 8, 3, 9])

resultado = serie_a % serie_b

print(resultado) """

#3.2.13
""" import pandas as pd

serie_a = pd.Series([1, 4, 6, 8])

resultado = serie_a * 4

print(resultado) """

#3.2.14
""" import pandas as pd

serie_a = pd.Series([4, 8, 6, 2, 7, 8, 2, 1, 9])
lista = []

for i in range(len(serie_a) - 1):
    element = serie_a[i] + serie_a[i +1]
    lista.append(element)

serie_resultado = pd.Series(lista)

print(serie_resultado) """

#3.2.15
""" import pandas as pd

data = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    'Ventas': [10000, 15200, 14300, 25800, 2560, 12780, 32500, 23624, 12000, 15858, 23250, 11630],
    'Gastos': [6500, 6500, 6500, 7850, 6500, 8250, 6500, 9252, 6500, 10250, 12450, 13000],
    'Cobrado': ['S', 'N', 'N', 'S', 'S', 'N', 'S', 'S', 'S', 'N', 'S', 'N']
}

df = pd.DataFrame(data)

print(df) """

#3.2.16
""" import pandas as pd

data = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    'Ventas': [10000, 15200, 14300, 25800, 2560, 12780, 32500, 23624, 12000, 15858, 23250, 11630],
    'Gastos': [6500, 6500, 6500, 7850, 6500, 8250, 6500, 9252, 6500, 10250, 12450, 13000],
    'Cobrado': ['S', 'N', 'N', 'S', 'S', 'N', 'S', 'S', 'S', 'N', 'S', 'N']
}

df = pd.DataFrame(data)

#Pregunta 1: ¿Cuántas filas tiene el DataFrame?
num_filas = len(df)
print("Número de filas:", num_filas)

#Pregunta 2: ¿Cuáles son las columnas que los forman?
columnas = df.columns
print("Columnas:", columnas)

#Pregunta 3: ¿Cuánto espacio ha utilizado en memoria?
espacio_memoria = df.memory_usage().sum()
print("Espacio utilizado en memoria (bytes):", espacio_memoria)

#Pregunta 4: ¿Cuál es la media de las ventas anuales?
media_ventas = df['Ventas'].mean()
print("Media de las ventas anuales:", media_ventas)

#Pregunta 5: Teniendo en cuenta solo las columnas Ventas y Gastos, 
#al final de año, ¿crees que la empresa es rentable?
total_ventas = df['Ventas'].sum()
total_gastos = df['Gastos'].sum()
rentabilidad = total_ventas - total_gastos

print("Total Ventas:", total_ventas)
print("Total Gastos:", total_gastos)
print("Rentabilidad:", rentabilidad)

if rentabilidad > 0:
    print("La empresa es rentable.")
else:
    print("La empresa no es rentable.") """

#3.2.17
""" import pandas as pd

data = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    'Ventas': [10000, 15200, 14300, 25800, 2560, 12780, 32500, 23624, 12000, 15858, 23250, 11630],
    'Gastos': [6500, 6500, 6500, 7850, 6500, 8250, 6500, 9252, 6500, 10250, 12450, 13000],
    'Cobrado': ['S', 'N', 'N', 'S', 'S', 'N', 'S', 'S', 'S', 'N', 'S', 'N']
}

df = pd.DataFrame(data)

media_ventas_anuales = df['Ventas'].mean()

meses_altos_ventas = df[df['Ventas'] > media_ventas_anuales]

print("Meses con ventas por encima de la media anual: ", meses_altos_ventas) """

#3.2.18
""" import pandas as pd

data = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    'Ventas': [10000, 15200, 14300, 25800, 2560, 12780, 32500, 23624, 12000, 15858, 23250, 11630],
    'Gastos': [6500, 6500, 6500, 7850, 6500, 8250, 6500, 9252, 6500, 10250, 12450, 13000],
    'Cobrado': ['S', 'N', 'N', 'S', 'S', 'N', 'S', 'S', 'S', 'N', 'S', 'N']
}

df = pd.DataFrame(data)

meses_pendientes_cobro = df[df['Cobrado'] == 'N']

print("Meses con facturas pendientes de cobro: ", meses_pendientes_cobro) """

#3.2.19
""" import pandas as pd

data = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    'Ventas': [10000, 15200, 14300, 25800, 2560, 12780, 32500, 23624, 12000, 15858, 23250, 11630],
    'Gastos': [6500, 6500, 6500, 7850, 6500, 8250, 6500, 9252, 6500, 10250, 12450, 13000],
    'Cobrado': ['S', 'N', 'N', 'S', 'S', 'N', 'S', 'S', 'S', 'N', 'S', 'N']
}

df = pd.DataFrame(data)

meses_gastos_mayores_ventas = df[df['Gastos'] > df['Ventas']]

print("Meses en los que los gastos han sido mayores que las ventas: ", meses_gastos_mayores_ventas) """

#3.2.20
import pandas as pd

data = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    'Ventas': [10000, 15200, 14300, 25800, 2560, 12780, 32500, 23624, 12000, 15858, 23250, 11630],
    'Gastos': [6500, 6500, 6500, 7850, 6500, 8250, 6500, 9252, 6500, 10250, 12450, 13000],
    'Cobrado': ['S', 'N', 'N', 'S', 'S', 'N', 'S', 'S', 'S', 'N', 'S', 'N']
}
df_original = pd.DataFrame(data)
nueva_data = {
    'Mes': df_original['Mes'],
    'Ventas': df_original['Ventas'],
    'Gastos': df_original['Gastos'],
    'Cobrado': df_original['Cobrado'],
    'Beneficio': [0] * len(df_original)  
}
df_con_beneficio = pd.DataFrame(nueva_data)
print(df_con_beneficio)