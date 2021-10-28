# Variables de Clase: Son variables que se pueden acceder desde cualquier lugar de la clase.
# Variables de Instancia: Son variables que se asignan a un objeto.
# Variables de clase al vuelo: Podemos crear variables de clase en cualquier momento.

class MiClase:
    variable_clase = "Valor Variable Clase"
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    # Metodo estatico: Se puede llamar sin instanciar la clase.
    # Un metodo estatico no puede acceder a variables de instancia (No poner self).
    # Podemos llamar una variable de clase de manera indirecta.
    @staticmethod
    def metodo_estatico():
        print("Metodo Estatico")
        print(MiClase.variable_clase)

    def metodo_instancia(self):
        print("Metodo Instancia")
        print(self.variable_instancia)
        print(MiClase.variable_clase)
    
    
# Así accedemos a una variable de clase:
print(MiClase.variable_clase)

# Para accerder una variable de instancia debemos crear un objeto de la clase:
miClase = MiClase("Valor Variable Instancia")
print(miClase.variable_instancia)

# El objeto tambien puede acceder a la variable de clase:
print(miClase.variable_clase)


miClase2 = MiClase("Otro Valor Variable Instancia")
print(miClase2.variable_instancia)
print(miClase2.variable_clase)

# Creando una variable de clase al vuelo:
MiClase.variable_clase2 = "Valor Variable Clase 2"
print(MiClase.variable_clase2)
print(miClase.variable_clase2)

print(MiClase.metodo_estatico())