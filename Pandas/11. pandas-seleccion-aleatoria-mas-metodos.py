import pandas as pd

df = pd.DataFrame(np.arange(18).reshape([6,3]), 
        index = ["a", "b", "c", "d", "e", "f"],
        columns = ["A", "B", "C"])

# Podemos extraer 3 filas de forma aleatoria, sin reemplazo (opción por defecto) y fijando como semilla del
# generador de números aleatorios el número 18, de la siguiente forma
print(df.sample(3, random_state=18))

# Si colocamos axis = 1 sacaremos las columnas
print()
print(df.sample(2, random_state=18, axis=1))

# Metodo Pop

# Otra forma de extraer datos es la proporcionada por el método pandas.DataFrame.pop, que extrae y
# elimina una columna de un dataframe.

df = pd.DataFrame(np.arange(15).reshape([3,5]), 
        index = ["a", "b", "c"],
        columns = ["A", "B", "C", "D", "E"])
print()
column = df.pop("B")
print(column)
print()
print(df)

# El metodo drop elimina solo un elemento:
s = pd.Series([1,2,3,4,5], index = ["a","b","c","d","e"])
print()
print(s)
r = s.drop("b")
print()
print(r)

# Si la etiqueta no se encontrase en la serie, se devolvería un error.

# También podemos pasar como argumento no una etiqueta, sino una lista de etiquetas. En este caso se
# eliminarán todos los elementos con dichas etiquetas:
    
r = s.drop(["d", "a"])
print()
print(r)