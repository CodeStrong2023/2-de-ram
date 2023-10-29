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

#Repaso de set o conjunto
#Para definir un conjunto
conjunto= set() #Unica manera de inicializarlo vacio
conjunto1 = {'bye',}
conjunto.add(7)
conjunto.add('Hola')
print(conjunto1)
conjunto1.add(9)
print(conjunto1)

print(3 not in conjunto1) #Preguntamos si el numero 3 no esta en el conjunto
print(conjunto1==conjunto)

#Operaciones con conjuntos
conjunto3= conjunto | conjunto1
print(conjunto3)
conjunto3 = conjunto & conjunto1 # Elementos en comun
print(conjunto3)
conjunto3 = conjunto1 - conjunto
print(conjunto3)

conjunto3 = conjunto ^ conjunto1 #Elementos q no comparten los conjuntos
print(conjunto3)

conjunto3 = conjunto | conjunto1
print(conjunto.issubset(conjunto3))#Aqui preguntamos si un conjunto es un subconjunto dentro de otro


print(conjunto3.issuperset(conjunto1))
print(conjunto3.issuperset(conjunto))
print(conjunto.issuperset(conjunto1))

#Como saber si ambos conjuntos son disconexos. es si no comparten elementos
print((conjunto1.isdisjoint(conjunto)))#No hay cosas en comun

#Convertir un conjunto totalmente en inmutable
conjunto1= frozenset

#Repaso de diccionarios

diccionarioNuevo = {'Azul':'Blue','Rojo':'Red','Verde':'Green','Negro':'Black'}
print(diccionarioNuevo)

#Como eliminar
del(diccionarioNuevo['Azul'])
#Los diccionarios pueden almacenar difrentes tipos de datos
diccionario2 ={'Ariel':{'Edad': 40, 'Altura': 1.83},'Osvaldo':[45,1.85], 'Natalia': [35, 1.67]}
print(diccionario2)

seleccionArgentina={
    10 :{'Nombre': 'Lione Messi', 'Edad': 35 ,'Altura': 1.70, 'Precio': '50 millones', 'Posicion': 'Extremo izquierdo'},
    11 :{'Nombre': 'Angel Di Maria', 'Edad': 34 ,'Altura': 1.80, 'Precio': '12 millones', 'Posicion': 'Extremo derecho'},
    24 :{'Nombre': 'Paulo Dybala', 'Edad': 28 ,'Altura': 1.77, 'Precio': '35 millones', 'Posicion': 'Medio campo'},
    19 :{'Nombre': 'Nicolas Otamendo', 'Edad': 34 ,'Altura': 1.83, 'Precio': '3.5 millones', 'Posicion': 'Extremo'},
     1 :{'Nombre': 'Franco Armani', 'Edad': 35 ,'Altura': 1.89, 'Precio': '3.5 millones', 'Posicion': 'Arqueroo'}
}

for llave, valor in seleccionArgentina.items():
    print(llave,valor)

#Como tarea agregar por lo menos 4 jugadores mas al diccionario seleccionArgentina
print('Tenemos cargados en el diccionario la cantidad de jugadores: ', end= ' ')
print(len(seleccionArgentina))

#Pilas usando listas
pila=[1,2,3]

#Agregamos elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

#Sacando elementos por el final
elentoBorrado = pila.pop()
print(f'La pila ahora quedo asi: {pila}')

#Colas con listas
#Estructura de datos de tipo fifo(first input/ first output)
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']
cola.append('Natalia')
cola.append('Jose')
print(cola)

#Sacamos elementos de la cola
seRetira= cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)
seRetira= cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)
seRetira= cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)
seRetira= cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)
seRetira= cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)


























