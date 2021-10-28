# ABC = Abstract Base Class
# Clases Abstractas: Son clases que no pueden ser instanciadas, sino que deben ser heredadas por otras clases.
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
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
       
    
    @property
    def ancho(self):
        return self._ancho
    
    
    @abstractmethod
    def area(self):
        pass

    
    def __str__(self):
        return "Ancho: {} - Alto: {}".format(self._ancho, self._alto)
    
    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False