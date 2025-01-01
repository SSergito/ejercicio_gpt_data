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

# Extrae el año y mes de las fechas de transacción en una nueva columna
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["Year-Month"] = df["date"].dt.to_period("M").astype(str)
print(df["Year-Month"])

# Identifica cuántos productos únicos hay en el dataset
print(f"Número de productos únicos: {len(df["product"].unique())}")

# Encuentra el producto más caro vendido
most_expensive = df.loc[df["price"] == df["price"].max()]
print("Producto más caro vendido:")
print(most_expensive)

# Genera un resumen estadístico (mean, std, min, max) de la columna precio
