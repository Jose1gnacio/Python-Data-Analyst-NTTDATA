import pandas as pd

#archivo_csv = r'C:\Users\josei\Documents\NTT DATA CLASES\Área 3 - Material de clases\Modulo_3\Esculturas_Parque_Arqueolgicos_Colombia.csv'
#df = pd.read_csv(archivo_csv)

# 3.4.1 (using double backslashes)
""" registro_105 = df.iloc[105]
print(registro_105)

nombre_elemento = registro_105['Nombre elemento arqueológico']
print(f'Nombre del elemento buscado es: {nombre_elemento}') """

# 3.4.2
""" registro = df.loc[[24, 36, 125, 182], ['Nombre elemento arqueológico', 'Ubicación actual dentro del parque']]
print(registro) """

#3.4.3
""" subset_df = df.loc[100:111, ['Código ICANH']]
print(subset_df) """

#3.4.4
""" registro_impares = df.iloc[lambda x: x.index % 2 != 0]
cant_impares = len(registro_impares)
print(f"{registro_impares} \nLa cantidad de registros impares es: {cant_impares}") """

#3.4.5
""" ubicacion = df.loc[[10, 20, 30, 40, 50], ['Ubicación actual dentro del parque']]
print(ubicacion) """

#3.4.6
""" nuevo_df = df.set_index("Elemento arqueológico") """
#print(nuevo_df)

#3.4.7
""" sarcofago_df = nuevo_df.loc['Sarcófago']
num_sarcofago = len(sarcofago_df.loc['Sarcófago'])
#print(sarcofago_df)
#print(f"El número total de registros es: {num_sarcofago}") """

#3.4.8
""" parque_arqueologico_df = sarcofago_df.reset_index()
print(parque_arqueologico_df.iloc[:3, 1]) """

#archivo_csv = r'C:\Users\josei\Documents\NTT DATA CLASES\Área 3 - Material de clases\Modulo_3\ejecucion-presupuestaria_Chile-febrero-2023.csv'
#df = pd.read_csv(archivo_csv, sep=';')

#3.4.9
""" seleccion = df[['Nombre_Subtítulo', 'Ejecución_de_FEBRERO']]
print(seleccion) """

#3.4.10
""" filtro = df['Ejecución_de_FEBRERO'] <= 0
registros_menor_o_igual_cero = df[filtro]
seleccion_final = registros_menor_o_igual_cero[['Nombre_Subtítulo', 'Ejecución_de_FEBRERO']]

print(f"Registros cuya Ejecución_de_FEBRERO es menor o igual que 0: \n{seleccion_final}") """

#3.4.11
""" filtro = df['Ejecución_de_FEBRERO'] > 2000
registros_mayor_20000 = df[filtro]
seleccion_final = registros_mayor_20000[['Nombre_Subtítulo', 'Ejecución_de_FEBRERO']]

print(f"Registros cuya Ejecución_de_FEBRERO es mayor que 20000 DÓLARES: \n {seleccion_final}") """

#3.4.12
""" filtro = (df['Ejecución_a_FEBRERO'] > 10000000) & (df['Moneda'] == 'PESOS')
registros_filtrados = df[filtro]
seleccion_final = registros_filtrados[['Subtítulo', 'Ejecución_a_FEBRERO']]

print(f"Registros cuya Ejecución_a_FEBRERO es mayor que 10000000 de PESOS y la Moneda es PESOS: \n{seleccion_final}") """

#3.4.13
""" subtitulos_a_buscar = ["IMPUESTOS", "RENTAS DE LA PROPIEDAD", "INGRESOS DE OPERACIÓN", "VENTA DE ACTIVOS FINANCIEROS"]

filtro = df['Nombre_Subtítulo'].isin(subtitulos_a_buscar)
registros_filtrados = df[filtro]

print(f"Registros cuyo Nombre_Subtítulo coincide con los elementos de la lista: \n {registros_filtrados}") """

#3.4.14
""" subtitulos_a_buscar = ["IMPUESTOS", "RENTAS DE LA PROPIEDAD", "INGRESOS DE OPERACIÓN", "VENTA DE ACTIVOS FINANCIEROS"]

filtro_ejecucion = df['Ejecución_de_FEBRERO'] > 10000

filtro_subtitulos = df['Nombre_Subtítulo'].isin(subtitulos_a_buscar)

registros_filtrados = df[filtro_ejecucion & filtro_subtitulos]

print(f"Registros cuya Ejecución_de_FEBRERO es mayor de 10000 DÓLARES y el Nombre_Subtítulo coincide con los elementos de la lista: \n {registros_filtrados}") """

#3.4.15
""" df['Diferencia'] = df['Ejecución_a_FEBRERO'] - df['Ejecución_de_FEBRERO']
registros_diferencia_cero = df[df['Diferencia'] == 0]

print(f"Registros donde la diferencia entre Ejecución_a_FEBRERO y Ejecución_de_FEBRERO es igual a 0: \n {registros_diferencia_cero}") """

#3.4.16
""" df['Diferencia'] = df['Ejecución_a_FEBRERO'] - df['Ejecución_de_FEBRERO']
registros_diferencia_mayor_250k = df[df['Diferencia'] > 250000]

print(f"Registros donde la diferencia entre Ejecución_a_FEBRERO y Ejecución_de_FEBRERO es mayor que 250,000 DÓLARES: \n {registros_diferencia_mayor_250k}") """

