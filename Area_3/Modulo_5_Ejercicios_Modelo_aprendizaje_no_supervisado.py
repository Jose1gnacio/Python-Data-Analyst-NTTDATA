""" import matplotlib.pyplot as plt
from sklearn.datasets import make_gaussian_quantiles
from sklearn.cluster import KMeans

#Creamos el conjunto de datos con make_gaussian_quantiles
X, y = make_gaussian_quantiles(n_samples=150, random_state=42)

#Inicializamos el algoritmo k-means con k = 3 clústeres
kmeans = KMeans(n_clusters=3, random_state=0)

#Entrenamos el modelo con los datos
kmeans.fit(X)

#Predecimos la asignación del clúster para cada punto de datos
labels = kmeans.predict(X)

#Obtenemos los centroides de los clústeres
centroides = kmeans.cluster_centers_
print("Centroides:\n", centroides)

#Visualizamos los datos y los centroides de los clústeres en un gráfico de dispersión
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centroides[:, 0], centroides[:, 1], marker="x", s=150, linewidths=3, color="r")
plt.title('Clustering K-Means con Centroides')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.colorbar()
plt.show()
 """

#3.12.3
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_gaussian_quantiles
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Creamos el conjunto de datos con make_gaussian_quantiles
X, y = make_gaussian_quantiles(n_samples=150, n_features=2, n_classes=3)

# Creamos una lista para almacenar los valores de Silhouette
silhouette_scores = []

# Probamos diferentes números de clústeres (de 2 a 6 por ejemplo)
for n_clusters in range(2, 7):
    # Inicializamos el algoritmo k-means con el número de clústeres actual
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    kmeans.fit(X)
    
    # Calculamos las etiquetas de los clústeres y el score de Silhouette
    labels = kmeans.labels_
    silhouette_avg = silhouette_score(X, labels)
    silhouette_scores.append(silhouette_avg)
    
    print(f"Número de clústeres = {n_clusters}, Silhouette Score = {silhouette_avg}")

# Graficamos el score de Silhouette para cada número de clústeres probado
plt.plot(range(2, 7), silhouette_scores, marker='o')
plt.xlabel('Número de Clústeres')
plt.ylabel('Score de Silhouette')
plt.title('Score de Silhouette para diferentes números de clústeres')
plt.xticks(np.arange(2, 7, step=1))
plt.show()

# Obtenemos el número óptimo de clústeres basado en el máximo score de Silhouette
optimal_n_clusters = np.argmax(silhouette_scores) + 2  # Sumamos 2 porque empezamos desde 2 clústeres
print(f"Número óptimo de clústeres según Silhouette: {optimal_n_clusters}")
