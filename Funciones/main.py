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

# Tambien podemos pasar como argumentos un diccionario.
# Lo hacemos añadiendo dos **kwargs
# (por defecto es asi, pero podemos poner como nombre lo que queramos)
# Si queremos, podemos pasar ningun argumento
# La llave o Key debe ir sin comilla, pero si el valor

def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print("{}: {}".format(llave, valor))
# listarTerminos(IDE="Integred Development Enviroment", PK="Primary Key")
# listarTerminos(DBMS="Database Management System")

