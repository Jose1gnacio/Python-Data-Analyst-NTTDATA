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
import numpy as np

valores = [3, 5, 6, 1, 7, 9, 2, 3, 6]
my_array = np.array(valores)
for i in range(0, my_array.size):
    if my_array[i] > 5:
        print("A")