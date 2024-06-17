import pandas as pd

archivo_csv = r'C:\Users\josei\Documents\NTT DATA CLASES\Área 3 - Material de clases\Modulo_3\Esculturas_Parque_Arqueolgicos_Colombia.csv'
df = pd.read_csv(archivo_csv)

# 3.4.1 (using double backslashes)
""" registro_105 = df.iloc[105]
print(registro_105)

nombre_elemento = registro_105['Nombre elemento arqueológico']
print(f'Nombre del elemento buscado es: {nombre_elemento}') """

# 3.4.2
registro = df.loc[[24, 36, 125, 182], ['Nombre elemento arqueológico', 'Ubicación actual dentro del parque']]
print(registro)

