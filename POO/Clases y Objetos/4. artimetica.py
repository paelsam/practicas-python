class Aritmetica: # Siempre la clase debe tener un nombre en mayuscula
    """
    Clase Arimetica para realizar las operaciones de sumar, restar, etc.
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return f"Suma: {self.operandoA + self.operandoB}"

    def restar(self):
        return f"Resta: {self.operandoA - self.operandoB}"

    def multiplicacion(self):
        return f"Multiplicacion: {self.operandoA * self.operandoB}"

    def division(self):
        return self.operandoA / self.operandoB

aritmetica = Aritmetica(5,3)
print(aritmetica.sumar())
print(aritmetica.restar())
print(aritmetica.multiplicacion())
# Para definir cuantos decimales queremos que se muestren
# Podemos hacer esto: :.$f Por ejemplo: :.2f
# Solo funciona en f strings
print(f"Division: {aritmetica.division():.2f}")



