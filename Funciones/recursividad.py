# Es una funcion que se llame a si misma
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)

# numero = 3
# resultado = factorial(numero)
# print(f"Factorial de {numero}: {resultado}")



# Haciendo una cuenta Regresiva:

def cuentaRegresiva(numero):
    if numero > 0:
        print(numero)
        cuentaRegresiva(numero-1)

cuentaRegresiva(10)