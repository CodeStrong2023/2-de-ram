#  calculadora de impuestos. crear una func para el total de un pago con impuestos


def calcular_total(pago_sin_impuestos, impuesto):
  pago_total = pago_sin_impuestos + pago_sin_impuestos * (impuesto/100)
  return pago_total



pago_sin_impuestos = float(input('Ingresa el pago sin impuestos: '))
impuesto = float(input('Ingresa el impuesto: '))

pago_sin_impuestos = calcular_total(pago_sin_impuestos, impuesto)

print(f'El pago total es: {pago_sin_impuestos}')