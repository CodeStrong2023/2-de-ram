# insertar elemento y ordenarlos, pedir numero y agregarlos a la lista, con el 0 se sale del programa, y mostarar los numero ordenados de menor a mayor

lista = []
salir = False

while not salir:
  numero = int(input('Ingrese un numero: '))
  if numero == 0:
    salir = True
  else:
    lista.append(numero)
   
lista.sort()

print(lista)

