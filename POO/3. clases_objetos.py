# Una clase es una plantilla por la cual podemos crear objetos
# Para añadir atributos, utilizamos el metodo init
# Self es una referencia al objeto en si mismo

class Persona:
    def __init__(self):
        self.name = "Elkin"
        self.apellido = "Panameño"
        self.age = 15

print(type(Persona))

persona = Persona()
print(persona.name, persona.apellido, persona.age)
