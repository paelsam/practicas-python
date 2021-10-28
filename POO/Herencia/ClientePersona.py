# Importamos todas las clases:
from herencia import * 

persona1 = Persona("Juan", 28)
# Ya con el metodo __str__() definido en la clase Persona, podemos imprimir la informacion del objeto persona1:
# print(persona1)

empleado1 = Empleado("Elkin", 30, 5000)
# Hereda el metodo __str__() de la clase Persona, pero sus atributos no se mostraran.
# Porque el metodo __str__() aun no esta definido en la clase Empleado.
print(empleado1)

empleado2 = Empleado("Margarita", 26, 9000)
print(empleado2)