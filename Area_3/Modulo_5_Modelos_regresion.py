""" from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

#Cargar el dataset
diabetes = load_diabetes()
X = diabetes.data[:, np.newaxis, 0]  #Tomar la primera columna como variable independiente
y = diabetes.target

#Inicializar el modelo de regresión lineal
model = LinearRegression()

#Ajustar el modelo
model.fit(X, y)

#Obtener coeficientes y puntaje de ajuste
coeficiente = model.coef_[0]
intercepto = model.intercept_
score = model.score(X, y)

print(f"Coeficiente: {coeficiente}")
print(f"Intercepto: {intercepto}")
print(f"Puntaje de ajuste (R^2): {score}")

plt.scatter(X, y, color="blue")
plt.plot(X, model.predict(X), color="red")
plt.xlabel("X")
plt.ylabel("Y")
plt.show() """

""" #3.11.2
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

#Cargar el dataset
diabetes = load_diabetes()
X = diabetes.data[:, :2]  # Tomar las dos primeras columnas como variables independientes
y = diabetes.target

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.2, random_state=42)

#Inicializar el modelo de regresión lineal
model = LinearRegression()

#Ajustar el modelo
model.fit(X_train, y_train)

#Obtener coeficientes y puntaje de ajuste
coeficientes = model.coef_
intercepto = model.intercept_
score = model.score(X, y)

print(f"Coeficientes: {coeficientes}")
print(f"Intercepto: {intercepto}")

y_pred = model.predict(X_test)

#Graficar los datos y la línea ajustada por el modelo
plt.scatter(y_test, y_pred, color="blue")
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color="red", linewidth=2, label="Predicción del modelo")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
 """

""" #3.11.4
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Cargar el dataset
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar el modelo de regresión logística
model = LogisticRegression(max_iter=1000)  # Aumentamos el número máximo de iteraciones para asegurar convergencia

# Ajustar el modelo
model.fit(X_train, y_train)

# Predecir en el conjunto de prueba
y_pred = model.predict(X_test)

# Calcular la precisión del modelo
precision = accuracy_score(y_test, y_pred)

print(f"Precisión del modelo de regresión logística: {precision}")
 """

#3.11.5
""" from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge

#Cargar el dataset
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

#Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Inicializar el modelo de regresión Ridge
ridge = Ridge(alpha=0.1)  # alpha es el parámetro de regularización

#Ajustar el modelo
ridge.fit(X_train, y_train)

#Predecir en el conjunto de prueba
y_pred = ridge.predict(X_test)

#Calcular la puntuación (R^2) del modelo en el conjunto de prueba
score = ridge.score(X_test, y_test)

print(f"Puntuación del modelo (R^2): {score}")
print(f"Coeficientes: \n{ridge.coef_}")
print(f"Término independiente: {ridge.intercept_}") """

#3.11.6
""" from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import r2_score

#Cargar el dataset
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

#Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Inicializar el modelo de regresión Lasso
lasso = Lasso(alpha=0.1)  # alpha es el parámetro de regularización

#Ajustar el modelo
lasso.fit(X_train, y_train)

#Predecir en el conjunto de prueba
y_pred = lasso.predict(X_test)

#Calcular la puntuación (R^2) del modelo en el conjunto de prueba
score = lasso.score(X_test, y_test)

print(f"Puntuación del modelo (R^2): {score}")
print(f"Coeficientes: \n{lasso.coef_}")
print(f"Término independiente: {lasso.intercept_}") """

#3.11.8
""" from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np

#Cargar el dataset digits
digits = load_digits()
X = digits.data
y = digits.target

#Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Inicializar el modelo de árbol de decisión
clf = DecisionTreeClassifier(random_state=42)

#Ajustar el modelo con los datos de entrenamiento
clf.fit(X_train, y_train)

#Calcular la precisión del modelo en el conjunto de prueba
accuracy = clf.score(X_test, y_test)
print(f"Puntuación del modelo (precisión): {accuracy}")

#Generar datos aleatorios para una predicción
np.random.seed(0)  # Fijamos la semilla para reproducibilidad
random_data = np.random.rand(1, 64)  # Generamos datos aleatorios de la misma forma que los datos de entrada

#Realizar la predicción con datos aleatorios
prediction = clf.predict(random_data)
print(f"Predicción con datos aleatorios: {prediction}") """

#3.11.9
""" from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np

#Cargar el dataset digits
digits = load_digits()
X = digits.data
y = digits.target

#Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Inicializar el modelo de árbol de decisión con Gini y profundidad máxima de 8
clf = DecisionTreeClassifier(criterion='gini', max_depth=8, random_state=42)

#Ajustar el modelo con los datos de entrenamiento
clf.fit(X_train, y_train)

#Calcular la precisión del modelo en el conjunto de prueba
accuracy = clf.score(X_test, y_test)
print(f"Puntuación del modelo (precisión): {accuracy}")

#Generar datos aleatorios para una predicción
np.random.seed(0)  # Fijamos la semilla para reproducibilidad
random_data = np.random.rand(1, 64)  # Generamos datos aleatorios de la misma forma que los datos de entrada

#Realizar la predicción con datos aleatorios
prediction = clf.predict(random_data)
print(f"Predicción con datos aleatorios: {prediction}") """