#3.4.17
""" datos = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    'Ventas': [10000, 15200, 14300, 25800, 2560, 12780, 32500, 23624, 12000, 15858, 23250, 11630],
    'Gastos': [6500, 6500, 6500, 7850, 6500, 8250, 6500, 9252, 6500, 10250, 12450, 13000],
    'Beneficio': [3500, 8700, 7800, 17950, -3940, 4530, 26000, 14372, 5500, 5608, 10800, -1370],
    'Cobrado': ['S', 'N', 'N', 'S', 'S', 'N', 'S', 'S', 'S', 'N', 'S', 'N']
}
df = pd.DataFrame(datos)
df['Dividendo'] = df['Beneficio']

#print(df) """

#3.4.18
""" df = df.assign(Dividendo=df['Dividendo'] * 0.1)

print(df) """

#3.4.19
""" df = df.assign(Dividendo=df['Dividendo'] * 0.1)
df['Dividendo'] = df['Dividendo'].map(lambda x: x if x > 0 else 0)

print(df) """

#3.4.20
""" def calcular_porcentaje(e):
    porcentaje_div = (e["Dividendo"]/e["Ventas"])*100
    return max(0, round(porcentaje_div))
df['Porcentaje'] = df.apply(calcular_porcentaje, axis=1)

#print(df) """

#3.4.21
""" columnas_numericas = df.select_dtypes(include='number').columns
df_texto = df.drop(columns=columnas_numericas) """

#print(df_texto)

#3.4.22
""" columnas_numericas = df.select_dtypes(include='number').columns
medias_por_cobrado = df[columnas_numericas].groupby(df['Cobrado']).mean()

print("Media agrupada por si están cobrados (S) o no cobrados (N):")
print(medias_por_cobrado) """

#3.4.23
""" datos = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    'Pedidos': [20, 40, None, 25, 10, 35, None, None, 22, 42, 36, None],
    'Facturacion': [15000, 30000, 2500, None, 25000, 30000, 1500, None, 15000, 35000, 25000, 2500],
    'Gastos': [5000, 6200, 4500, 3100, 5000, 5500, 6000, 5000, 6500, 5250, 7000, 5200],
    'Pendientes': [None, None, 25, None, 6, 15, 10, None, None, None, 4, None],
    'En_revision': [None, None, None, None, 3, 5, 2, None, 1, None, None, 1]
}
df = pd.DataFrame(datos)
#df_sorted = df.sort_values(by='Facturacion', ascending=True)

#print(df_sorted) """

#3.4.24
""" df_sorted_gastos_facturacion = df.sort_values(by=['Gastos', 'Facturacion'], ascending=True)
df_sorted_facturacion_gastos = df.sort_values(by=['Facturacion', 'Gastos'], ascending=True)

print("Ordenado por Gastos y luego por Facturacion:")
print(df_sorted_gastos_facturacion)
print("\nOrdenado por Facturacion y luego por Gastos:")
print(df_sorted_facturacion_gastos) """

#3.4.25
""" df_sorted_index = df.rename(columns={'Facturacion': 'Facturas'}).sort_index()

print(df_sorted_index) """

#3.4.26
""" nulos_por_columna = df.isnull().sum()
media_nulos_por_columna = df.isnull().mean()

print(f"Número de elementos nulos por columna: \n {nulos_por_columna}")
print(f"\nMedia de valores nulos por columna: \n {media_nulos_por_columna}") """

#3.4.27
""" meses_sin_pendientes = df[df['Pendientes'].isnull()]['Mes'].tolist()
meses_sin_pedidos = df[df['Pedidos'].isnull()]['Mes'].tolist()

print(f"Meses sin pedidos pendientes: \n {meses_sin_pendientes}")
print(f"\nMeses sin pedidos: \n {meses_sin_pedidos}") """

#3.4.28
""" meses_sin_nulos = df[df.notnull().all(axis=1)]['Mes'].tolist()

if meses_sin_nulos:
    print("Hay meses sin ningún valor nulo:", meses_sin_nulos)
else:
    print("No hay ningún mes sin ningún valor nulo.") """

#3.4.29
""" columnas_sin_nulos = df.columns[df.notnull().all()]
df_sin_nulos = df[columnas_sin_nulos]

print(f"Nuevo DataFrame sin columnas con valores nulos: \n {df_sin_nulos}") """

#3.4.30
datos = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    'Pedidos': [20, 40, None, 25, 10, 35, None, None, 22, 42, 36, None],
    'Facturacion': [15000, 30000, 2500, None, 25000, 30000, 1500, None, 15000, 35000, 25000, 2500],
    'Gastos': [5000, 6200, 4500, 3100, 5000, 5500, 6000, 5000, 6500, 5250, 7000, 5200],
    'Pendientes': [None, None, 25, None, 6, 15, 10, None, 1, None, 4, None],
    'En_revision': [None, None, None, None, 3, 5, 2, None, 1, None, None, 1]
}
datos2 = {
    "Mes": ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"],
    "Pedidos": [10,20,15,None,10,None,26,12,None,22,42,36],
    "Facturas": [6500,25000,15000,12000,None,10000,10500,None,15000,15000,5000,25000],
    "Gastos": [5000,6200,4500,3100,5000,5500,6000,5000,6500,5250,7000,5200],
    "Pendientes": [None,None,5,3,6,15,10,None,None,None,4,None],
    "En_revision": [None,None,2,None,3,5,2,None,1,None,1,1]
}

df1 = pd.DataFrame(datos)
df2 = pd.DataFrame(datos2)

df_concat = pd.concat([df1, df2], ignore_index=True)

print("DataFrame concatenado con índices reiniciados:")
print(df_concat)




