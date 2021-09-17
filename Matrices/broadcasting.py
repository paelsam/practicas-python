import numpy as np

# BROADCASTING:
# El Broadcasting es un mecanismo poderoso que permite a numpy trabajar con matrices de diferentes
# formas al realizar operaciones aritméticas.

x = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
v = np.array([1,0,1])
y = np.empty_like(x) # Crear una matriz vacia con la misma forma de x

# Agregar el vector v a cada fila de la matriz x con un bucle explicito
for i in range(4):
    y[i, :] = x [i, :] + v # Se añaden a la matriz "y" la suma de la matriz x & v
print(y)

# El proceso de arriba es algo lento asi que lo mejoraremos un poco:
vv = np.tile(v, (4,1)) # hacemos una matriz con la misma forma que la matriz x
print(vv)

# Añadimos x y vv. Tendremos lo mismo que lo anterior pero mucho mas facil
y = x + vv 
print(y)