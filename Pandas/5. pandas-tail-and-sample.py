import pandas as pd

# Metodo Tail
# Lo contrario al la funcion head
# Esta mostrara los ultimos indices horizontales de la serie o DataFrame

entradas = pd.Series([11,18,12,16,9,16,22,28,31,29,30,12],
                     index = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dec"])

salidas = pd.Series([9,26,18,15,6,22,19,25,34,22,21,14], 
                    index = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dec"])

# Creando DataFrame:
almacen = pd.DataFrame({"Entradas": entradas, "Salidas": salidas})
almacen["Neto"] = almacen.Entradas - almacen.Salidas

# Podemos indicarle cuantos indices quiere que nos muestre
# Por defecto nos muestra 5 indices
print(entradas.tail())
print()
print(almacen.tail(3))

# Metodo Sample
# Nos muestra 1 dato aleatorio de nuestra Serie o DataFrame
# Podemos pedirle mas si lo señalamos
print()
print(entradas.sample())
print()
print(entradas.sample(5))
