import pandas as pd

# Carga el dataset en un DataFrame de pandas y muestra las primeras 10 filas
df = pd.read_csv("sales_data.csv")
print(df.head(10))

# Obtén un resumen de las columnas, tipos de datos y valores nulos
print(df.info())
print(df.isnull().sum())

# Cuenta el número total de filas y columnas en el dataset
rows, columns = df.shape
print(f"Número de filas: {rows}\nNúmero de columnas: {columns}")

# Filtra las transacciones para un producto específico
df_watch = df.loc[df["product"] == "Smartwatch"]
print(df_watch)

# Ordena las transacciones por fecha
print(df.sort_values(by="date",ascending=True))

# Calcula el precio promedio de los productos vendidos.
print(f"Precio promedio de ventas: {df["price"].mean():.2f}")
##### Extra a la pregunta quiero hallar el precio promedio por cada producto
precios_promedio = df.groupby("product")["price"].mean()

for producto, promedio in precios_promedio.items():
    print(f"Precio promedio de {producto}: {promedio:.2f}")