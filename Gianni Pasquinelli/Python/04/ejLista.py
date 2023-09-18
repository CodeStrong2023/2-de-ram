# eliminar elementos duplicados de una lista

#craer una lista con elementos duplicados
lista = [1,2,3,4,'text',5,6,'texto',7,8,9,'text',10,1,2,3,4,5]
print(lista) #imprimir la lista
conjunto = set(lista) #convertir la lista en un conjunto
print(conjunto) #imprimir el conjunto

lista = list(conjunto) #convertir el conjunto en una lista  
print(lista) #imprimir la lista sin elementos duplicados

# solucion 2, en una sola linea
lista2 = [1,2,3,4,'text',5,6,'texto',7,8,9,'text',10,1,2,3,4,5]
lista2 = list(set(lista2)) #convertir la lista en un conjunto y luego en una lista
print(lista2) #imprimir la lista sin elementos duplicados


