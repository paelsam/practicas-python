import numpy as np

# Creando matriz de ceros de 3x3 (Fila-Columna)
matriz = np.zeros((3, 3))
print(matriz)

# Creando matriz de unos de 1x2 (Fila-Columna)
matriz2 = np.ones((1, 2))
print(matriz2)

# Creando matriz de una constantes (7) de 2x2
matriz3 = np.full((2, 2), 7)
print(matriz3)

# Creando matriz de identidad (1 y 0) de 2x2
matriz_identidad = np.eye(2)
print(matriz_identidad)

# Creando matriz con datos aleatorios (Puede entregar valores decimales muy pequeños)
matriz_random = np.random.random((2, 2))
print(matriz_random)
