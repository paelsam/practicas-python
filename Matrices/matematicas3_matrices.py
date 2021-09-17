import numpy as np

x = np.array([[1, 2], [3, 4]])
print(np.sum(x))
print(np.sum(x, axis=0))  # Imprime la suma de cada columna
print(np.sum(x, axis=1))  # Imprime la suma de cada fila

# Trasposicion de la matriz
print("\n", x.T)

# Los vectores de una sola fila o columna No se pueden transponer
y = np.array([1, 2, 3])
print("\n", y)
print(y.T)
