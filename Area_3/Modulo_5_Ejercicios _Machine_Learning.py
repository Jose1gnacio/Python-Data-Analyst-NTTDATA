import pandas as pd


#3.7.6
# Datos proporcionados
datos = {
    'Nombre': ['Luis Zafra', 'Gemma Sanz', 'Lourdes Mora', 'Isaac Pérez', 'Sonia Gracia', 
               'Alberto Lungo', 'Tamara López'],
    'Fecha nacimiento': ['15/05/1993', '25/04/2000', '04/12/1985', '18/10/1999', '02/08/2001', 
                         '11/11/1986', '06/07/1991'],
    'Zona': [0, 2, 1, 3, 0, 1, 1],
    'Artículo': [348, 125, 3, 248, 124, 17, 157],
    'Cantidad': [1, 3, 2, 1, 1, 1, 2],
    'Entregado': ['Sí', 'No', 'Sí', 'Sí', 'No', 'Sí', 'Sí'],
    'Método pago': ['Tarjeta', 'Transferencia', 'Bizum', 'Tarjeta', 'Tarjeta', 
                    'Transferencia', 'Contrareembolso'],
    'Dto': ['No', 'Sí', 'No', 'No', 'No', 'Sí', 'Sí']
}

df = pd.DataFrame(datos)

#print(f"DataFrame original: \n{df.dtypes}")

df['Fecha nacimiento'] = pd.to_datetime(df['Fecha nacimiento'], format='%d/%m/%Y', errors='raise')
df['Entregado'] = df['Entregado'].astype('category')
df['Método pago'] = df['Método pago'].astype('category')
df['Dto'] = df['Dto'].astype('category')

#print(f"\nDataFrame con tipos ajustados: \n {df.dtypes}")

#3.7.7
# Calcular la fecha de 40 cumpleaños sumando 40 años a la fecha de nacimiento
df['40 cumpleaños'] = df['Fecha nacimiento'] + pd.DateOffset(years=40)

# Mostrar el dataframe con la nueva columna agregada
print("DataFrame con columna '40 cumpleaños':")
print(df)


