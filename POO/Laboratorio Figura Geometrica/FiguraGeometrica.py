# Crear clase figura geometrica con los atributos ancho y alto y sus respectivos getters y setters.
class FiguraGeometrica:
    def __init__(self, alto, ancho):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f"Valor erroneo: {alto}")
        if self._validar_valor(ancho):
            self._ancho = ancho
        else: 
            print(f"Valor erroneo: {ancho}")
            self._ancho = 0
                
    @property
    def alto(self):
        return self._alto
    
    @alto.setter
    def alto(self, alto):
        # Validamos el valor
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f"Valor erroneo: {alto}")
    
    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self, ancho):
        # Validamos el valor
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f"Valor erroneo: {ancho}")

    
    def __str__(self):
        return "Ancho: {} - Alto: {}".format(self._ancho, self._alto)
    
    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False