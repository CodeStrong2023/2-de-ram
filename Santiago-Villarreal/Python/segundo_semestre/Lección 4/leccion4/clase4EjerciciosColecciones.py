# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuación
# elimine los elementos repetidos, por ultimo mostrar la lista

lista = [1, 2, 3, "ariel", 7, 7, 3, "alberto", 5, "ariel"]
conjunto = set(lista) # convertir lista a un conjunto de tipo set
lista = list(conjunto)
print(lista)
# lista = list(set(lista))

