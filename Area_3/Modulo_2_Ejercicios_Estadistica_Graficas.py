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
""" datos = [
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
plt.show() """

#3.3.7
""" data = {
    'Artículos': ['Art0001', 'Art0002', 'Art0003', 'Art0004', 'Art0005'],
    'Pedidos': [325, 125, 205, 54, 186],
    'Entregado': ['S', 'S', 'N', 'N', 'S'],
    'Facturación': [8125, 9375, 13325, 18900, 9300]
}
df = pd.DataFrame(data)

media_facturacion = df['Facturación'].mean()
varianza_pedidos = df['Pedidos'].var()
covarianza = df[['Pedidos', 'Facturación']].cov().loc['Pedidos', 'Facturación']
entregados = df[df['Entregado'] == 'S']
media_facturacion_entregados = entregados['Facturación'].mean()
media_pedidos_entregados = entregados['Pedidos'].mean()

print("Media de facturación:", media_facturacion)
print("Varianza de pedidos:", varianza_pedidos)
print("Covarianza entre pedidos y facturación:", covarianza)
print("Media de facturación de artículos entregados:", media_facturacion_entregados)
print("Media de pedidos de artículos entregados:", media_pedidos_entregados) """

#3.3.8
""" notas_lengua = [5, 7, 6, 2, 8, 9, 3, 4, 1, 9, 5, 4, 6, 4, 8, 7, 6, 2, 8, 9]
notas_matematicas = [7, 8, 5, 6, 8, 3, 2, 9, 9, 6, 1, 5, 7, 3, 5, 4, 5, 9, 7, 6]
correlacion = np.corrcoef(notas_lengua, notas_matematicas)[0, 1]
print(f"Coeficiente de correlación entre las notas de lengua y matemáticas: {correlacion}")
plt.scatter(notas_lengua, notas_matematicas, color='blue', marker='o', alpha=0.5)
plt.title('Gráfico de dispersión: Notas de lengua vs. Notas de matemáticas')
plt.xlabel('Notas de lengua')
plt.ylabel('Notas de matemáticas')
plt.grid(True)
plt.tight_layout()
plt.show() """

#3.3.9
""" notas_lengua = [5, 7, 6, 2, 8, 9, 3, 4, 1, 9, 5, 4, 6, 4, 8, 7, 6, 2, 8, 9]
notas_ingles = [7, 9, 7, 5, 9, 9, 5, 6, 3, 9, 7, 6, 8, 6, 9, 8, 8, 4, 9, 9]
correlacion = np.corrcoef(notas_lengua, notas_ingles)[0, 1]
print(f"Coeficiente de correlación entre las notas de lengua y matemáticas: {correlacion}")
plt.scatter(notas_lengua, notas_ingles, color='blue', marker='o', alpha=0.5)
plt.title('Gráfico de dispersión: Notas de lengua vs. Notas de ingles')
plt.xlabel('Notas de lengua')
plt.ylabel('Notas de ingles')
plt.grid(True)
plt.tight_layout()
plt.show() """

#3.3.10
""" edades = [25, 36, 25, 20, 35, 24, 42, 44, 51, 32, 36, 36, 25, 29, 28, 25, 36, 37, 29, 44,
          42, 41, 40, 40, 42, 51, 25, 26, 28, 27, 32, 31, 30, 31, 39, 36, 36, 32, 23, 26,
          24, 27, 46, 46, 48]

intervalos = range(min(edades), max(edades) + 11, 10)

plt.hist(edades, bins=intervalos, edgecolor='black')
plt.title('Histograma de Edades en el Sector TIC')
plt.xlabel('Edades')
plt.ylabel('Frecuencia')
plt.show() """

#3.3.11
""" edades = [25, 36, 25, 20, 35, 24, 42, 44, 51, 32, 36, 36, 25, 29, 28, 25, 36, 37, 29, 44,
          42, 41, 40, 40, 42, 51, 25, 26, 28, 27, 32, 31, 30, 31, 39, 36, 36, 32, 23, 26,
          24, 27, 46, 46, 48]

box = plt.boxplot(edades, patch_artist=True, boxprops=dict(facecolor='lightblue', color='black'))
plt.boxplot(edades)
plt.title('Diagrama de Caja de Edades en el Sector TIC')
plt.xlabel('Grupo de Edades')
plt.ylabel('Edad')
plt.grid(True)
plt.show() """

#3.3.12
""" def solicitar_ventas():
    ventas_mensuales = []
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    
    for mes in meses:
        venta = float(input(f"Ingrese las ventas de {mes}: "))
        ventas_mensuales.append(venta)
    
    return meses, ventas_mensuales

def graficar_ventas(meses, ventas_mensuales):
    plt.figure(figsize=(10, 6))
    plt.bar(meses, ventas_mensuales, color='blue')
    plt.xlabel('Meses')
    plt.ylabel('Ventas')
    plt.title('Ventas mensuales por mes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    meses, ventas_mensuales = solicitar_ventas()
    graficar_ventas(meses, ventas_mensuales) """

#3.3.13
""" archivo_csv = r'C:\Users\josei\Documents\NTT DATA CLASES\Área 3 - Material de clases\Modulo_2\apellidos_mas_frecuentes_pais_Argentina.csv'
df = pd.read_csv(archivo_csv)

plt.boxplot(df['porcentaje_de_poblacion_portadora'])
plt.title('Porcentaje de población portadora por apellido (Argentina)')
plt.ylabel('Porcentaje de población portadora (%)')
plt.grid(True)
plt.show() """


