# Crear una clase llamada MiClase con una variable de clase llamada variable_clse
class MiClase:
    variable_clase = "Variable de Clase"
    def __init__(self, variable_instancia):
        self.variable_instancia = "Variable de Instancia"
    
    # No recibe ningun parametro
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)
        
    # Metodo de Clase: No se puede acceder a las variables de instancia.
    # Recibe un parametro de tipo MiClase
    # cls: Referencia a la clase (La clase en si misma). Se utiliza para acceder a las variables de clase.
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)
        
    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)
        
MiClase.metodo_clase()
# Contexto Estatico: Se utiliza para acceder a las variables de clase.
miObjeto1 = MiClase('variable_instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()

# Una clase no puede acceder a las variables de instancia porque aun no se han creado objetos de la clase.
# Constantes: Se utilizan para definir un valor que no puede cambiar.