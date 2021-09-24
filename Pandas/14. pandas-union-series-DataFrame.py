import pandas as pd 
import numpy as np

# Primero veremos la union de Series:
    
s = pd.Series([1,2,3,4,5], index = ["a", "b", "c", "d", "e"])
r = pd.Series([10,11,12], index = ["f", "g", "h"])

# Podemos unir estas dos Series con la funcion concat
t = pd.concat([s,r])
print(type(t))
print(t)

# Si algunas etiquetas se repiten podemos poner axis = 1 creando asi una una columna
# Con los valores de las etiquetas identicas de las dos Series
# Los que no tienen retornaran el valor de NaN
# Se convierte en un DataFrame

a = pd.Series([1,2,3,4,5], index = ["a", "b", "c", "d", "e"])
b = pd.Series([10,11,12], index = ["a", "b", "h"])

c = pd.concat([a,b], axis=1, sort=True)
print(type(c))
print(c)

# No hay problema si la etiquetas son iguales
# Estas pueden estar en las misma Serie o DataFrame
print()
print(pd.concat([a,b]))


# Metodo Append: Es lo mismo que el metodo concat pero mas limitado
c = a.append(b)
print()
print(c)

# Con el metodo append, podemos omitir las etiquetas y solo dejar los indices 
c = a.append(b, ignore_index=True)
print()
print(c)

# Union de DataFrames
df1 = pd.DataFrame(np.arange(4).reshape([2,2]), index = ["a", "b"], columns = ["A", "B"])
print()
print(df1)

df2 = pd.DataFrame(np.arange(5,9).reshape([2,2]), index = ["a", "b"], columns = ["A", "B"])
print()
print(df2)

print()
print(pd.concat([df1,df2]))

# Investigar Mas...
