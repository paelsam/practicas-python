import pandas as pd

# DataFrames
# Para crear un dataframe, simplemente creamos un diccionario.
# El cual tendra los indices y los valores


# Los elementos manzanas y narajan son columnas
# Y nos hizo 5 filas por la cantidad de valores de cada elemento
datos = {
    "Manzanas": [20,6,14,8,11],
    "Naranjas": [4,12,45,6,8]
}


compras = pd.DataFrame(datos)
print(compras)


# Ahora, cambiemos el nombre los indices por el nombre de nuestros clientes
compras = pd.DataFrame(datos, index = ["Elkin", "Fernando", "James", "Marjorie", "Brayan"])
# print(compras)


# Podemos acceder al nombre de los indices y de las columnas de la siguiente forma:
# print(compras.index)
# print(compras.columns)


# El atributo axes devuelve una lista con los ejes de la estructura (dos, al tratarse de una estructura
# bidimensional
# print(compras.axes)
# print(compras)


# Tanto el índice de filas como el de columnas poseen el atributo name. Una vez fijado, se muestra al
# imprimir la estructura
compras.index.name = "Clientes"
compras.columns.name = "Frutas"
# print(compras)


# Para acceder a los valores del DataFrame usamos lo siguiente:
# Traera una matriz con todos los valores
# print(compras.values)

# Un dataframe también tiene un atributo shape que nos informa de su dimensionalidad y del número de
# elementos en cada dimensión.
# print(compras.shape)

# Invesiga un poco mas...

