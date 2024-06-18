import pandas as pd
import matplotlib.pyplot as plt
#pd.set_option('display.max_columns', None)

#archivo_csv = r'C:\Users\josei\Documents\NTT DATA CLASES\Área 3 - Material de clases\Modulo_4\World_Development_Report_2021.csv'
#df = pd.read_csv(archivo_csv)

#3.5.1
""" print("\nTipos de las variables en el DataFrame:")
print(df.dtypes) """

#3.5.2
""" duplicados = df.duplicated()
num_duplicados = duplicados.sum()

print(f"Número de filas duplicadas: {num_duplicados}") """

#3.5.3
""" duplicados = df.duplicated()
num_duplicados = duplicados.sum()
#print(f"Número de filas duplicadas antes de eliminarlas: {num_duplicados}") """

""" df = df.drop_duplicates()

duplicados_despues = df.duplicated()
num_duplicados_despues = duplicados_despues.sum()
#print(f"Número de filas duplicadas después de eliminarlas: {num_duplicados_despues}") """

#3.5.4
""" valores_nulos = df.isnull().sum()
columnas_con_nulos = valores_nulos[valores_nulos > 0]

#print("Variables con elementos nulos y el número de nulos en cada una:")
#print(columnas_con_nulos) """

#3.5.5
""" valor_maximo = df['percentage'].max()
valor_minimo = df['percentage'].min()
media = df['percentage'].mean()

print(f"Valor máximo de 'percentage': {valor_maximo}")
print(f"Valor mínimo de 'percentage': {valor_minimo}")
print(f"Media de 'percentage': {media}") """

#3.5.6
""" valores_fuera_rango = {}

percentil_bajo = 1
percentil_alto = 99

for columna in df.select_dtypes(include='number').columns:
    limite_inferior = df[columna].quantile(percentil_bajo / 100)
    limite_superior = df[columna].quantile(percentil_alto / 100)
    
    fuera_de_rango = df[(df[columna] < limite_inferior) | (df[columna] > limite_superior)]
    
    if not fuera_de_rango.empty:
        valores_fuera_rango[columna] = fuera_de_rango[columna]

for columna, valores in valores_fuera_rango.items():
    print(f"Valores fuera de rango en la columna '{columna}':")
    print(valores) """

#3.5.7
""" df = df.drop(columns=['counted'])
print(df.head()) """

#3.5.8
""" columnas = ['counted', 'population', 'percentage']
limite_inferior = 0.02
limite_superior = 0.05
def verificar_frecuencias(columna):
    frecuencias = df[columna].value_counts(normalize=True)
    return frecuencias[(frecuencias > limite_inferior) & (frecuencias < limite_superior)]

for columna in columnas:
    if columna in df.columns:
        frecuencias_superiores = verificar_frecuencias(columna)
        if not frecuencias_superiores.empty:
            print(f"Frecuencias de la columna '{columna}' entre 2% y 5%:")
            print(frecuencias_superiores)
        else:
            print(f"No hay frecuencias en la columna '{columna}' entre 2% y 5%")
    else:
        print(f"La columna '{columna}' no se encuentra en el DataFrame.") """

#3.5.9
archivo_csv = r'C:\Users\josei\Documents\NTT DATA CLASES\Área 3 - Material de clases\Modulo_4\indicadores.csv'
df = pd.read_csv(archivo_csv, sep=';')
#elementos_nulos = df.isnull().sum()

#print("Número de elementos nulos en cada variable:")
#print(elementos_nulos)

#3.5.11
columnas_a_eliminar = ['Anno1996', 'Anno2001']  
df_mod = df.drop(columnas_a_eliminar, axis=1)
#df_mod.info()

#3.5.12
#print("DataFrame original:")
#print(df['Anno2013'])

registros_nulos_2013 = df_mod[df_mod['Anno2013'].isnull()]

#print("\nRegistros con valores nulos en 'Anno2013':")
#print(registros_nulos_2013['Anno2013'])

df_mod_2 = df_mod.dropna(subset=['Anno2013'])

#print("\nDataFrame después de eliminar nulos en 'Anno2013':")
#print(df_mod_2['Anno2013'])

#3.5.13
numerical_columns = df_mod_2.select_dtypes(include=['number']).columns
df_mod_2[numerical_columns] = df_mod_2[numerical_columns].apply(lambda x: x.fillna(x.mean()), axis=0)

#print("DataFrame después de rellenar los valores nulos con la media:")
#print(df_mod_2.head())

#3.5.14
df_years = df_mod_2[['Anno2016', 'Anno2014']]

""" plt.figure(figsize=(10, 6))
df_years.boxplot(flierprops=dict(markerfacecolor='r', marker='o'))
plt.title('Diagrama de Caja para Anno2016 y Anno2014')
plt.ylabel('Valores')
plt.show() """

#3.5.15
Q1 = df_years.quantile(0.25)
Q3 = df_years.quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df_years_filtered = df_years[~((df_years < lower_bound) | (df_years > upper_bound)).any(axis=1)]

plt.figure(figsize=(10, 6))
boxplot = df_years_filtered.boxplot(flierprops=dict(markerfacecolor='r', marker='o'))
plt.title('Diagrama de Caja para Anno2016 y Anno2014 (Sin Outliers)')
plt.ylabel('Valores')
plt.show()
