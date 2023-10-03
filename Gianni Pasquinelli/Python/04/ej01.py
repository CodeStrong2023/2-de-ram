# llenar una lista con los numeroes del 1 al 50 y mostrarla con el for

lista = []

i = 1
while i <= 50:
  lista.append(i)
  i += 1
  
for i in lista:
  print(i, end='-')
  
  
lista2 = list(range(1, 51)) # mismo resultado que el while