class Cube:
    def __init__(self, ancho, profundidad, alto):
        self.ancho = ancho
        self.profundidad = profundidad
        self.alto = alto

    def calcular_volumen(self):
        return self.ancho * self.profundidad * self.alto

ancho = int(input("Ingresa el ancho del cubo: "))
profundidad = int(input("Ingresa la profundidad del cubo: "))
alto = int(input("Ingresa el alto del cubo: "))

cubo1 = Cube(ancho, profundidad, alto)
print(f"Volumen del cubo: {cubo1.calcular_volumen()}m³")