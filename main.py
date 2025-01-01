import pandas as pd

# Carga el dataset en un DataFrame de pandas y muestra las primeras 10 filas
df = pd.read_csv("sales_data.csv")
print(df.head(10))

# Obtén un resumen de las columnas, tipos de datos y valores nulos
print(df.info())
print(df.isnull().sum())

# Cuenta el número total de filas y columnas en el dataset
