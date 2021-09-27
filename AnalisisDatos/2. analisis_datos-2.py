import matplotlib.pyplot as plt
import pandas as pd

# USO DE GRAFICAS EN UN DATAFRAME
df = pd.DataFrame({
    "Nombre": ["John", "Maria", "Pedro", "Jenifer", "Bob", "Lisa", "Jose"],
    "Edad": [23, 78, 22, 19, 45, 33, 20],
    "Ciudad": ["Bogota", "Medellin", "Bogota", "Medellin", "Bogota", "Armenia", "Armenia"],
    "Num_niños": [2, 0, 0, 3, 2, 1, 4],
    "Num_mascotas": [5, 1, 0, 5, 2, 2, 3]
})

# Creamos la grafica de dispersion
# df.plot(kind="scatter", x="Num_niños", y="Num_mascotas", color="red")

# De barras
# df.plot(kind="bar", x="Nombre", y="Edad", color="yellow")

# La variable ax toma los datos de los ejes actuales
ax = plt.gca()
df.plot(kind="line", x="Nombre", y="Num_niños", ax=ax)
df.plot(kind="line", x="Nombre", y="Num_mascotas", color="lightblue", ax=ax)


plt.show()
