
import random

numero_elegido = int(input("Digite un número para adivinar: "))
numero_aleatorio = random.randint(1,100)
intentos = 0

while numero_aleatorio != numero_elegido:
    if(numero_elegido > numero_aleatorio):
        print("El número elegido es más alto")
    else: 
        print("El número elegido es más bajo")
        
    intentos += 1
    numero_elegido = int(input("Digite un número para adivinar: "))
        

print(f"\nFelicitaciones adivinaste el número {numero_aleatorio} en {intentos} intentos")