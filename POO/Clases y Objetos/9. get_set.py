# Podemos acceder a los atributos encapsulados con los metodos get y set.
# Get: Nos permite obtener el valor de un atributo.
# Set: Nos permite modificar el valor de un atributo.
# Les mostrare un ejemplo:

class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        
    # @property permite que solo podamos acceder a esta instancia con este metodo.
    # Para llamar a este metodo no es necesario poner parentesis.
    @property
    def nombre(self):
        print("Ejecutando el metodo get_nombre")
        return self._nombre
    
    # @nombre.setter permite modificar el valor de este atributo.
    @nombre.setter
    def nombre(self, nombre):
        print("Ejecutando el metodo set_nombre")
        self._nombre = nombre
        
    # Podemos hacer atributos read-only quitando el setter.
    
persona1 = Persona('Juan', 'Perez', 25)
# Primero se ejecuta el metodo set, ya estamos modificando el valor de la instancia.
# Luego se ejecuta el metodo get, retornando el valor que modificamos anteriormente.
persona1.nombre = "Elkin"
print(persona1.nombre)
