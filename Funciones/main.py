# Argumentos Varibales
# El argumento con un * es una tupla. Asi que podemos añadir muchos datos
# Comunmente lo vemos escrito asi: *args
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)


# listarNombres("Juan", "Carla", "Maria", "Ernesto")
# listarNombres("Laura", "Carlos")


def numeros(*args):
    suma = 1
    for numero in args:
        suma *= numero
    print(suma)


# numeros(0,1,2,3,4)
