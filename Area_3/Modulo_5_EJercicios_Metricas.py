from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score, KFold
from sklearn.linear_model import LogisticRegression

# Cargar el dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Crear un modelo de regresión logística
model = LogisticRegression()

# Definir el objeto KFold para 3 splits
kfold = KFold(n_splits=3, shuffle=True, random_state=42)

# Calcular cross-validation score con métrica de accuracy
scores = cross_val_score(model, X, y, cv=kfold, scoring='accuracy')

# Mostrar los scores obtenidos
print("Cross-validation scores:", scores)
print("Mean accuracy:", scores.mean())
