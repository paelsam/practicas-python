# Los metodos en POO son funciones, pero se llaman asi porque estan
# Asociadas a las clases
# Un metodo es la accion que hace un objeto
# Diagramas UML: Se utilizan para modelar clases, objetos, etc

# Creando clase Persona
# Nota: El parametro self solo se utiliza en la clase, fuera de la clase NO
# Podemos añadir tuplas o diccionarios con *args o **kwargs
class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        # Atributos de instancia: Son los atributos que recibira el objeto
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    # Creando metodos de instancia:
    def mostrar_detalle(self):
            return f"Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}"

# Creando un objeto:
persona1 = Persona("Elkin", "Panameño", 16, "Hola Mundo", 22, 8, m="Manzanas", p="Peras")
# Accediendo a sus atributos a traves del metodo mostrar_detalle:
print(persona1.mostrar_detalle())
# Podemos añadir nuevos atributos a los objetos.
# Pero estos solo se quedaran con el objeto que se creo
persona1.telefono = "3154321541"
print(f"Persona Telefono: {persona1.telefono}")

# Creando otro objeto:
persona2 = Persona("Karla", "Gomes", 30)
print(persona2.mostrar_detalle())

# Caracteristicas del parametro self:
# - En otros lenguajes de programcion, en vez de self se llama this
# - El nombre self puede ser cualquier otro nombre, como this o papa xd
# - Podemos llamar directamente al metodo con la clase Persona en vez del objeto

# Esto no es muy comun:
# print(Persona.mostrar_detalle(persona1))