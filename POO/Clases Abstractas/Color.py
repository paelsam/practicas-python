# Crear clase Color con los atributos: Color y sus respectivos getters y setters.
class Color:
    def __init__(self, color):
        self._color = color
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color

    def __str__(self):
        return f"Color: {self._color}"