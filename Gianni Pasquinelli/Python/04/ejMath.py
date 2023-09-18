#  ejercicio matemáticas.
#  sacar la raiz cuadrada de un numero positivo
import math

numero = int(input('ingrese un numero positivo: '))

while numero < 0:
    numero = int(input('ingrese un numero positivo: '))

print(f'la raiz cuadrada de {numero} es: {math.sqrt(numero):.2f}')