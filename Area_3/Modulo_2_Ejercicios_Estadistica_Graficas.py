import statistics
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
""" datos = {
    'D_ejer1': [5, 3, 6, 5],
    'D_ejer2': [4, 5, 7, 8]
}

df = pd.DataFrame(datos)

#La media
media = df.mean()

#La mediana
mediana = df.median()

#Los cuartiles Q2 y Q3
Q2 = df.quantile(0.5)
Q3 = df.quantile(0.75)

#Los percentiles P40 y P90
P40 = df.quantile(0.4)
P90 = df.quantile(0.9)

#La desviación típica
desviacion_tipica = df.std()

#La varianza
varianza = df.var()

#La covarianza
covarianza = df.cov()

# h) La correlación de Pearson
correlacion = np.corrcoef([datos['D_ejer1'], datos['D_ejer2']])

# i) La matriz de correlación de Pearson
matriz_correlacion = df.corr(method = 'pearson')
sns.heatmap(matriz_correlacion, annot= True, cmap = 'coolwarm')

# Mostrar los resultados
print(f"a) La media: {media}")
print(f"b) La mediana: {mediana}")
print(f"c) Cuartiles Q2 y Q3: Q2={Q2}, Q3={Q3}")
print(f"d) Percentiles P40 y P90: P40={P40}, P90={P90}")
print(f"e) La desviación típica: {desviacion_tipica}")
print(f"f) La varianza: {varianza}")
print(f"g) La covarianza: {covarianza}")
print(f"h) La correlación de Pearson: {correlacion}")
print("i) Matriz de correlación de Pearson:")
print(matriz_correlacion)
plt.title('Matriz de Correlación de Pearson')
plt.show() """

#3.3.3
""" valores = list(range(25, 46))
resultado = np.median(valores)
print(f"La mediana es {resultado}") """

#3.3.4
""" hijos = np.array([0]*5 + [1]*6 + [2]*8 + [3]*4 + [4]*2)

#media
media = np.mean(hijos)

#varianza
varianza = np.var(hijos)

print(f"La media es {media}")
print(f"La varianza es {varianza}") """

#3.3.5
""" impuestos = np.array([0.16, 0.2, 0.06, 0.06, 0.07, 0.17, 0.06, 0.22])

q1 = np.percentile(impuestos, 25)
q2 = np.percentile(impuestos, 50)
q3 = np.percentile(impuestos, 75)

print(f"Q1: {q1}")
print(f"Q2: {q2}")
print(f"Q3: {q3}") """

#3.3.6
datos = [
    [4, 5, 5, 1, 7, 4],
    [3, 2, 4, 4, 3, 6],
    [6, 4, 3, 3, 4, 5],
    [5, 2, 4, 7, 3, 6],
    [2, 1, 3, 7, 3, 1]
]
df = pd.DataFrame(datos)
corr_pearson = df.corr(method='pearson')
sns.heatmap(corr_pearson, annot=True, cmap='coolwarm')
print(corr_pearson)
plt.title('Matriz de Correlación de Pearson')
plt.show()


