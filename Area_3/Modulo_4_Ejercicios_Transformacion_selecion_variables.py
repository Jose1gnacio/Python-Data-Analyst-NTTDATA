import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency, stats
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Normalizer, Binarizer, RobustScaler, power_transform, LabelEncoder, OneHotEncoder
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import VarianceThreshold

#3.6.1
""" #Datos
data = {
    'Ventas': [10000, 15200, 14300, 25800, 2560, 12780, 32500, 23624, 12000, 15858, 23250, 11630],
    'Gastos': [6500, 6500, 6500, 7850, 6500, 8250, 6500, 9252, 6500, 10250, 12450, 13000],
    'Beneficio': [3500, 8700, 7800, 17950, -3940, 4530, 26000, 14372, 5500, 5608, 10800, -1370]
}
df = pd.DataFrame(data)

#Inicializar el scaler
scaler = MinMaxScaler()

#Reescalar los datos
#df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
#print(df_scaled) """

#3.6.2
""" scaler = StandardScaler()
standardized_data = scaler.fit_transform(df_scaled)
standardized_df = pd.DataFrame(standardized_data, columns=df_scaled.columns)

print("\nDataFrame tipificado con media 0 y desviación estándar 1:")
print(standardized_df) """

#3.6.3
#scaler = Normalizer().fit(df)
#normalized_df = scaler.transform(df)

#print("\nDataFrame normalizado:")
#print(normalized_df)

#3.6.4
""" binarizer = Binarizer(threshold=10000).fit(df)
binarized_df = binarizer.transform(df)

print("\nDataFrame con variable binaria (Ventas_binaria):")
print(binarized_df) """

#3.6.5
""" # Inicializar RobustScaler
scaler = RobustScaler().fit(df)

# Ajustar y transformar los datos
scaled_data = scaler.transform(df)

# Crear un nuevo DataFrame con los datos escalados
scaled_df = pd.DataFrame(scaled_data, columns=df.columns)

print("\nDataFrame con datos escalados utilizando RobustScaler:")
print(scaled_df) """

#3.6.6
""" transformer = power_transform(df.apply(lambda x: x +abs(x.min()) +1 if x.min() < 0 else x + 1), method= 'box-cox')
transformed_df = pd.DataFrame(transformer, columns=df.columns)

print("\nDataFrame con variables normalizadas utilizando Box-Cox:")
print(transformed_df) """

#3.6.7
#df['Cobrado'] = ['S', 'N', 'N', 'S', 'S', 'N', 'S', 'S', 'S', 'N', 'S', 'N']
""" label_encoder = LabelEncoder()

#Codificar la variable y guardar
df['Cobrado2'] = label_encoder.fit_transform(df['Cobrado'])

print("\nDataFrame con 'Cobrado' transformada a numérico (Cobrado2):")
print(df) """

#3.6.8
""" encoder = OneHotEncoder()

#Transformar 'Cobrado' a variables binarias
cobrado_encoded = encoder.fit_transform(df[['Cobrado']])

#Convertir a DataFrame y añadir nombres a las columnas
cobrado_encoded_df = pd.DataFrame(cobrado_encoded.toarray(), columns=encoder.get_feature_names_out(['Cobrado']))

#Concatenar el DataFrame original con las variables binarias
df = pd.concat([df, cobrado_encoded_df], axis=1)

print("\nDataFrame con 'Cobrado' transformada a variables binarias:")
print(df) """

#3.6.9
""" #Transformar 'Cobrado' a variables binarias usando get_dummies
cobrado_dummies = pd.get_dummies(df['Cobrado'], prefix='Cobrado')

#Concatenar el DataFrame original con las variables binarias
df = pd.concat([df, cobrado_dummies], axis=1)

print("\nDataFrame con 'Cobrado' transformada a variables binarias usando get_dummies:")
print(df) """

#3.6.10
archivo_csv = r'C:\Users\josei\Documents\NTT DATA CLASES\Área 3 - Material de clases\Modulo_4\Tabla.csv'
df = pd.read_csv(archivo_csv, delimiter=';')
""" print(df.head())

#Boxplot de A vs E
plt.subplot(2, 2, 1)
plt.boxplot([df[df['E'] == 1]['A'], df[df['E'] == 2]['A']], labels=['E=1', 'E=2'])
plt.title('Boxplot de A vs E')
plt.xlabel('E')
plt.ylabel('A')

#Boxplot de B vs E
plt.subplot(2, 2, 2)
plt.boxplot([df[df['E'] == 1]['B'], df[df['E'] == 2]['B']], labels=['E=1', 'E=2'])
plt.title('Boxplot de B vs E')
plt.xlabel('E')
plt.ylabel('B')

#Boxplot de C vs E
plt.subplot(2, 2, 3)
plt.boxplot([df[df['E'] == 1]['C'], df[df['E'] == 2]['C']], labels=['E=1', 'E=2'])
plt.title('Boxplot de C vs E')
plt.xlabel('E')
plt.ylabel('C')

#Boxplot de D vs E
plt.subplot(2, 2, 4)
plt.boxplot([df[df['E'] == 1]['D'], df[df['E'] == 2]['D']], labels=['E=1', 'E=2'])
plt.title('Boxplot de D vs E')
plt.xlabel('E')
plt.ylabel('D')

plt.tight_layout()
plt.show() """

#3.6.11
""" #Crear un histograma de A vs B
plt.figure(figsize=(10, 6))
plt.hist2d(df['A'], df['B'], bins=(20, 20), cmap='Blues')
plt.colorbar(label='Frecuencia')
plt.xlabel('A')
plt.ylabel('B')
plt.title('Histograma 2D de A vs B')

#Crear un histograma de E vs B
plt.figure(figsize=(10, 6))
plt.hist2d(df['E'], df['B'], bins=(2, 20), cmap='Greens')
plt.colorbar(label='Frecuencia')
plt.xlabel('E')
plt.ylabel('B')
plt.title('Histograma 2D de E vs B')

plt.tight_layout()
plt.show() """

#3.6.12
""" variables = ["A", "E"]

for var in variables:
    #Crear la tabla de contingencia entre var (A o E) y B
    crosstab_result = pd.crosstab(index=df[var], columns=df['B'])

    #Realizar la prueba de chi-cuadrado
    chi2, p, dof, expected = chi2_contingency(crosstab_result)

    #Establecer el nivel de significancia
    alpha = 0.05

    #Interpretar los resultados de la prueba de chi-cuadrado
    if p < alpha:
        print(f"Hay una relación significativa entre {var} y B (p-value = {p}).")
    else:
        print(f"No hay suficiente evidencia para afirmar una relación entre {var} y B (p-value = {p}).")

    # Mostrar la tabla de contingencia para referencia
    print("\nTabla de contingencia:")
    print(crosstab_result)
    print() """

#3.6.13
""" #Calcular la correlación de Pearson entre cada variable (A, B, C, D) y E
correlations = df[['A', 'B', 'C', 'D', 'E']].corr(method='pearson')

print("Correlaciones de Pearson:")
print(correlations)

#Crear el heatmap usando seaborn
plt.figure(figsize=(10, 8))
sns.heatmap(correlations, annot=True, cmap='coolwarm', vmin=-1, vmax=1, fmt='.2f', linewidths=.5)
plt.title('Mapa de calor de correlación (Pearson)')
plt.show() """

#3.6.14
""" #Separar las variables predictoras (A, B, C, E) y la variable objetivo (D)
X = df[['A', 'B', 'C', 'E']]
y = df['D']

#Aplicar SelectKBest con chi2 para seleccionar la variable más relevante
selector = SelectKBest(score_func=chi2, k=1)
selector.fit(X, y)

#Obtener los puntajes de chi2 y los nombres de las variables
scores = selector.scores_
feature_names = X.columns

#Encontrar la variable más relevante
most_relevant_feature = feature_names[scores.argmax()]

print(f"La variable más relevante para la clasificación de D es: {most_relevant_feature}") """

#3.6.15
""" # Separar las variables predictoras (A, B, C, E) y la variable objetivo (D)
X = df[['A', 'B', 'C', 'E']]
y = df['D']

# Crear un modelo ExtraTreesClassifier
model = ExtraTreesClassifier(random_state=42)
model.fit(X, y)

# Obtener la importancia de las características
feature_importances = model.feature_importances_

# Crear un diccionario para asociar importancias con nombres de características
feature_importance_dict = dict(zip(X.columns, feature_importances))

# Encontrar la variable más relevante según ExtraTreesClassifier
most_relevant_feature = max(feature_importance_dict, key=feature_importance_dict.get)

print(f"La variable más relevante para la clasificación de D según ExtraTreesClassifier es: {most_relevant_feature}") """

