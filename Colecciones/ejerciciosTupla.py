# tupla = (13 ,1, 8, 3, 2, 5, 8)
# crear una lista que solo incluya los numer menores a 5 de la tupla

tupla = (13 ,1, 8, 3, 2, 5, 8)
print(tupla)
lista = []

for num in tupla:
  if num < 5:
    lista.append(num)

print(lista)