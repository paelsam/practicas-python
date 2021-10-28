from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from FiguraGeometrica import FiguraGeometrica

# No se puede instanciar una clase abstracta
# figura = FiguraGeometrica()

print("Creacion de Objeto Cuadrado".center(50, "-"))
cuadrado1 = Cuadrado(10, 10, "Verde")
# Just Read Only
# cuadrado1.alto = 5
# cuadrado1.ancho = 5
print(cuadrado1)

print("Creacion de Objeto Rectangulo".center(50, "-"))
rectangulo1 = Rectangulo(5, 10, "Azul")
# Just Read Only
# rectangulo1.alto = -1
# rectangulo1.ancho = 3
print(rectangulo1)

# Se modifico el orden de las clases.
print(Cuadrado.mro())
