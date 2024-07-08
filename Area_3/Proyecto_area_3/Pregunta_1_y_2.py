import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


# Cargar datos
archivo_csv = r'C:\Users\josei\Documents\NTT DATA CLASES\Área 3 - Material de clases\estadisticas_community_areas.csv'
df = pd.read_csv(archivo_csv)

###EJERCICIO 1
# Ver primeras filas
#print(df.head())

# Ver información
#print(df.info())

## 1. Ver valores nulos
missing_values = df.isnull().sum()
#print('Valores faltantes por columna:')
#print(missing_values)

### Observamos qué valores hay en la variable Num_Hospitals y visualizamos cuáles contiene:
df["Num_Hospitals"].unique()

### Reemplazar valores nulos por cero en 'Num_Hospitals'
df['Num_Hospitals'] = df['Num_Hospitals'].fillna(0)

### Reemplazar valores nulos por la media en 'Num_Hospitals'
df['Num_Hospitals'] = df['Num_Hospitals'].fillna(0)

### Observamos los datos que tiene consumo eléctrico:
df["Consumo_Electrico"].unique()

# Observando los datos, visualizamos que hay un registro nulo para la variable Consumo_Electrico, y que su tipo es object. 
# Teniendo en cuenta sus valores, consideramos que debemos cambiar el tipo a category. Y para ello:
# Consideramos dar al único nulo de "Consumo_Electrico" valor 0 para, posteriormente, asignarlo a la categoría con mayor porcentaje, para equilibrarlo.
# Rellenamos el único nulo con valor 0:
df["Consumo_Electrico"] = df.Consumo_Electrico.fillna(0)

# Comprobamos que se ha realizado correctamente:
df["Consumo_Electrico"].isnull().sum()

# Vemos cuánto porcentaje hay de cada categoría:
df["Consumo_Electrico"].value_counts()

# Sustituimos el valor 0 por la categoría con mayor porcentaje:
df["Consumo_Electrico"] = df["Consumo_Electrico"].apply(lambda X:"Medio Bajo" if X == 0 else X)

# Comprobamos de nuevo las categorías existentes:
df["Consumo_Electrico"].unique()

### Verificar que ya no hay valores nulos en Num_Hospitals y en Consumo_Electrico
missing_values = df.isnull().sum()
#print('Valores faltantes por columna después de reemplazar:')
#print(missing_values)



## 2. Se ha observado que no existen valores con decimales útiles en la variable Num_Hospitals.
### Por lo que, procedemos a cambiar su categoría de float64 a int8:
df["Num_Hospitals"] = df["Num_Hospitals"].astype("int8")

### Por último, procedemos a cambiar su categoría de Consumo_Electrico de object a category:
df["Consumo_Electrico"] = df["Consumo_Electrico"].astype("category")

""" # Mostramos los tipos de datos:
print(df.info())

## 3. A continuación, visualizamos las gráficas de las variables seleccionadas.
### Histograma de la variable Population.

### Importamos las librerías:
import matplotlib.pyplot as plt

### Construimos el Histograma:
plt.hist(df["Population"], bins=10)
plt.title("Distribución de la variable Population")
plt.xlabel("Población")
plt.ylabel("Frecuencia")
plt.show()

# A continuación, visualizamos las gráficas de las variables seleccionadas.
# Histograma de la variable Criminalidad_100000.

# Importamos las librerías:
import matplotlib.pyplot as plt

# Construimos el Histograma:
# Creamos la figura: 
plt.hist(df["Criminalidad_100000"], bins=10)
plt.title("Distribución de la variable Criminalidad_100000")
plt.xlabel("Índice de Criminalidad")
plt.ylabel("Frecuencia")
plt.show()

# Revisamos los outliers de la variable Criminalidad_100000:

# Importamos las librerías:
import matplotlib.pyplot as plt

# Creamos el diagrama:
plt.boxplot(df["Criminalidad_100000"])
plt.title("Diagrama de la variable Criminalidad_100000")
plt.xlabel("Índice de Criminalidad")
plt.ylabel("Frecuencia")
plt.show() """



### EJERCICIO 2

# Excluir las columnas no numéricas al calcular la matriz de correlación
numeric_df = df.select_dtypes(include=[float, int])

# Calcular la matriz de correlación y visualizar
corr_matrix = numeric_df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()

# Seleccionar las variables para el modelo predictivo
X = numeric_df.drop(columns=['Criminalidad_100000'])
y = df['Criminalidad_100000']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Predecir y calcular el error cuadrático medio
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Error Cuadrático Medio: {mse}')

# Validación del modelo
r2 = r2_score(y_test, y_pred)
print(f'R²: {r2}')

### Respuestas

""" 
1. ¿Extraéis alguna conclusión relevante?

Correlación entre variables: El gráfico de la matriz de correlación muestra que hay algunas correlaciones moderadas entre varias de las variables. 
Por ejemplo:
Ingresos y White tienen una correlación alta (0.83).
Latinos y Population tienen una correlación positiva (0.19).
Blacks y White tienen una correlación negativa fuerte (-0.69).
Num_Schools y Population tienen una correlación positiva (0.077).
Criminalidad_100000 y Num_Schools tienen una correlación negativa (-0.34).
Criminalidad_100000 y Population tienen una correlación negativa (-0.25).

2. ¿Qué selección de variables habéis considerado?

Las variables seleccionadas para el modelo predictivo fueron:
Population
Latinos
Blacks
White
Asian
Other
Num_Afford_Rental_Houses
Num_Hospitals
Num_Schools
Ingresos
Consumo_Electrico

3. Validad el modelo atendiendo a distintas métricas de error. ¿Qué conclusión extraéis?

Error Cuadrático Medio (MSE): 5548649.186269152
R² (Coeficiente de Determinación): -0.059376924371334905

Conclusiones:

MSE: Un valor de MSE tan alto indica que hay un gran error en las predicciones del modelo.
R²: El valor de 𝑅2 negativo sugiere que el modelo es peor que un modelo trivial (un modelo que simplemente predice el valor medio de la variable objetivo para todas las observaciones). Un valor negativo indica que el modelo no es adecuado para los datos y no captura la variabilidad de la variable objetivo.
"""
