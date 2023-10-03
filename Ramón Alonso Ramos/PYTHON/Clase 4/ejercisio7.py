# Ejercisio: insertar elementos y ordenarlos
# Pedir numeros y meterlos en una lista.
# Cuando el usuario introduzca un numero 0, nuestro programa dejaría de insertar
# Por último, mostrar los números ordenados de menor a mayor.

lista = []
salir = False
while not salir:
    numero = int(input("Digite un numero: "))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
print(lista)

lista.sort() # La lista esta ordenada con el operador .sort
print(f"\nLista Ordenada: \n{lista}")