#3.6.16
""" #Separar las variables predictoras (A, B, C, D) y la variable objetivo (E)
X = df[['B', 'C', 'D', 'E']]  # Variables predictoras
y = df['A']  # Variable objetivo

#Crear un estimador para el RFE (RandomForestClassifier como ejemplo)
estimator = RandomForestClassifier(random_state=42)

#Crear un selector RFE y ajustarlo al modelo
selector = RFE(estimator, n_features_to_select=1, step=1)  # Seleccionamos una característica a la vez
selector = selector.fit(X, y)

#Obtener el ranking de las características
rankings = selector.ranking_
feature_names = X.columns

#Crear una lista de tuplas (ranking, nombre de la característica) y ordenarla por ranking
ranked_features = sorted(zip(rankings, feature_names))

# Imprimir las variables ordenadas desde la más importante a la menos importante
print("Variables ordenadas por importancia según RFE para predecir A:")
for rank, feature in ranked_features:
    print(f"Rank {rank}: {feature}") """

#3.6.17
""" #Mostrar las varianzas originales de las variables
print("Varianzas originales:")
print(df.var())

#Separar las variables predictoras (A, B, C, D, E)
X = df[['A', 'B', 'C', 'D', 'E']]

#Crear un objeto VarianceThreshold con umbral por defecto (0.0)
selector = VarianceThreshold()

#Ajustar y transformar los datos
X_transformed = selector.fit_transform(X)

#Obtener las varianzas finales después de aplicar VarianceThreshold
variances_final = selector.variances_

#Crear un dataframe para mostrar las varianzas originales y finales
variances_df = pd.DataFrame({
    'Variable': X.columns,
    'Varianza original': X.var(),
    'Varianza final': variances_final
})

print("\nVarianzas originales y finales:")
print(variances_df) """

#3.6.18
# PASO 1: CARGAR EL DATASET Y EXPLORAR LOS DATOS INICIALES
archivo_csv = r'C:\Users\josei\Documents\NTT DATA CLASES\Área 3 - Material de clases\Modulo_4\netflix_movies_and_tv_shows_sample_dataset_sample.csv'
df = pd.read_csv(archivo_csv)
#print(df.head())

# PASO 2: LIMPIEZA DATASET 
## 2.1 Valores Nulos
valores_nulos = df.isnull().sum()

###Filtrar columnas que tienen al menos un valor nulo
columnas_con_nulos = valores_nulos[valores_nulos > 0]

#print(f"Columnas con valores nulos: \n{columnas_con_nulos}")

## 2.2 Manejo de valores nulos, rellenan con "Unknown" o valores específicos
df['formattedDuration'] = df['formattedDuration'].fillna('Unknown')
df['actors'] = df['actors'].fillna('Unknown')
df['director'] = df['director'].fillna('Unknown')
df['creator'] = df['creator'].fillna('Unknown')
df['audio'] = df['audio'].fillna('Unknown')
df['subtitle'] = df['subtitle'].fillna('Unknown')
df['numberOfSeasons'] = df['numberOfSeasons'].fillna(0)
df['seasonStartDate'] = df['seasonStartDate'].fillna('Unknown')

### Verificar que no haya valores nulos
valores_nulos_despues = df.isnull().sum()
#print(f"Valores nulos restantes: \n {valores_nulos_despues}")

## 2.3 Formato de fecha
df['releasedDate'] = pd.to_datetime(df['releasedDate'], errors='coerce')

### Verificar el resultado
#print(df['releasedDate'].head())


## 2.4 Estandarización de nombres de las columnas
### Estandarizar nombres de columnas
df.columns = df.columns.str.strip().str.replace(' ', '_')

### Verificar los nombres de columnas estandarizados
#print(f"Columnas estandarizadas: \n {df.columns}")

## 2.5 Eliminar columnas no informativas
# Mostrar las columnas actuales
#print(df.columns)

# Decidir qué columnas eliminar (ejemplo: sourceLink y scrapedAt)
columnas_a_eliminar = ['sourceLink', 'scrapedAt']

# Eliminar las columnas seleccionadas
df.drop(columns=columnas_a_eliminar, inplace=True)

# Verificar las columnas después de la eliminación
#print(f"\nColumnas después de eliminar: \ndf.columns")

## 2.6 Valores duplicados
# Verificar y eliminar duplicados
duplicados = df[df.duplicated()]
#print(f"Valores duplicados: \n {duplicados}")

## PASO 3: GUARDAR EL DATASET LIMPIO

archivo_limpiado = r'C:\Users\josei\Documents\NTT DATA CLASES\Área 3 - Material de clases\Modulo_4\netflix_movies_and_tv_shows_sample_dataset_cleaned.csv'

# Guardar el DataFrame en el nuevo archivo CSV
df.to_csv(archivo_limpiado, index=False)

print(f"El dataset limpio ha sido guardado en: {archivo_limpiado}")






