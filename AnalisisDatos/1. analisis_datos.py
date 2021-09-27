# Analisis de Datos

# Importamos la libreria para hacer graficas
import matplotlib.pyplot as plt

# Grafico usando listas:
x1 = [2, 5, 6, 14]
y1 = [11, 22, 33, 44]

x2 = [2, 5, 6, 15]
y2 = [4, 12, 18, 45]

# Graficar 2 lineas en la misma grid(Grafica de Lineas)
# plt.plot(x1, y1, color="blue", linewidth=3, label="Linea 1")
# plt.plot(x2, y2, color="green", linewidth=3, label="Linea 2")

# plt.title("Dos graficas juntas")
# plt.xlabel("Eje X")
# plt.ylabel("Eje Y")
# plt.legend()
# plt.grid()
# plt.show()

# Grafica de barras con las mismas listas
# plt.bar(x1, y1, color="blue", linewidth=3, label="Barra 1")
# plt.bar(x1, y2, color="green", linewidth=3, label="Barra 2")

# plt.title("Dos barras juntas")
# plt.xlabel("Eje X")
# plt.ylabel("Eje Y")
# plt.legend()
# plt.grid()
# plt.show()

# Creando un Histograma
# Datos = [20, 22, 21, 20, 23, 25, 28, 40, 22, 23,
#          22, 15, 16, 18, 18, 19, 21, 22, 24, 4, 12, 17, 17, 22, 30]
# RangoBin = [0,10,20,30,40]

# plt.hist(Datos, RangoBin, histtype="bar", rwidth=0.8, color="gray")
# plt.title("Histograma de Elkin")
# plt.xlabel("Eje X")
# plt.ylabel("Eje Y")
# # El plt.grid() no es necesario
# plt.show()


# Creando grafica circular
valores = [20, 40, 60, 80]

# Autopct = Nos pone los porcentajes de cada uno de las partes
# Explode = Hace que una parte del digrama se vea como "salido"
# Shadow = Genera sombras
plt.pie(valores, labels=["Prekinder", "Kinder", "Primaria", "Secundaria"], colors=[
        "red", "lightblue", "blue", "orange"], startangle=90, shadow=True, explode=(0.1, 0, 0, 0), autopct="%1.1f%%")
plt.title("Grafico Circular")
plt.show()
