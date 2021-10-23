# Haremos la clase persona con todos sus atributos encapsulados:

class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._edad = edad
        self._apellido = apellido
        
    
    @property
    def nombre(self):
        return self._nombre  
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad
        
    def mostrar_detalle(self):
        print(f"Persona: {self._nombre} {self._apellido} {self._edad}")
    

# Este es el modulo principal, por eso mostrara el resultado de __main__:
print(__name__)

# Para evitar que esto se muestre en otro archivo, haremos una condicional:
if __name__ == "__main__":
    persona1 = Persona("Juan", "Perez", 28)
    persona1.nombre = "Elkin Samir"
    persona1.apellido = "Angulo"
    persona1.edad = 17
    persona1.mostrar_detalle()
