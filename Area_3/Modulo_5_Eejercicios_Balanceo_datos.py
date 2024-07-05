""" from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from collections import Counter
from imblearn.under_sampling import NearMiss

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=1)

# Definimos las funciones que vamos a necesitar para balancear los datos
def run_model_balanced(X_train, X_test, y_train, y_test):
    clf = LogisticRegression(C=1.0, penalty='l2', random_state=1, solver="newton-cg", class_weight="balanced")
    clf.fit(X_train, y_train)
    return clf

# Para mostrar los resultados
def mostrar_resultados(y_test, pred_y):
    conf_matrix = confusion_matrix(y_test, pred_y)
    plt.figure(figsize=(8, 8))
    sns.heatmap(conf_matrix, xticklabels=iris.target_names, yticklabels=iris.target_names, annot=True, fmt="d", cmap='Blues')
    plt.title("Confusion Matrix")
    plt.ylabel('True Class')
    plt.xlabel('Predicted Class')
    plt.show()
    
    print(classification_report(y_test, pred_y))

# Entrenamos y testeamos
model = run_model_balanced(X_train, X_test, y_train, y_test)
pred_y = model.predict(X_test)
mostrar_resultados(y_test, pred_y) """

#3.10.2
""" from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from collections import Counter
from imblearn.under_sampling import NearMiss

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7)

#Definimos las variables que no estaban definidas
us = NearMiss(n_neighbors=3,version=2)
X_train_res, y_train_res = us.fit_resample(X_train, y_train)

#Definimos la función que vamos a necesitar para balancear los datos sin el class_weight
def run_model (X_train, X_test, y_train, y_test):
    clf = LogisticRegression(C=1.0,penalty='l2',random_state=1,solver="newton-cg")
    clf.fit(X_train,y_train)
    return clf

def mostrar_resultados(y_test, pred_y):
    conf_matrix = confusion_matrix(y_test, pred_y)
    plt.figure(figsize=(8, 8))
    sns.heatmap(conf_matrix, xticklabels=iris.target_names, yticklabels=iris.target_names, annot=True, fmt="d", cmap='Blues')
    plt.title("Confusion Matrix")
    plt.ylabel('True Class')
    plt.xlabel('Predicted Class')
    plt.show()
    
    print(classification_report(y_test, pred_y))

#Mostramos los valores de antes de balancear los datos y de después
print("Distribución antes del balanceo {}".format(Counter(y_train)))
print("Distribución después del balanceo {}".format(Counter(y_train_res)))

#Entrenamos y testeamos
model = run_model(X_train_res, X_test, y_train_res, y_test)
pred_y = model.predict(X_test)
mostrar_resultados(y_test, pred_y) """

#3.10.3
""" from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
from imblearn.over_sampling import RandomOverSampler
from collections import Counter

#Cargar el dataset iris
iris = load_iris()
X, y = iris.data, iris.target

#Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=1)

#Aplicar RandomOverSampling para balancear los datos
ros = RandomOverSampler(random_state=1)
X_train_res, y_train_res = ros.fit_resample(X_train, y_train)

#Definir la función que vamos a necesitar para entrenar el modelo
def run_model(X_train, X_test, y_train, y_test):
    clf = LogisticRegression(C=1.0, penalty='l2', random_state=1, solver="newton-cg")
    clf.fit(X_train, y_train)
    return clf

#Mostrar los resultados
def mostrar_resultados(y_test, pred_y):
    conf_matrix = confusion_matrix(y_test, pred_y)
    plt.figure(figsize=(8, 8))
    sns.heatmap(conf_matrix, xticklabels=iris.target_names, yticklabels=iris.target_names, annot=True, fmt="d", cmap='Blues')
    plt.title("Confusion Matrix")
    plt.ylabel('True Class')
    plt.xlabel('Predicted Class')
    plt.show()
    
    print(classification_report(y_test, pred_y))

#Mostrar los valores antes y después de balancear los datos
print("Distribución antes del balanceo {}".format(Counter(y_train)))
print("Distribución después del balanceo {}".format(Counter(y_train_res)))

#Entrenar y testear el modelo
model = run_model(X_train_res, X_test, y_train_res, y_test)
pred_y = model.predict(X_test)
mostrar_resultados(y_test, pred_y) """

#3.10.4
""" from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
from imblearn.combine import SMOTEENN
from collections import Counter

#Cargar el dataset iris
iris = load_iris()
X, y = iris.data, iris.target

#Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=1)

#Aplicar SMOTEENN para balancear los datos
smote_enn = SMOTEENN(random_state=1)
X_train_res, y_train_res = smote_enn.fit_resample(X_train, y_train)

#Definir la función que vamos a necesitar para entrenar el modelo
def run_model(X_train, X_test, y_train, y_test):
    clf = LogisticRegression(C=1.0, penalty='l2', random_state=1, solver="newton-cg")
    clf.fit(X_train, y_train)
    return clf

#Mostrar los resultados
def mostrar_resultados(y_test, pred_y):
    conf_matrix = confusion_matrix(y_test, pred_y)
    plt.figure(figsize=(8, 8))
    sns.heatmap(conf_matrix, xticklabels=iris.target_names, yticklabels=iris.target_names, annot=True, fmt="d", cmap='Blues')
    plt.title("Confusion Matrix")
    plt.ylabel('True Class')
    plt.xlabel('Predicted Class')
    plt.show()
    
    print(classification_report(y_test, pred_y))

#Mostrar los valores antes y después de balancear los datos
print("Distribución antes del balanceo {}".format(Counter(y_train)))
print("Distribución después del balanceo {}".format(Counter(y_train_res)))

#Entrenar y testear el modelo
model = run_model(X_train_res, X_test, y_train_res, y_test)
pred_y = model.predict(X_test)
mostrar_resultados(y_test, pred_y)
 """

#3.10.5
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
from imblearn.ensemble import BalancedBaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from collections import Counter

#Cargar el dataset iris
iris = load_iris()
X, y = iris.data, iris.target

#Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=1)

#Aplicar BalancedBaggingClassifier para balancear los datos
bbc = BalancedBaggingClassifier(estimator=DecisionTreeClassifier(),
                                sampling_strategy='auto',
                                replacement=False,
                                random_state=1)
bbc.fit(X_train, y_train)

#Predecir las etiquetas para los datos de prueba
pred_y = bbc.predict(X_test)

#Mostrar la matriz de confusión y el reporte de clasificación
def mostrar_resultados(y_test, pred_y):
    conf_matrix = confusion_matrix(y_test, pred_y)
    plt.figure(figsize=(8, 8))
    sns.heatmap(conf_matrix, xticklabels=iris.target_names, yticklabels=iris.target_names, annot=True, fmt="d", cmap='Blues')
    plt.title("Confusion Matrix")
    plt.ylabel('True Class')
    plt.xlabel('Predicted Class')
    plt.show()
    
    print(classification_report(y_test, pred_y))

#Mostrar los resultados
mostrar_resultados(y_test, pred_y)


