import math

# Ejercicio 1: Iterar un rango de 0 a 10 e imprimir números divisibles entre 3

print("Rango de 0 a 10 con numeros divisibles entre 3")
for i in range(11):
    if i % 3 == 0:
        print(i)

# Ejercicio 2: Crear un rango de numeros de 2 a 6 e imprimirlos

print("Rango de 2 a 6")
for i in range(5):
    print(i+2)

# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)
# crear una lista que solo incluya los números menos a 5 e imprimir de 1, 3, 5
lista = []
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)

# Ejercicio de matematicas
# para sacar la raiz cuadrada de un numero positivo
numero = int(input('digite un numero positivo >'))
while numero < 0:
    print('Error -> deberia ser un numero positivo')
    numero = int(input('digite un numero positivo >'))
print(f'\nSu raiz cuadrada es: {math.sqrt(numero):2f}')
