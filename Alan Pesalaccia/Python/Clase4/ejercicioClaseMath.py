# Importamos la clase math
import math

# Sacar la raíz cuadrada de un número positivo

numero = int(input("Ingrese un número positivo: "))

while numero < 0:
    print("Error debe ser un número positivo")
    numero = int(input("Ingrese un número positivo: "))

print(f"\nSu raíz cuadrada es: {math.sqrt(numero):.2f}")