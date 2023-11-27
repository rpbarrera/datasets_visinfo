import pandas as pd

# Lista de archivos CSV a unir
archivos_csv = ['accessories.csv', 'bags.csv', 'bottoms.csv', 'construction.csv', 'dress-up.csv', 'fencing.csv', 'floors.csv', 'headwear.csv',
                 'housewares.csv', 'miscellaneous.csv', 'other.csv','shoes.csv','socks.csv','tools.csv','tops.csv','umbrellas.csv']  # Añade tus archivos aquí

# Columnas que quieres conservar
columnas_deseadas = ['Name', 'Image', 'tipo']

# Leer y concatenar los archivos CSV
df_concatenado = pd.concat((pd.read_csv(archivo)[columnas_deseadas] for archivo in archivos_csv))

# Guardar el dataframe concatenado en un nuevo archivo CSV
df_concatenado.to_csv('csv_unidos.csv', index=False)
