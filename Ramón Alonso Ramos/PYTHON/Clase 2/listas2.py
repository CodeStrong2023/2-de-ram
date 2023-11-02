
# PARA CONCATENAR LAS LISTAS REALIZAMOS LA SUMA DE LAS MISMAS

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9]
lista4 = lista1+lista2+lista3
print(lista4)

# AGREGAR varios ELEMENTOS a una lista. con un operador .extend

lista4.extend([10, 100, 1000])
print(lista4)

# BUSCAR EL INDICE DE UN ELEMENTO .IndexError

print(lista4.index(10))

# BUSCAR VALORES REPETIDOS DENTRO DE UNA LISTA

print(lista4.count(10))

# PONER AL REVES UNA LISTA

lista4.reverse()
print(lista4)

# MULTIPLICAR LA LISTA

lista1 = [1, 2, 3]
print(lista1*2)

# METODO DE ORDENAMIENTO: siempre va a ordenar los elementos de una manera ascendente por default con el operador .sort si queremos que la ordena de manera descendente es .sort(reverse=true)

lista1.sort()
print(lista1)

lista1.sort(reverse=True)
print(lista1)