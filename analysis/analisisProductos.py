import pandas as pd


from helpers.crearCSVProductos import crearCSVProductos

from data.producto import productos

#1. Crear un CSV con los datos de las ventas
crearCSVProductos(productos,'productos.csv')

"#2 Cargo la fuente de datos y con pandos PANDAS creo un DATAFRAME"
productosDataFrame=pd.read_csv('data/productos.csv')
print(productosDataFrame)

#3.Explorar los datos
examen1 = productosDataFrame.head()
examen2 = productosDataFrame.tail()
examen3 = productosDataFrame.head(20)
examen4 = productosDataFrame.info()
examen5 = productosDataFrame.describe()
examen6 = productosDataFrame.tail(50)

#4.Filtrar y ordenar (limpiar)

#5. aplicar modelos estadísticos

#6. Presentar y explorar losd datos
print(examen1)
print("\n")
print(examen2)
print("\n")
print(examen3)
print("\n")
print(examen4)
print("\n")
print(examen5)
print("\n")
print(examen6)
print("\n")
