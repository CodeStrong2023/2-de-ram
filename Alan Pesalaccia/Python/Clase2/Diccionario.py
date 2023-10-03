# 'Maradona' :10 el diccionario esta compuesto por dos elementos
# una llame y un valor

diccionario = {
    'IDE' : 'Integrated Development Environment',
    'POO' : 'Programacion Orientada a Objetos',
    'SABD' : 'Sistema de Administracion de Base de Datos'
}
#Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave
print(diccionario['IDE'])

#otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificar elementos
diccionario['IDE'] = 'Entorno de desarrollo integrado'
print(diccionario)

# Como recorrer los elementos
for termino in diccionario: # recorremos mostrando las llaves
    print(termino)
#necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino) # muestra solo las llaves

for valor in diccionario.values():
    print(valor)

# comprobar la existencia de algun elemento
print('IDE' in diccionario) # devuelve un booleano

#agregar un elemento
diccionario['PK'] = 'Primary ket'
print(diccionario)

#eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

#vaciar un diccionario
diccionario.clear()
print(diccionario)

#eliminar diccionario
del diccionario

#concatenamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1 + lista2
print(lista3)

lista3.extend([7, 8, 9, 1]) # funcion para agregar varios elementos a una lista
print(lista3)
print(lista3.insert(5)) # funcion para ubicar en que indice esta el valor ingresado

#como saber cuantos elementos repetidos hay dentro de la lista
print(lista3.count(1)) #cuenta cuantos valores iguales hay dentro de la lista

# para poner nuesta lista al reves
lista3.reverse()
print(lista3)

# para que una lista se multiplique repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)

#metodos de ordenamiento
lista3.sort() #ordena ascendentemente todos los elementos
print(lista3)
lista3.sort(reverse=True) # ordena descendentemente
print(lista3)

tupla = (4, 'hola', 6.78, [1, 2, 78], 4, 'Hola') # puede tener diferentes tipos de datos dentro
print(tupla)

