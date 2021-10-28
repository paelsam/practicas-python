# Herencia: Es la capacidad de crear una clase que hereda de otra clase.
# Este puede tener las caracteristicas de la clase padre y ademas puede tener propias.

# Nota: Todas las clases heredan de la clase object.

# Creando clase Persona con los atributos nombre y edad:
class Persona(object):
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        
    # Creando Getters y Setters:
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad
    
    # __str__: Es un metodo que se ejecuta automaticamente cuando se imprime un objeto.
    def __str__(self):
        return f'Persona: [Nombre: {self.nombre}, Edad: {self.edad}]'
    
    
# Creando class Empleado 
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        # Super: Es una palabra reservada que hace referencia a la clase padre.
        # Estamos pasando los atributos de la clase padre.
        super().__init__(nombre, edad)
        self._sueldo = sueldo
        
        @property 
        def sueldo(self):
            return self._sueldo 
        
        @sueldo.setter
        def sueldo(self, sueldo):
            self._sueldo = sueldo

    def __str__(self):
        return f"Empleado: [Sueldo: {self._sueldo}] {super().__str__()}"
