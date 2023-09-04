
""" Dadas la horas trabajadas por 5 personas y la tarifa de pago,calcular el salario y la suma de todos los salarios 
"""
horas = 0
empleado = 1
sueldosTotales = 0
horas = 0

while empleado <= 5:
  print("Empleado ", empleado)
  horas = int(input("Cuantas horas trabajo: "))
  salario = int(input("Cuanto es su salario por hora: "))
  sueldo = salario * horas
  sueldosTotales += sueldo
  empleado += 1
  
  
print(f'La suma de todos los sueldos es: {sueldosTotales}')