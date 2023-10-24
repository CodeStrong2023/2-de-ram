"""
Ejercicio 7: juego adivina el número
Realizar un juego para adivinar un número. Para ello se generar un número
alaeatorio entre 1 - 100, y luego ir pidiendo nuúmero indicando "es mayor"
o "es menor" según sea mayor o menor con respecto a N. El proceso termina
cuando el usuario acierta y se debe mostrar el número de intentos
"""
import random
aleatorio = random.randint(0,100)
contador = 0
print("Juego adivina el número")
while True:
    numero = int(input("Ingrese un número >"))
    contador += 1
    if numero > aleatorio:
        print("Incorrecto, ingrese un número menor")
    elif numero < aleatorio:
        print("Incorrecto, ingrese un número mayor")
    else:
        print(f"Correcto! El número es {aleatorio}")
        break
print(f'El número de intentos fue {contador}')

