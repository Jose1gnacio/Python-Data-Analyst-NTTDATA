import pandas as pd

#3.4.1
archivo_csv = r'C:\Users\josei\Documents\NTT DATA CLASES\Área 3 - Material de clases\Modulo_3\Esculturas_Parque_Arqueolgicos_Colombia.csv'
df = pd.read_csv(archivo_csv)
registro_105 = df.iloc[105]
print(registro_105)

nombre_elemento = registro_105['Nombre elemento arqueológico']
print(f'Nombre del elemento buscado es: {nombre_elemento}')
