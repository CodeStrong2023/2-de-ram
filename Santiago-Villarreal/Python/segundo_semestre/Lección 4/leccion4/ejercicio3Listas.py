"""
Ejercicio 3: Insertar elementos y ordenarlos
Pedir numeros y meterlos en una lista cuando el usuario introduzca un
numero 0, nuestro programa dejara de insertar
Por ultimo, mostrar los numeros de menor a mayor
"""
lista = []
salir = False
while not salir:
    numero = int(input('inserte un número >'))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort()  # la lista se ordena con esta funcion
print(f'Lista ordenada: {lista}')
