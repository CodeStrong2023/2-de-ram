# Ejercicio funciones: Calcular impuestos

def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total


pago_sin_impuesto = float(input("Ingrese el pago sin impuestos: "))
impuesto = float(input("Ingrese el impuesto a aplicar: "))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)

print(f"El pago con impuesto es: {pago_con_impuesto}")