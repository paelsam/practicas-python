import numpy as np

print("Tipos de datos en Numpy")
# Numpy adivina el tipo de matriz que estamos haciendo si no se lo # especificamos
x = np.array([1, 2])
print(x.dtype)

x = np.array([1.0, 2.0])
print(x.dtype)

x = np.array([1, 2], dtype=np.int64)
print(x.dtype)

x = np.array([True, False, False, True])
print(x.dtype)