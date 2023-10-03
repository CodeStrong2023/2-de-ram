# modificar elemento de una lista, llenar una lista con los numeroes del 1 al 10 y modificar los elementos multipdolos por un valor ingresado por el usuario

lista = list(range(1, 11))
print("lista original")

for i in lista:
  print(i, end='-')
  
valor = int(input('\nIngrese un valor: '))

for indice, i in enumerate(lista):
  lista[indice] *= valor
  
print(f'lista modificada por el valor {valor}')
for i in lista:
  print(i, end='-')