#Ejercicio 7: juego adivina el numero
#Realizar un juego para adivinar un numero. Para ello se debe
#generar un numero aleatorio entre 1 y 100 y luego ir pidinedo
#numeros inidicando "es mayor " o "es menor" segun sea mayor o menor
#con respecto a N. El proceso termina cuando el usuario acierta
#y alli se debe mostrar el numero de intentos.

import random

numero_elegido = int(input("Digite un número para adivinar: "))
numero_aleatorio = random.randint(1, 100)
intentos = 0

while numero_aleatorio != numero_elegido:
    if (numero_elegido > numero_aleatorio):
        print("El número elegido es más alto")
    else:
        print("El número elegido es más bajo")

    intentos += 1
    numero_elegido = int(input("Digite un número para adivinar: "))

print(f"\nFelicitaciones adivinaste el número {numero_aleatorio} en {intentos} intentos")