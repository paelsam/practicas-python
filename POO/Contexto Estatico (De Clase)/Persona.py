class Persona: 
    # Creamos la variable contador que es una variable de clase
    contador_personas = 0
    
    # Creamos un metodo que aumenta el contador de personas:
    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas
    
    # Creamos metodo constructor
    # No declaramos la varble id_persona porque es una variable de clase
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
        # Ya declarada las propiedades de la clase, se incrementa el contador
        # Ya no lo necesitamos porque tenemos la funcion de incrementar el contador
        # Persona.contador_personas += 1
        
        # Y se añade el metodo generar_siguiente_Valor() a la instancia id_persona
        self.id_persona = Persona.generar_siguiente_valor()
    
    def __str__(self):
        return "ID: [{}], Persona: [{}], Edad: [{}]".format(self.id_persona, self.nombre, self.edad)


if __name__ == "__main__":
    Persona1 = Persona("Juan", 20)
    Persona2 = Persona("Pedro", 30)
    Persona3 = Persona("Ana", 40)
    Persona4 = Persona("Maria", 50)
    Persona5 = Persona("Juana", 60)
    Persona6 = Persona("Jorge", 70)
    # Este metodo es contraproducente, ya que no se puede llamar a Persona.contador_personas
    # Y perderiamos el id de la personas
    Persona.generar_siguiente_valor()
    # Este objeto no tendran ID 7 porque llamamos a la funcion generar_siguiente_valor() antes
    Persona7 = Persona("Juan", 80)
    print(Persona1)
    print(Persona2)
    print(Persona3)
    print(Persona4)
    print(Persona5)
    print(Persona6)
    print(Persona7)
    print("Valor del Contador: {}".format(Persona.contador_personas))
    