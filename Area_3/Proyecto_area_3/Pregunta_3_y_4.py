# Importar librerías necesarias
import pandas as pd
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el fichero Delitos_Chicago.csv
archivo_csv = r'C:\Users\josei\Documents\NTT DATA CLASES\Área 3 - Material de clases\Delitos_Chicago.csv'
df_delitos = pd.read_csv(archivo_csv, sep=",").sample(frac=0.01, random_state=42)

# Mostramos los primeros registros para tener constancia del tipo de datos:
#print(df_delitos.head())

# Comprobamos el tipo de las variables del fichero:
#print(df_delitos.info())

# Comprobamos valor duplicados
duplicados = df_delitos.duplicated()
num_duplicados = duplicados.sum()
#print(f"Número de filas duplicadas: {num_duplicados}")

# Comprobamos los elementos nulos:
#print(df_delitos.isnull().sum())

# Eliminamos los registros con valores nulos:
df_delitos = df_delitos.dropna()

# Comprobamos que se han eliminado correctamente:
#print(df_delitos.isnull().sum())

# Cambiamos los booleanos por 0 y 1:
df_delitos["Arrest"] = df_delitos["Arrest"].apply(lambda X:0 if X == False else 1)
df_delitos["Domestic"] = df_delitos["Domestic"].apply(lambda X:0 if X == False else 1)

# Cambiamos el tipo de la columna Primary Type a categórica:
df_delitos["Primary Type"] = df_delitos["Primary Type"].astype("category")

# Y le asignamos un valor numérico: 
le = preprocessing.LabelEncoder()
le.fit(df_delitos["Primary Type"])

# Imprimimos las clases que se van a convertir en números:
#print(le.classes_)
df_delitos["Primary Type"] = le.transform(df_delitos["Primary Type"])

# Borramos las columnas no numéricas: 
df_delitos = df_delitos.drop(df_delitos.select_dtypes(include = ["object"]), axis = 1)

# Borramos las variables ID y año, ya que todos son 2015 y no aportan información de valor:
df_delitos = df_delitos.drop(["ID", "Year"], axis = 1)
#print(df_delitos.info())

# Vemos la relación entre variables con la matriz de Pearson:
# Generamos la matriz de correlación de Pearson:
corr_pearson = df_delitos.corr(method = "pearson")

# Mostramos la matriz de correlación de Pearson:
""" plt.figure(figsize = (14, 10))
sns.heatmap(corr_pearson, annot = True, cmap = "coolwarm")
plt.title("Matriz de Correlación de Pearson")
plt.show() """

# Con Feature importance vemos qué variables independientes están más relacionadas con la variable objetivo:
model = ExtraTreesClassifier()
model.fit(X = df_delitos.loc[:, df_delitos.columns != "Domestic"], y = df_delitos["Domestic"])
#print("Importancia de variables con ExtraTreesClassifier:")
#print(model.feature_importances_)

# Ajustamos:
X = df_delitos.drop("Domestic", axis = 1)
y = df_delitos["Domestic"]

# Dividir el dataset en conjuntos de entrenamiento y prueba:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

# Creamos el modelo y lo ajustamos:
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Mostramos la puntuación del modelo:
clf_score = clf.score(X, y)
#print(f"Puntuación: {clf_score}.")

# Predecimos en el conjunto de prueba:
y_pred = clf.predict(X_test)
#print(f"Predicción: {y_pred}.")

# Evaluamos los errores:

# Importamos las librerías:
from sklearn.metrics import accuracy_score, confusion_matrix

# Vemos la exactitud del algoritmo y lo mostramos:
accuracy = accuracy_score(y_test, y_pred)
#print(f"La exactitud es: {accuracy}.")

# Calculamos la matriz de confusión y la mostramos:
conf_matrix = confusion_matrix(y_test, y_pred)
#print(f"Matriz de confusión:\n{conf_matrix}")


## EJERCICIO 4
# Plantead una segmentación analítica de delitos atendiendo a sus características. 


# Selección de características relevantes para la segmentación:
X_cluster = df_delitos[["Arrest", "Domestic", "Beat", "District", "Ward", "Community Area"]]

# Para determinar la cantidad óptima de clusters o segmentos, utilizaremos dos métodos principales. 
# Estos métodos, a través de sus gráficos, nos ayudarán a identificar la cantidad de clusters para el análisis.

# 1. Método del codo
""" inertias = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_cluster)
    inertias.append(kmeans.inertia_)

plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), inertias, marker='o')
plt.xlabel('Número de clusters')
plt.ylabel('Inercia')
plt.title('Método del codo para encontrar el número óptimo de clusters')
plt.show() """


# 2. Método de la silueta
silhouette_scores = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_cluster)
    score = silhouette_score(X_cluster, kmeans.labels_)
    silhouette_scores.append(score)

plt.figure(figsize=(10, 6))
plt.plot(range(2, 11), silhouette_scores, marker='o')
plt.xlabel('Número de clusters')
plt.ylabel('Puntaje de silueta')
plt.title('Método de la silueta para encontrar el número óptimo de clusters')
plt.show()

""" ## 1.- ¿Cuántos segmentos tiene la solución planteada?

# Según el análisis de los gráficos del método del codo y del método de la silueta, 
# determinamos que la cantidad óptima de clusters a utilizar será de 4.

# Creamos el modelo de K-Means con 4 clusters
kmeans = KMeans(n_clusters = 4, random_state = 42)
df_delitos["Cluster"] = kmeans.fit_predict(X_cluster)
cluster_means = df_delitos.groupby("Cluster").mean()
#print(cluster_means)

## 2.- ¿Qué características tienen los delitos de cada segmento?

# Características de cada cluster de K-Means:
print("\nSegmentación de delitos:")
print(f"1. ¿Cuántos segmentos tiene la solución planteada?")
print(f"- La solución planteada tiene {cluster_means.shape[0]} segmentos.")
 
print("\n2. ¿Qué características tienen los delitos de cada segmento?")
for cluster_id, cluster_info in cluster_means.iterrows():
    print(f"\nSegmento {cluster_id}:")
    print("- Características principales:")
    top_features = cluster_info.sort_values(ascending = False)[:5]  # Mostrar las 5 características principales.
    for feature, value in top_features.items():
        print(f"  - {feature}: {value:.3f}") """