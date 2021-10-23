# Encapsulamiento: Es la idea de que los datos de un objeto no se pueden modificar fuera de la clase.
# Mostrare un ejemplo de encapsulamiento.

class Persona:
    def __init__(self, nombre, apellido, edad):
        # Estos son atributos encapsulados solo ponemos un "_" antes de su nombre.
        # Son mas comunes de encontrar.
        self._nombre = nombre
        self._apellido = apellido
        # Si queremos ser mas esctrictos, podemos usar el "__" para hacer un atributo privado.
        # Son menos comunes que los de "_".
        self.__edad = edad
    
    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self.__edad}')

persona1 = Persona('Juan', 'Perez', 23)
# No es recomendable
persona1._nombre = 'Pedro'
persona1.__edad = 24

persona1.mostrar_detalle()