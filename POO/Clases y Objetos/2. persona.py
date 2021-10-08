# Agregaremos parametros al metodo init

# La clase es como un molde para crear nuevos objetos
class Persona:
    def __init__(self, nombre, apellido, edad):
        # Atributos de instancia: Son los atributos que recibira el objeto
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


# Creando un objeto:
persona1 = Persona("Elkin", "Panameño", 16)
# Accediendo a sus atributos
print(f"Obejto 1: {persona1.nombre} {persona1.apellido} {persona1.edad}")

# Creando otro objeto:
persona2 = Persona("Karla", "Gomes", 30)
print(f"Obejto 2: {persona2.nombre} {persona2.apellido} {persona2.edad}")

persona3 = Persona("Mar", "Val", 16)
print(f"Obejto 3: {persona3.nombre} {persona3.apellido} {persona3.edad}")

# Modificando atributos de un objeto
# Esto no es recomendable, la mejor forma es aprendiendo encapsulamiento
print("\n")
persona1.nombre = "Elkin Samir"
persona1.apellido = "Angulo Panameño"
persona1.edad = 17
print(f"Obejto 1: {persona1.nombre} {persona1.apellido} {persona1.edad}")

persona2.nombre = "Marjorie"
persona2.apellido = "Valencia"
persona2.edad = 17
print(f"Obejto 2: {persona2.nombre} {persona2.apellido} {persona2.edad}")
