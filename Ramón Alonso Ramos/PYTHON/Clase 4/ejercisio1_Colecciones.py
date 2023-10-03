# Ejercisio1 1: eliminar duplicados de una lista

# Creamos una lista
lista0 = [1, 2, 3, 3, 5, "Ramon", 5, 6.4, 7, 8 ,10, "Ramon", 12, 12, 3, 5, 6, 7]
print(lista0)

# convertimos una lista a conjunto de tipo set, ya que estos no pueden contener elemetos repetidos
conjunto = set(lista0) 
print(conjunto)

# convertimos el conjunto de tipo set a lista
lista = list(conjunto)
print(lista)


# Una variable a la resolucion anterior acortada es la siguiente

lista0 = list(set(lista0))



