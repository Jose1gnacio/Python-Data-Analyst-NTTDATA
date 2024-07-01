from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score, KFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, make_scorer, recall_score, f1_score

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
# Calcular cross-validation score con métrica de F1-score
# Definir scorer para F1-score
scorer = make_scorer(f1_score, average='binary')

# Calcular cross-validation scores
scores = cross_val_score(model, X, y, cv=kfold, scoring=scorer)

# Mostrar los scores obtenidos
print("Cross-validation scores (F1-score):", scores)
print("Mean F1-score:", scores.mean())
