import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    "Nombre": ["John", "Maria", "Pedro", "Jenifer", "Bob", "Lisa", "Jose"],
    "Edad": [23, 78, 22, 19, 45, 33, 20],
    "Ciudad": ["Bogota", "Medellin", "Bogota", "Medellin", "Bogota", "Armenia", "Armenia"],
    "Num_niños": [2, 0, 0, 3, 2, 1, 4],
    "Num_mascotas": [5, 1, 0, 5, 2, 2, 3]
})

# Tomamos los elemntos de la columna Ciudad
# Basado en el las ciudades de las que son los Nombre
#  Luego se imprime una grafica con todas las ocurrencias de cada Ciudad
# df.groupby("Ciudad")["Nombre"].nunique().plot(kind="bar")


# Podemos ver el tipo de clase de estos elementos facilmente
# df.groupby(["Ciudad", "Edad"]).size().unstack().plot(kind="bar", stacked=True)

# Mas graficas:
df[['Edad']].plot(kind="hist", bins=[0, 20, 40, 60, 80, 100], rwidth=.8)
plt.show()
