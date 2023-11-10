
# ejercicio 7 adivinar un numero
# generar un numero aleatorio entre 1 y 100 y pedir al usuario que lo adivine indicando si el numero ingresado es mayor o menor al numero a adivinar. mostrar el numero de intentos cuando se adivine el numero

import random
aleatorio = random.randint(1, 100)
contador = 0

while True:
  numero = int(input("Ingrese un numero: "))
  contador += 1
  if numero > aleatorio:
    print("El numero ingresado es mayor al numero a adivinar")
  elif numero < aleatorio:
    print("El numero ingresado es menor al numero a adivinar")
  else:
    print("El numero ingresado es igual al numero a adivinar")
    break

print(f'El numero de intentos fue: {contador}')


