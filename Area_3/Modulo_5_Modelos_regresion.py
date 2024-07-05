from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

#Cargar el dataset
diabetes = load_diabetes()
X = diabetes.data[:, np.newaxis, 0]  #Tomar la primera columna como variable independiente
y = diabetes.target

#Inicializar el modelo de regresión lineal
model = LinearRegression()

# Ajustar el modelo
model.fit(X, y)

# Obtener coeficientes y puntaje de ajuste
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

plt.show()
