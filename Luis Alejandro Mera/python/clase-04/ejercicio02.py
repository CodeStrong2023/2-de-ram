
lista1 = [3,24,5,32,2,3,5,2,2,4,5,52,11,1,1,1,5,5]
lista2 = [2,3,5,33,5,3,256,6,4,674,3,64,3,34,]

# Eliminar los elementos repetidos de las listas 
conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = list(conjunto1 | conjunto2)
solo1 = list(conjunto1 - conjunto2)
solo2 = list(conjunto2 - conjunto1)
interseccion = list(conjunto1 & conjunto2)

print(f"Lista de palabras que aparecen en las listas: {union}")
print(f"Lista de palabras que aparecen en la primera lista, pero no en la segunda: {solo1}")
print(f"Lista de palabras que aparecen en la segunda lista, pero no en la primera: {solo2}")
print(f"Lista de palabras que aparecen en ambas listas: {interseccion}")



