class AreaRectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

width = int(input("Ingresa la base del rectangulo: "))
height = int(input("Ingresa la altura del rectangulo: "))

rectangulo1 = AreaRectangle(width, height)
print(f"Área del rectangulo: {rectangulo1.area()}")