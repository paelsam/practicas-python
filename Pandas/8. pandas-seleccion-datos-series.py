import pandas as pd

s = pd.Series([10,20,30,40])
print(s)

# Notacion por corchetes
print(s[0])
print(s[2])

# Podemos asignar indices de forma explicita:
s = pd.Series([10,20,30,40], index=["a","b","c","d"])
print()
print(s)

# Podemos seleccionar datos con los indices explicitos:
print()
print(s["a"], s[0])
print(s["d"], s[3])

# Con el metodo iloc podemos indexar
print()
print(s.iloc[1:])