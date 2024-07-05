import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
archivo_csv = r'C:\Users\josei\Documents\NTT DATA CLASES\Área 3 - Material de clases\estadisticas_community_areas.csv'
df = pd.read_csv(archivo_csv)

#print(df.dtypes)

## Duplicados
duplicated_rows = df.duplicated()
#print(f'Número de filas duplicadas: {duplicated_rows.sum()}')

## Valores NaN
missing_values = df.isnull().sum()
print('Valores faltantes por columna:')
print(missing_values)

# Media hospitales
media_num_hospitals = df['Num_Hospitals'].mean()

# Imprimir la media
print(f'La media del número de hospitales es: {media_num_hospitals}')

df['Num_Hospitals'] = df['Num_Hospitals'].fillna(0)

## Verificar que ya no hay valores nulos en Num_Hospitals
missing_values = df.isnull().sum()
print('Valores faltantes por columna después de reemplazar:')
print(missing_values)

# Encontrar el valor moda en la columna Consumo_Electrico
print(df["Consumo_Electrico"].unique())

""" # Ejemplo de matriz de dispersión (pairplot)
sns.pairplot(df[['Population', 'Ingresos', 'Num_Hospitals', 'Num_Schools', 'Criminalidad_100000']])
plt.suptitle('Matriz de Dispersión', y=1.02)
plt.tight_layout()
plt.show() """

# Ejemplo de boxplots para variables clave
plt.figure(figsize=(12, 10))

""" # Boxplot de Population vs Criminalidad_100000
plt.subplot(3, 2, 1)
sns.boxplot(x='Criminalidad_100000', y='Population', data=df)
plt.title('Distribución de Population por Criminalidad_100000')

# Boxplot de Ingresos vs Criminalidad_100000
plt.subplot(3, 2, 2)
sns.boxplot(x='Criminalidad_100000', y='Ingresos', data=df)
plt.title('Distribución de Ingresos por Criminalidad_100000')

# Boxplot de Num_Hospitals vs Criminalidad_100000
plt.subplot(3, 2, 3)
sns.boxplot(x='Criminalidad_100000', y='Num_Hospitals', data=df)
plt.title('Distribución de Num_Hospitals por Criminalidad_100000') """

# Boxplot de Num_Schools vs Criminalidad_100000

sns.boxplot(x='Criminalidad_100000', data=df)
plt.title('Distribución de Num_Schools por Criminalidad_100000')

""" # Boxplot de Latinos vs Criminalidad_100000
plt.subplot(3, 2, 5)
sns.boxplot(x='Criminalidad_100000', y='Latinos', data=df)
plt.title('Distribución de Latinos por Criminalidad_100000') """

# Ajustes de diseño
plt.tight_layout()
plt.show()