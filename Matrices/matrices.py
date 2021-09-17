import numpy as np

# Creando un vector:
# Matriz Irregular: No tiene numero de filas y columnas iguales.
print("Matriz A")
a = np.array([34, 25, 7])
print(f"{a}:", type(a))
# Es como el len, muestra el numero de parametros en una matriz
print(a.shape)
# Podemos indexar normalmente como si fuera una lista
# Teniendo en cuenta las filas y las columnas de la matriz
print(a[0], a[1], a[2])
# Cambiar un elemento de una matriz
a[0] = 5
print(a)
# Haciendo otra matriz:
print("\nMatriz B")
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print(b.shape, "Primero muestra el numero de elementos que hay en una fila y luego el de la columna.")
# Indexacion: Primero ponemos la fila y luego la columna para poder encontrar el valor.
print(b[0, 0], b[0, 1], b[1, 0])
