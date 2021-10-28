from Cuadrado import Cuadrado

cuadrado1 = Cuadrado(20,20,"Azul")
print(cuadrado1.area())

# Método MRO: Method Order Resolution 
# Nos ayuda conocer la gerarquia (El orden) de las clases heredadas
# Se ejecuta primero la clases hijas hasta la clase padre object
print(Cuadrado.mro())