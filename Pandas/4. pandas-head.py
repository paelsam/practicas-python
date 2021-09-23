import pandas as pd

# El metodo head nos ayuda a mostras los primeros
# Elementos de la serie o el DataFrame

entradas = pd.Series([11,18,12,16,9,16,22,28,31,29,30,12],
                     index = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dec"])

salidas = pd.Series([9,26,18,15,6,22,19,25,34,22,21,14], 
                    index = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dec"])

# Creando DataFrame:
almacen = pd.DataFrame({"Entradas": entradas, "Salidas": salidas})
almacen["Neto"] = almacen.Entradas - almacen.Salidas
# print(almacen)

# Para ejecutar los primeros elementos de la lista 
# Utilizamos la funcion head
# Por defecto la funcion head solo muestra 5 indices horizontales
# Pero podemos filtrarlo al numero que queramos
print(entradas.head())
print()
print(almacen.head(3))

