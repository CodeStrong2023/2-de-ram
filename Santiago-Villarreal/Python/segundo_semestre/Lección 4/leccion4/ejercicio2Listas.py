"""
Ejercicio 2: modificar los elementos de una lista
Llenar una lista con los números del 1 al 10, luego modificarlos
elementos de la lista multiplicandonos por un valor ingresado por el usuario
"""
lista = list(range(1,11))
print('Lista original')
for i in lista:
    print(i, end="-")
print('')
valor = int(input('Ingrese un número para multiplicar >'))
# multiplicar los elementos
for indice, i in enumerate(lista):
    lista[indice] *= valor

print(f'Lista final con los elementos multiplicados por {valor}')
for i in lista:
    print(i,end='-')