#3.11.10
""" from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np

# Cargar el dataset digits
digits = load_digits()
X = digits.data
y = digits.target

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar el modelo Random Forest con 50 árboles y profundidad máxima de 10
rf = RandomForestClassifier(n_estimators=50, max_depth=10, random_state=42)

# Ajustar el modelo con los datos de entrenamiento
rf.fit(X_train, y_train)

# Calcular la precisión del modelo en el conjunto de prueba
accuracy = rf.score(X_test, y_test)
print(f"Puntuación del modelo (precisión): {accuracy}")

# Generar datos aleatorios para una predicción
np.random.seed(0)  # Fijamos la semilla para reproducibilidad
random_data = np.random.rand(1, 64)  # Generamos datos aleatorios de la misma forma que los datos de entrada

# Realizar la predicción con datos aleatorios
prediction = rf.predict(random_data)
print(f"Predicción con datos aleatorios: {prediction}") """

#3.11.11
""" from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np

#Cargar el dataset digits
digits = load_digits()
X = digits.data
y = digits.target

#Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Inicializar el modelo Random Forest con 10 árboles y profundidad máxima de 5
rf = RandomForestClassifier(n_estimators=10, max_depth=5, random_state=42)

#Ajustar el modelo con los datos de entrenamiento
rf.fit(X_train, y_train)

#Calcular la precisión del modelo en el conjunto de prueba
accuracy = rf.score(X_test, y_test)
print(f"Puntuación del modelo (precisión): {accuracy}")

#Generar datos aleatorios para una predicción
np.random.seed(0)  # Fijamos la semilla para reproducibilidad
random_data = np.random.rand(1, 64)  # Generamos datos aleatorios de la misma forma que los datos de entrada

#Realizar la predicción con datos aleatorios
prediction = rf.predict(random_data)
print(f"Predicción con datos aleatorios: {prediction}") """


#3.11.12
""" from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
import numpy as np

# Cargar el dataset digits
digits = load_digits()
X = digits.data
y = digits.target

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Corregir el nombre del parámetro n_estimators
clf = XGBClassifier(n_estimators=10, max_depth=5, random_state=42)

# Entrenar el modelo
clf.fit(X_train, y_train)

# Calcular y mostrar la puntuación de entrenamiento
train_score = clf.score(X_train, y_train)
print(f"Puntuación de entrenamiento: {train_score:.4f}")

# Calcular y mostrar la puntuación de prueba
test_score = clf.score(X_test, y_test)
print(f"Puntuación de prueba: {test_score:.4f}")

# Crear datos aleatorios y hacer una predicción
random_data = np.random.rand(1, 64) * 16
prediction = clf.predict(random_data)
print(f"Predicción con datos aleatorios: {prediction}") """

#3.11.13
""" from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import numpy as np

# Cargar el dataset digits
digits = load_digits()
X = digits.data
y = digits.target

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear el modelo Naive Bayes Multinomial
clf = MultinomialNB()

# Entrenar el modelo
clf.fit(X_train, y_train)

# Calcular y mostrar la puntuación de entrenamiento
train_score_nb = clf.score(X_train, y_train)
print(f"Puntuación de entrenamiento: {train_score_nb:.4f}")

# Calcular y mostrar la puntuación de prueba
test_score_nb = clf.score(X_test, y_test)
print(f"Puntuación de prueba: {test_score_nb:.4f}")

# Crear datos aleatorios y hacer una predicción
random_data = np.random.rand(1, 64) * 16
prediction_nb = clf.predict(random_data)
print(f"Predicción con datos aleatorios: {prediction_nb}") """

#3.11.14
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np

# Cargar el dataset digits
digits = load_digits()
X = digits.data
y = digits.target

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear el modelo SVC con el kernel predeterminado (RBF)
clf = SVC()

# Entrenar el modelo
clf.fit(X_train, y_train)

# Calcular y mostrar la puntuación de entrenamiento
train_score_svc = clf.score(X_train, y_train)
print(f"Puntuación de entrenamiento: {train_score_svc:.4f}")

# Calcular y mostrar la puntuación de prueba
test_score_svc = clf.score(X_test, y_test)
print(f"Puntuación de prueba: {test_score_svc:.4f}")

# Crear datos aleatorios y hacer una predicción
random_data = np.random.rand(1, 64) * 16
prediction_svc = clf.predict(random_data)
print(f"Predicción con datos aleatorios: {prediction_svc}")

# Obtener los vectores de soporte
support_vectors = clf.support_vectors_
print(f"Número de vectores de soporte: {support_vectors.shape[0]}")







