def calcular_total(pago_sin_impuesto, impuesto):
    return pago_sin_impuesto + pago_sin_impuesto * (impuesto / 100)

pago_sin_impuesto = float(input("Ingresa pago: "))
impuesto = float(input("Ingresa impuesto: "))
print(calcular_total(pago_sin_impuesto, impuesto))

