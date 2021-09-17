# Matematicas de Matriz
import numpy as np

x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)

# Suma  de Elementos de las Matrices
# Primera forma:
print(x + y, "\n")
# Segunda forma:
print(np.add(x, y), "\n")

# Resta de Elementos de las Matrices
# Primera Forma:
print(x - y, "\n")
# Segunda forma
print(np.subtract(x, y), "\n")

# Multiplicacion de Elementos de las Matrices
# Primera Forma:
print(x * y, "\n")
# Segunda forma
print(np.multiply(x, y), "\n")

# Division de Elementos de las Matrices
# Primera Forma:
print(x / y, "\n")
# Segunda forma
print(np.divide(x, y), "\n")

# Raiz cudadrada de Elementos de las Matrices
print(np.sqrt(x, y), "\n")
