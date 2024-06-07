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
import pandas as pd

datos = [4, 8, 6, 2, 7, 8, 2, 1, 9]

indices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

serie = pd.Series(datos, index=indices)

valor_e = serie['e']

print(valor_e)

