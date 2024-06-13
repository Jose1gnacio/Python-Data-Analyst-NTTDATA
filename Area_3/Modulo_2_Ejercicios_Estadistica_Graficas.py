import statistics
import numpy as np

#3.3.1


# Datos de las puntuaciones
puntuaciones = [5, 3, 6, 5, 4, 5, 7, 8, 6, 5, 6, 8, 3, 4, 5, 4, 8, 5, 5, 4]

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
print(f"g) El rango intercuartílico: {rango_intercuartilico}")
