import numpy as np

# Creando la matriz
a = np.array([[1, 2], [3, 4], [5, 6]])
# print(a)
# print(a.shape)
print(a[[0, 1, 2], [0, 1, 0]])
# Esto es lo mismo que lo anterior. No lo entendi, asi que hay que preguntarle al profesor
print(np.array([a[0, 0], a[1, 1], a[2, 0]]))
# Tampoco entiendo esto. Hay que preguntar
# print(a[[0, 0], [1, 1]])
# # Lo mismo que lo anterior
# print(np.array([a[0, 1], a[0, 1]]))

# # Creando una nueva matriz
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# print(a, "\n")
# # Creando una serie de indices
# b = np.array([0, 2, 0, 1])
# a[np.arange(4), b] += 10
# print(a, "\n")
