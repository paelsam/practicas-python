# Modulos: son archivos que contienen funciones y clases. Y tienen la capacidad de pasarse a otros archios.
# Como llamar a un modulo: 
# from nombre_del_archivo import nombre_de_la_funcion_o_clase
# Por ejemplo: 
from destructores import Persona
# Para llamar a todas las clases y funciones de un modulo, usamos el *.


print("Creacion Objetos".center(50, "-"))
persona1 = Persona("Juan", "Perez", 23)
# Tambien se ejecutaran las pruebas que hicimos en el archivo anterior.
# Update: ahora ya no se ejecutaran las pruebas que hicimos en el archivo mas_encapsulamiento.py
# Por el condicional que hicimos anteriormente.
persona1.mostrar_detalle()
# Este es el modulo principal, pero solo de este archivo.
# Entonces se mostraran solo las pruebas que hemos hecho en este archivos.

print("Eliminacion de objetos (DESTRUCTOR!)".center(50, "-"))
del persona1 # Esto eliminara el objeto persona1.