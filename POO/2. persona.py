# Agregaremos parametros al metodo init

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1 = Persona("Elkin", "Panameño", 16)
print(persona1.nombre, persona1.apellido, persona1.edad)