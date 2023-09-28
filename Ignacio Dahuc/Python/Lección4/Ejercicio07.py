# Ejercicio 7: Juego adivina el número
# Realizar un juego para adivinar un número. Para ello se debe
# generar un número aleatorio entre 1 - 100, y luego ir pidiendo
# números indicando "es mayor" o "es menor" según sea mayor o menor
# con respecto a N. El proceso termina cuando el usuario acierta
# y allí se debe mostrar el número de intentos.

import random

aleatorio = random.randint(0,100) # Toma de 0 a 100 literal
contador = 0

print("\t.:Juego Adivina el número:.")

while True:
    
    numero = int(input(f"Digite un número entre 0 y 100: "))
    contador += 1
    
    if numero > aleatorio:
        print("\tNo es el número, digite un número menor")
    elif numero < aleatorio:
        print( "\tNo es el número, digite un número mayor")
    else:
        print(f"\nFELICIDADES, acabas de adivinar el número {aleatorio}")
        break # Rompe el ciclo y el bucle
    
print(f"\nNúmero de intentos: {contador}")