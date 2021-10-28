from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print("Creacion de Objeto Cuadrado".center(50, "-"))
cuadrado1 = Cuadrado(10, 10, "Verde")
cuadrado1.alto = 5
cuadrado1.ancho = 5
print(cuadrado1)

print("Creacion de Objeto Rectangulo".center(50, "-"))
rectangulo1 = Rectangulo(5, 10, "Azul")
rectangulo1.alto = -1
rectangulo1.ancho = 3
print(rectangulo1)

