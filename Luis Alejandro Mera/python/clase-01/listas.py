
# Listas

lista_numeros = [1,2,3,4,5]
lista_nombres = ["Luis", "Jose", "Maria", "Pedro"]

print(lista_nombres)

# Mostrar de manera individual

print(lista_nombres[0]) # Luis 

# Mostrar en rongo, el número final del rango indica que imprime hasta el número de posición anterior 

print(lista_numeros[1:3]) # [2, 3]
print(lista_numeros[0:3]) # [1, 2, 3]
print(lista_numeros[0:]) # [1, 2, 3, 4, 5]
print(lista_numeros[:4]) # [1, 2, 3, 4]

# Modificar el valor de una lista 

lista_nombres[3] = "Ana"
print(lista_nombres) # ['Luis', 'Jose', 'Maria', 'Ana']

# Agregar un elemento al final del array 
lista_nombres.append("Eduardo") 
print(lista_nombres) # ['Luis', 'Jose', 'Maria', 'Ana', 'Eduardo']

# Eliminar un elemento de la lista 
lista_nombres.remove("Ana")
print(lista_nombres) # ['Luis', 'Jose', 'Maria', 'Eduardo']

# Insertar un elemento en una determinada posición
lista_nombres.insert(1,"Ana")
print(lista_nombres) # ['Luis', 'Ana', 'Jose', 'Maria', 'Eduardo']

# Eliminar el último elemento de la lista
lista_nombres.pop()
print(lista_nombres) # ['Luis', 'Ana', 'Jose', 'Maria']

# Eliminar todos los elementos de una lista
lista_nombres.clear()
print(lista_nombres) # []

# Concatenar listas
lista1 = [1, 2, 3]
lista2 = [4, 5 , 6]
lista_concatenada = lista1 + lista2
print(lista_concatenada) # [1, 2, 3, 4, 5, 6]

# Extender elementos de una lista con el método extend()
lista_concatenada.extend([7, 8, 9])
print(lista_concatenada) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Saber que posición se encuentra un elemento con el método index()
print(lista_concatenada.index(5)) # 4

# Saber cuantos valores repetidos tiene una lista con el método count()
lista_repetidos = [1, 2, 2, 3, 5, 7, 3, 2, 33, 21, 3, 5, 7]
print(lista_repetidos.count(5)) # 2
print(lista_repetidos.count(3)) # 3

# Invertir el orden de una lista con el método reverse()
lista_concatenada.reverse()
print(lista_concatenada) # [9, 8, 7, 6, 5, 4, 3, 2, 1]

# Multiplicar los elementos de una lista para que se repitan la cantidad de veces que indicamos
lista_multiplicada = [1, 2, 3] * 2
print(lista_multiplicada) # [1, 2, 3, 1, 2, 3]

# Métodos de ordenamientos

# Ordenar los elementos de manera ascendente con el método sort()
lista_concatenada.sort()
print(lista_concatenada) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Ordenar los elementos de manera descendente con el método sort(reverse=True)
lista_concatenada.sort(reverse=True)
print(lista_concatenada) # [9, 8, 7, 6, 5, 4, 3, 2, 1]







