from sklearn import datasets
from sklearn.model_selection import train_test_split, cross_val_score, LeaveOneOut
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()

#3.8.1
""" X = iris.data[:, :2]
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

result = model.score(X_test,y_test)
print(result) """

#3.8.2
""" # Usar solo las dos primeras columnas como features
X = iris.data[:, :2]
y = iris.target

# Crear el modelo
model = LogisticRegression()

# Aplicar K-fold cross-validation con 4 pliegues
scores = cross_val_score(model, X, y, cv=4)

# Resultados de los cross-validation scores
print(scores)
print(scores.mean()) """

#3.8.3
# Usar solo las dos primeras columnas como features
X = iris.data[:, :2]
y = iris.target

# Crear el modelo
model = LogisticRegression()

# Aplicar Leave-One-Out cross-validation
loocv = LeaveOneOut()
scores = cross_val_score(model, X, y, cv=loocv)

# Mostrar el promedio del cross-validation score
print("Average Leave-One-Out cross-validation score:", scores.mean())

