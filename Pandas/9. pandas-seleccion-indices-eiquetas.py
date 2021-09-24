import pandas as pd 
import numpy as np

# Pandas - Selección con índices y etiquetas

# Una muy interesante opción para seleccionar elementos de una serie pandas es usar arrays booleanos.
# Por ejemplo, partimos de la siguiente serie
s = pd.Series([5,2,-3,7,8,4])

# Podemos usar operadores logicos
# print(s < 4)

# O podemos hacer un array de booleanos:
# print()
# print(s[[True, False, False, True, True, False]])

# Podemos usar el metodo loc para extraer valores con
# Operadores logicos y condicionales
# print()
# print(s.loc[s > 2])
# print()
# print(s.loc[[True, False, False, True, True, False]])

# Tambien podemos extraer los valores de una condicion:
# Pero esta expresion solo nos mostrara un array de booleanos
# print((s < 2).values)

# Para que se muestren los valores, necesistamos el metodo iloc
# print(s.iloc[(s < 2).values])


# Selección con índices y etiquetas simultáneamente:

# Creando DataFrame con numeros del 0 al 17 (6x3)
df = pd.DataFrame(np.arange(18).reshape([6,3]), 
        index = ["a", "b", "c", "d", "e", "f"],
        columns = ["A", "B", "C"])
print(df)
print()

# El metodo get_loc devuelve el índice de la etiqueta que se adjunte como parámetro. 
print(df.columns.get_loc("B"))
print()

# El segundo, get_indexer, devuelve un array con los índices de las etiquetas que se
# adjunten en forma de lista como parámetro. Por ejemplo, partimos del siguiente dataframe
print(df.columns.get_indexer(["A", "C"]))
print()

# En el primer caso hemos pasado la etiqueta "B" y el método ha devuelto su índice (1). En el segundo caso
# hemos pasado una lista de etiquetas y hemos obtenido un array con sus índices

# Pasara lo mismo si lo hacemos con las filas