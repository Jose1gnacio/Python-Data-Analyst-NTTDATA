import statistics
import numpy as np
import pandas as pd

#3.3.1
""" puntuaciones = [5, 3, 6, 5, 4, 5, 7, 8, 6, 5, 6, 8, 3, 4, 5, 4, 8, 5, 5, 4]

#La media
media = np.mean(puntuaciones)

#La mediana
mediana = np.median(puntuaciones)

#Los cuartiles Q1, Q2 y Q3
Q1 = np.percentile(puntuaciones, 25)
Q2 = np.percentile(puntuaciones, 50)  # Q2 es la mediana
Q3 = np.percentile(puntuaciones, 75)

#Los percentiles P30 y P80
P30 = np.percentile(puntuaciones, 30)
P80 = np.percentile(puntuaciones, 80)

#La desviación típica
desviacion_tipica = np.std(puntuaciones)

#La varianza
varianza = np.var(puntuaciones)

#El rango intercuartílico
rango_intercuartilico = Q3 - Q1

print(f"a) La media: {media}")
print(f"b) La mediana: {mediana}")
print(f"c) Los cuartiles Q1, Q2 y Q3: Q1={Q1}, Q2={Q2}, Q3={Q3}")
print(f"d) Los percentiles P30 y P80: P30={P30}, P80={P80}")
print(f"e) La desviación típica: {desviacion_tipica}")
print(f"f) La varianza: {varianza}")
print(f"g) El rango intercuartílico: {rango_intercuartilico}") """

#3.3.2
# Crear el diccionario de datos
datos = {
    'D_ejer1': [5, 3, 6, 5],
    'D_ejer2': [4, 5, 7, 8]
}

# Convertir el diccionario en un DataFrame de Pandas
df = pd.DataFrame(datos)

# a) La media
media = df.mean()

""" # b) La mediana
mediana = df.median().median()

# c) Los cuartiles Q2 y Q3
Q2 = df.quantile(0.5).mean()  # Q2 es la mediana de la mediana de cada serie
Q3 = df.quantile(0.75).mean()

# d) Los percentiles P40 y P90
P40 = df.quantile(0.4).mean()
P90 = df.quantile(0.9).mean()

# e) La desviación típica
desviacion_tipica = df.stack().std()

# f) La varianza
varianza = df.stack().var()

# g) La covarianza
covarianza = df['D_ejer1'].cov(df['D_ejer2'])

# h) La correlación de Pearson
correlacion = df['D_ejer1'].corr(df['D_ejer2'])

# i) La matriz de correlación de Pearson
matriz_correlacion = df.corr()
 """
# Mostrar los resultados
print(f"a) La media: {media}")
""" print(f"b) La mediana: {mediana}")
print(f"c) Cuartiles Q2 y Q3: Q2={Q2}, Q3={Q3}")
print(f"d) Percentiles P40 y P90: P40={P40}, P90={P90}")
print(f"e) La desviación típica: {desviacion_tipica}")
print(f"f) La varianza: {varianza}")
print(f"g) La covarianza: {covarianza}")
print(f"h) La correlación de Pearson: {correlacion}")
print("i) Matriz de correlación de Pearson:")
print(matriz_correlacion)
 """

