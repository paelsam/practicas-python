import numpy as np


a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Si queremos acceder a los valores de una fila
# Primera fila, todas las columnas
row_r1 = a[1, :]
# Selecciona la fila entre las 1 y 2 (sin contar el 2)
# Y todas la columnas
row_r2 = a[1:2, :]
print(row_r1, row_r1.shape)
print(row_r2, row_r2.shape)
print("\n")

# Si queremos acceder a los valores de una columna
# Es el mismo proceso que con las filas
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)
print(col_r2, col_r2.shape)
print("\n")
