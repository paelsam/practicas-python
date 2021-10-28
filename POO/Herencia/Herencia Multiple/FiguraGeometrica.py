class FiguraGeometrica:
    def __init__(self, ancho, alto): 
        self._ancho = ancho
        self._alto = alto
    
    # Añadiendo los getters y setterss
    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho