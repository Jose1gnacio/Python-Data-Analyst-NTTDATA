from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score, KFold, train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, make_scorer, recall_score, f1_score, roc_auc_score, confusion_matrix

# Cargar el dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Crear un modelo de regresión logística
model = LogisticRegression(max_iter=10000)

# Definir el objeto KFold para 3 splits
kfold = KFold(n_splits=3, shuffle=True, random_state=42)

#3.9.1
""" # Calcular cross-validation score con métrica de accuracy
scores = cross_val_score(model, X, y, cv=kfold, scoring='accuracy')

# Mostrar los scores obtenidos
print("Cross-validation scores:", scores)
print("Mean accuracy:", scores.mean()) """

#3.9.2
""" # Calcular cross-validation score con métrica de precision
# Definir scorer para precision
scorer = make_scorer(precision_score, average='binary')

# Calcular cross-validation scores
scores = cross_val_score(model, X, y, cv=kfold, scoring=scorer)

# Mostrar los scores obtenidos
print("Cross-validation scores (precision):", scores)
print("Mean precision:", scores.mean()) """

#3.9.3
""" # Calcular cross-validation score con métrica de recall
# Definir scorer para recall
scorer = make_scorer(recall_score, average='binary')

# Calcular cross-validation scores
scores = cross_val_score(model, X, y, cv=kfold, scoring=scorer)

# Mostrar los scores obtenidos
print("Cross-validation scores (recall):", scores)
print("Mean recall:", scores.mean()) """

#3.9.4
""" # Calcular cross-validation score con métrica de F1-score
# Definir scorer para F1-score
scorer = make_scorer(f1_score, average='binary')

# Calcular cross-validation scores
scores = cross_val_score(model, X, y, cv=kfold, scoring=scorer)

# Mostrar los scores obtenidos
print("Cross-validation scores (F1-score):", scores)
print("Mean F1-score:", scores.mean()) """

#3.9.5
""" # Calcular cross-validation scores con métrica AUC-ROC
scores = cross_val_score(model, X, y, cv=kfold, scoring='roc_auc')

# Mostrar los scores obtenidos
print("Cross-validation scores (AUC-ROC):", scores)
print("Mean AUC-ROC:", scores.mean()) """

#3.9.6
""" # Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un modelo de regresión logística con max_iter aumentado
model = LogisticRegression(max_iter=1000)  # Aumentar el número máximo de iteraciones

# Entrenar el modelo con los datos de entrenamiento
model.fit(X_train, y_train)

# Predecir con los datos de prueba
y_pred = model.predict(X_test)

# Calcular la matriz de confusión
conf_matrix = confusion_matrix(y_test, y_pred)

# Mostrar la matriz de confusión
print("Matriz de Confusión:")
print(conf_matrix) """

""" from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Cargar el dataset
data = load_iris()
X = data.data
y = data.target

#3.9.8
# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un modelo de regresión logística
model = LogisticRegression(max_iter=1000)  # Aumentar el número máximo de iteraciones si es necesario

# Entrenar el modelo con los datos de entrenamiento
model.fit(X_train, y_train)

# Predecir con los datos de prueba
y_pred = model.predict(X_test)

# Calcular el error cuadrático medio (MSE)
mse = mean_squared_error(y_test, y_pred)

# Mostrar el error cuadrático medio
#print("Error cuadrático medio:", mse) """

#3.9.9
""" # Calcular el error absoluto medio (MAE)
mae = mean_absolute_error(y_test, y_pred)

# Mostrar el error absoluto medio
print("Error absoluto medio:", mae)
 """

#3.9.10
""" r2_score = model.score(X_test, y_test)
print(f"Coeficiente de determinación (Precisión del modelo): {r2_score}") """

""" #3.9.12
from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.tree import DecisionTreeClassifier

# Cargar el dataset
data = load_iris()
X = data.data
y = data.target

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definir el modelo de árbol de decisión
model = DecisionTreeClassifier()

# Definir el grid de parámetros a probar
param_grid = {
    "max_depth": [4],  # Profundidad máxima del árbol
    "criterion": ["entropy"]  # Criterio para la división de nodos
}

# Configurar Grid Search con validación cruzada (cross-validation)
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5)

# Ejecutar Grid Search para encontrar la mejor configuración
grid_search.fit(X_train, y_train)

# Obtener los resultados
best_score = grid_search.best_score_
best_params = grid_search.best_params_

# Mostrar resultados
print("Mejor puntuación del modelo:", best_score)
print("Mejor configuración de parámetros:", best_params)
 """

#3.9.13
from sklearn.datasets import load_iris
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from sklearn.tree import DecisionTreeClassifier
from scipy.stats import randint

# Cargar el dataset
data = load_iris()
X = data.data
y = data.target

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definir el modelo de árbol de decisión
model = DecisionTreeClassifier()

# Definir el grid de parámetros a probar
param_dist = {
    "max_depth": [4],  # Profundidad máxima del árbol
    "criterion": ["entropy"]  # Criterio para la división de nodos
}

# Configurar Randomized Search con validación cruzada (cross-validation)
random_search = RandomizedSearchCV(estimator=model, param_distributions=param_dist, n_iter=10, cv=5, scoring='accuracy', random_state=42)

# Ejecutar Randomized Search para encontrar la mejor configuración
random_search.fit(X_train, y_train)

# Obtener los resultados
best_score = random_search.best_score_
best_params = random_search.best_params_

# Mostrar resultados
print("Mejor puntuación del modelo:", best_score)
print("Mejor configuración de parámetros:", best_params)

