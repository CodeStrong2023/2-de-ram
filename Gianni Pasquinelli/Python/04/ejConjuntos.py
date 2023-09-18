# ejercicio 2
# opercaiones de conjuntos con listas
# escribir un programa con dos listas y realizar las siguientes operaciones:
# 1 lista de palabras que aparecen en las dos listas
# 2 lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 lista de palabras que aparecen en ambas listas

# crear dos listas con palabras

lista1 = ['hola', 'mundo', 'python', 'programacion', 'programa', 'programar', 'programador', 'programadora', 'programadores', 'programadoras', 'programacion', 'Gianni', 'UTN']
lista2 = ['hola', 'mundo', 'python', 'programacion', 'programa', 'programar', 'programador', 'programadora', 'programadores', 'programadoras', 'programacion', 'hola', 'mundo','San Rafel', 'Universidad', 'python', 'programacion', 'programa', 'programar', 'programador', 'programadora', 'programadores', 'programadoras', 'programacion']

# eliminar elementos duplicados de las listas

conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = list(conjunto1 | conjunto2) # union de los dos conjuntos
solo1 = list(conjunto1 - conjunto2) # elementos que estan en el conjunto1 pero no en el conjunto2
solo2 = list(conjunto2 - conjunto1) # elementos que estan en el conjunto2 pero no en el conjunto1
interseccion = list(conjunto1 & conjunto2) # elementos que estan en ambos conjuntos

print('lista1: ', lista1)
print('lista2: ', lista2)
print('union: ', union)
print('solo1: ', solo1)
print('solo2: ', solo2)
print('interseccion: ', interseccion)
