# Creando la clase color
class Color:
    def __init__(self, color):
        self._color = color

    # Añadiendo getters y setters
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color