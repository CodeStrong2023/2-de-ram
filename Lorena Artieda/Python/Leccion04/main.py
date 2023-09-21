#LISTAS(mutables)
# lista = Ariel, Liliana, Natalia, Osvaldo

nombres= ['Naty', 'Osvaldo', 'Lily', 'Ariel']
print(nombres)
print(nombres[0])
print(nombres[0:2])#Solo muestra el indice 0, 1 pero no el indice 2
#ir del inicio de la lista al indice(sin incluirlo)
print(nombres[ :3])#Indices a mostrar 0, 1, 2
#Desde el indice indicado hasta el final
print(nombres[1: ])
nombres[2]='Liliana'
print( nombres)
nombres[0]= 'Natalia'
print(nombres)
for nombre in nombres:#nombre es singular la lista plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

#Preguntamos cuantos elementos tiene
print(len(nombres))#Le pasamos como parametro la lista

#Agregamos un elemento
nombres.append('Marcelo')
print(nombres)#Cola se agrega al final de la lista

#Insertar un elemento en el indice especifico
nombres.insert(0, 'Pedro')
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)

#Eliminamos un elemento de la lista
nombres.remove('Marcelo')
print(nombres)

#Eliminar el ultimo elemento de la lista(Default las, el ultimo por defecto)
nombres.pop()
print(nombres)

#Eliminar un indice especifico
del nombres[2]
print(nombres)

#Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

#Eliminar la lisa
del nombres
print(nombres)#Error


#TUPLAS (inmutables)

#Definimos una tupla
cocina=('cuchara', 'cuchillo', 'tenedor')
print(cocina)

#Largo de la tupla
print(len(cocina))

#Acceder a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[0])

#Mostrar de manera inversa
print(len(cocina[-1]))

#Como acceder a un rango
print(cocina[0:2])
#Ejemplo
verdudas=('papa')#Cadena, para ser tupla hay q poner la coma a la derecha(aunque sea un solo elemento)

#De lo contrario solo seria un tipo string

#Recorremos los elementos de la tupla

for cocinar in cocina:
    print(cocinar, end=' ')#Agrega un espacio entre elementos y elimina saltos de linea

#Error porque no se puede modificar la tupla
cocina[0]= 'plato'
print(cocina)

#Castea de tupla a lista(Aunque no es una buena practica)
cocinaLista= list(cocina)
cocinaLista[0]='plato'
cocina= tuple(cocinaLista)
print('\n', cocina)

#del cocina


















