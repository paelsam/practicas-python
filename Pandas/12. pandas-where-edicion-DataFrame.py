import pandas as pd

# Metodo Where que nos ayuda a filtrar los datos por medio de una condicion.
# Los que no la cumplen retornan un NaN

s = pd.Series(np.arange(0,10))

# Ahora filtraremos los numero pares
# Podemos pasar como segundo argumento el reemplazo del mensaje para los 
# Elementos que no cumplen la condicion
par = s.where(s % 2 == 0, "Impar")
print(par)

