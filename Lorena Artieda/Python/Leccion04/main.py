#Listas: conjunto de elementos

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

#del cocina
print(cocina)










