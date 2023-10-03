# Ejercisio 2: Operaciones de conjuntos con listas
# Escriba un programa que tenga 2 listas 
# A continuacion cree las siguientes listas (en las que no deben haber repeticion)
# 1- lista de palabras que aparece en las listas
# 2- lista de palabra que aparecen en la primer lista, pero no en la segunda
# 3- lista de palabras que aparecen en la segunda lista, pero no en la tercera
# 4- lista de palabras que aparecen en ambas listas

list1 = [1, 3, 5, 5, 3, "Ramon", 9, "River", 10]
list2 = [1, 9, "Argentina", 0, 7, "Somos Campeones", 10, 3]

# Eliminar elementos repetidos 

conjunto1 = set(list1)
conjunto2 = set(list2)

# Unificamos ambas listas

listaUnificada = list(conjunto1 | conjunto2)
solo1 = list(conjunto1 - conjunto2)
solo2 = list(conjunto2 - conjunto1)
ambas = list(conjunto1 & conjunto2)

print(f"Lista de palabras que aparecen sin repetirse: {listaUnificada}")
print(f"Lista de palabras que aparecen en la primer lista: {solo1}")
print(f"Lista de palabras que aparecen en la segunda lista: {solo2}")
print(f"Lista de palabras que coinciden en ambas lista: {ambas}")