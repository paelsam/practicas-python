class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    
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
    
    def mostrar_detalle(self):
        print(f"Nombre: {self._nombre} {self._apellido} {self._edad}")
    
    # Esto no es muy comun, pero es una forma de destruir un objeto   
    def __del__(self):
        print(f"Se eliminó un objeto: {self._nombre} {self._apellido}")