# Aprenderemos algunas cosas sobre el metodo init
# Si queremos pasar una tupla de valores a una clase, debemos hacerlo con el metodo *args
# Si queremos pasar un diccionario de valores a una clase, debemos hacerlo con el metodo **kwargs
# Nota: *args y *kwargs pueden cambiar de nombre, pero no es recomendable

class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos
    
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')


persona1 = Persona('Juan', 'Perez', 30, "11111234", 2, 3, 4, 5, NFT="Cosa cara", BITCOIN="Criptomoneda")
persona1.mostrar_detalle()
