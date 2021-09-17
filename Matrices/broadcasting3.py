import numpy as np

# Se multiplican cada uno de los elementos de v con los dos de w
# Creando una fila por cada elemento
v = np.array([1,2,3]) # 1 x 3
w = np.array([4,5]) # 1 x 2
print(np.reshape(v, (3,1)) * w)

# Se suman cada uno de los elementos de v con los de la matriz x
# Creando asi una matriz de 2x3
x = np.array([[1, 2,3], [4,5,6]])
print(x + v)

# Se suman los elementos de la matriz x transpuesta con la matriz w 
# Que al mismo tiempo estan transpuestas
print((x.T + w).T)
# Es lo mismo que antes
print(x + np.reshape(w, (2,1)))

# Multiplicar una matriz con una constante
print(x * 2)