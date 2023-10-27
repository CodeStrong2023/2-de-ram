#Listas: conjunto de elementos
#Colecciones en python

#Las listas es lo que se conoce en otros lengujaes como arreglos o vectores

nombres=['Natalia', 'Ariel', 'Osvaldo', 'Liliana']
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[-1])
print(nombres[-2])

print(nombres[0:2])
print(nombres[ :3])
print(nombres[1: ])
#Modificamos un valor
nombres[0]="Naty"
nombres[3]= "Lily"
print(nombres)
#Iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print("No hay mas elementos en la lista")
#Preguntamos cuantos elementos tiene
print(len(nombres))#Le pasamos como parametro la lista

#Agregamso un elemento
nombres.append(("Marcelo"))
nombres.append([1,2,3])
nombres.append((True))
nombres.append(10.45)
nombres.append([4,5])
nombres.append(7)
print(nombres)

#Insertar un elemento en un indice especifico
nombres.insert(1, "Alberto")
nombres.insert(3,"Debora")
print(nombres)
#Eliminamos un elemento
nombres.remove("Alberto")
print(nombres)
#Eliminar el ultimo elemento de la lista
nombres.pop()
print(nombres)
#Eliminar un elemento especifico
del nombres[2]
print(nombres)
#Eliminar, borrar o limpiar todos los elementos
#nombres.clear()
print(nombres)

#TUPLAS
#Definimos una tupla
cocina= ('cuchara','cuchillo','tenedor')
print(len(cocina))

#Acceder a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[-1])

#Acceder a un rango
print(cocina[0:2])

#Ejemplo
verduras = ('papa',) #Cuando le ponemos una (coma) apsa a ser una tupla sino es un string

#Recorremos un elemento de la tupla
for cocinar in cocina:
    print(cocinar, end= ' ')#Usamos end = para eliminar saltos de linea

cocinaLista = list(cocina)
cocinaLista[0]='plato'
cocina= tuple(cocinaLista)
print('\n', cocina)

#del cocina / Para eliminar una tupla
print(cocina)

#TIPO SET(o conjunto)
#Un elemento de tipo set es un elemento sin orden que no mantiene ningun indice
planetas= {'Marte', 'Júpiter','Venus' }
print(len(planetas))

#Revisar si un elemento existe dentro de set
print('Martes' in planetas)

#Agregar un elemento
planetas.add('Tierra')#Add es una funcion
print(planetas)
#Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Júpiter')
print(planetas)
planetas.discard('tierra')
print(planetas)

#Limpiar set
planetas.clear()
print(planetas)

#Eliminar set
del planetas
#print(planetas)

#'Maradona' :10 UN DICCIONARIO ESTA COMPUESTO POR DOS ELEMENTOS
#UNA LLAVE Y UN VALOR
#dict(key,value)

diccionario={
    'IDE': "Integrated Development Environment",
    'POO': 'Programacion Orientada a Objetos',
    'SABD':'Sistema de administracion de Base de Datos'
}

print(diccionario)

#Verificar la cantidad de elementos de ldiccionario
print(len(diccionario))
print(diccionario)

#Acceder a un diccionario con la llave
print(diccionario['IDE'])

#Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

#Modificamos elementos
diccionario['IDE']= "Entorno de desarrollo integrado"
print(diccionario)

#Como recorrer los elementos
for termino in diccionario:
    print(termino)

#Necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino,valor)

#Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

#Comprobar la existencia de algun elemento
print('IDE' in diccionario)#Devuelve un booleano

#Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

#Eliminar un elementp
diccionario.pop('SABD')
print(diccionario)

#Vaciar un diccionario
diccionario.clear()
print(diccionario)

#Eliminar diccionario
del diccionario

#Concatenamos Listas
lista1= [1,2,3]
lista2=[4,5,6]
lista3= lista1+lista2
print(lista3)

lista3.extend([7,8,9,1])
print(lista3)

print(lista3.index(5))#Fncion para ubicar en que indice esta el valor ingresado
#Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1))

#Para poner al reves la lista
lista3.reverse()
print(lista3)

#Para que una lista se multiplique utilizando sus elementos
lista = [1,2,3] * 2
print(lista3)

#Metodos de ordenamiento
lista3.sort()
print(lista3)
lista3.sort(reverse=True)
print(lista3)

#Repaso tuplas

tupla= (4,'Hola',6.78,[1,2,78], 4, 'Hola')
print(tupla)
print(4 in tupla)#Accion Booleanda





















