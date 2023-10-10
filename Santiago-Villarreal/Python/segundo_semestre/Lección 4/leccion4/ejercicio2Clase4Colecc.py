# Ejercicio 2: operaciones de conjuntos con listas
# escriba un programa que tenga 2 lista y que a continuacion
# cree las siguientes listas (en las que no debe haber repetición)
# 1 lista de palabras que aparecen en las listas
# 2 Lista de palabras que aparecen en la primera lista pero no en la segunda
# 3 lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 lista de palabras que aparecen en ambas lista

lista1 = [2,3,4,5,23,6,4,6,7,12]
lista2 = [4,3,2,1,6,8,9,15,23]

conj1 = set(lista1)
conj2 = set(lista2)

union = list(conj1 | conj2)
solo = list(conj1 - conj2)
solo1 = list(conj2 - conj1)
inters = list(conj1 & conj2)

print(f'Lista de palabras que aparecen en las listas: {union}')
print(f'Lista de palabras que aparecen en la primera lista pero no en la segunda: {solo}')
print(f'Lista de palabras que aparecen en la segunda lista pero no en la primera: {solo1}')
print(f'Lista de palabras que aparecen en ambas listas: {inters}')


