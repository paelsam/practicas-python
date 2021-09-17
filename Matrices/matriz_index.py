import numpy as np

# Creamos la matriz 3x3
a = np.array([[1, 2, 3], [5, 6, 7], [9, 10, 11]])
# Aqui estamos tomando los valores de:
# La fila entre 0 y 2 (Sin contar el 2) (:2)
# Las columnas entre el 1 y 3 (Sin contar el 3) (1:3)
b = a[:2, 1:3]
print(f"{b} \n")
# Para cambiar la posicion de los numeros al contrario
# (Como el reverse en las listas)
print(f"{np.fliplr(a)} \n")
# Para mostrar un solo dato
print(f"{a[0, 1]} \n")
# Es lo mismo que a[0, 1]
# No te recuerdas cierto? XD Mira las matrices a y b nuevamente
b[0, 0] = 77
# Prints 77
print(a[0, 1])
