# La clase cuadrado es heredada de la clase FiguraGeometrica y Color
# Nota: El orden las clases heredadas es importante.
from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        # Ya no utilizaremos el metodo super, ya que tenemos muchas clases.
        # Ahora utilizaremos solo el nombre de la clase con el atributo self.
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)

    def area(self):
        if self._alto != self._ancho:
            return "Lo siento, pero eso no es un cuadrado"
        return self._alto * self._ancho

