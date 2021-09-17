import numpy as np
print("Indexación de matriz booleana", "\n")

# Creamos la matriz
a = np.array([[1, 2], [3, 4], [5, 6]])
# Hara esta condicion con todos los numeros de la matriz
bool_idx = (a > 2)
print(bool_idx, "\n")

# Podemos imprimir los valores que si cumplieron la condicion
print(a[bool_idx])
# Sin embargo, podemos ahorrarnos lineas de codigo con esto:
print(a[a > 2], "\n")
# Jugando con esto:
# Para hacer condicionales se debe de tener la misma matriz con las mismas dimensiones
b = np.array([[2, 4], [6, 8], [10, 12]])
print(b[a < b])


# Si re gusto, te recomiendo a que sigas investigando sobre la indexacion en este link:
# https: // numpy.org/doc/stable/reference/arrays.indexing.html
