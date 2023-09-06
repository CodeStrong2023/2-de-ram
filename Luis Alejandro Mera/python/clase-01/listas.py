
# Listas

lista_numeros = [1,2,3,4,5]
lista_nombres = ["Luis", "Jose", "Maria", "Pedro"]

print(lista_nombres)

# Mostrar de manera individual

print(lista_nombres[0]) # Luis 

# Mostrar en rongo, el número final del rango indica que imprime hasta el número de posición anteriror 

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

# Eliminar un elemetno de la lista 
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


