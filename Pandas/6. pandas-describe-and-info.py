import pandas as pd

# Metodo Describe
# Nos muestra toda la informacion estadistica del DataFrame
# En otro DataFrame

entradas = pd.Series([11,18,12,16,9,16,22,28,31,29,30,12],
                     index = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dec"])

salidas = pd.Series([9,26,18,15,6,22,19,25,34,22,21,14], 
                    index = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dec"])

# Creando DataFrame:
almacen = pd.DataFrame({"Entradas": entradas, "Salidas": salidas})
almacen["Neto"] = almacen.Entradas - almacen.Salidas

# Esta información incluye el número de muestras, el valor medio, la
# desviación estándar, el valor mínimo, máximo, 
#la mediana y los valores correspondientes a los percentiles 25% y 75%
print(almacen.describe())

# Metodo Info
# El método info muestra un resumen de un dataframe, incluyendo 
# información sobre el tipo de los índices de filas y columnas, 
# los valores no nulos y la memoria usada:
print()
print(almacen.info())