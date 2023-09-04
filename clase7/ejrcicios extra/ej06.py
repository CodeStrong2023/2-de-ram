""" Ingresar n enteros, visualizar la suma de los numeros pares de la lista
cuantos pares existen y caul es el promedio de los numeros impares"""

CantidadDeElementos = int(input("Cuantos elementos vamo a utilizar: "))

sumaPares = 0
totalPares = 0
sumaImpares = 0
totalImpares = 0
promedioImpares = 0
contador = 0

while contador < CantidadDeElementos:
  numero = int(input("Ingrese un numero: "))
  if numero % 2 == 0:
    sumaPares += numero
    totalPares += 1
  else:
    sumaImpares += numero
    totalImpares += 1
  contador += 1

print(f'Ingreso un total de {totalPares} numero pares, que sumados dan {sumaPares}')

promedioImpares = sumaImpares / totalImpares
print(f'los número impares ingrsados tienen un promedio de {promedioImpares}')