# Clase Rectangulo que se hereda de FiguraGeometrica y Color
from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)
    
    def area(self):
        return self._alto * self._ancho
    
    def __str__(self):
        return f"{FiguraGeometrica.__str__(self)}, {Color.__str__(self)}, Area: {self.area()}"
        
