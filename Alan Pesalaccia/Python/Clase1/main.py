# lista = Ariel , Liliana, Natalia, Osvaldo

nombres = ['Naty','Osvaldo','Lily','Ariel']
print(nombres)
print(nombres[2])
print(nombres[-1]) # muestra el ultimo dato
print(nombres[0:2]) # muestra el indice 0, 1 pero no el 2
print(nombres[ :3]) # indices a mostrar 0, 1, 2
print(nombres[1: ]) # desde el indice hasta el final
# modificando valores
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)
# Iterar una lista
for nombre in nombres: #nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

# preguntamos cuantos elementos tiene
print(len(nombres))
# insertar un elemento
nombres.append('Marcelo')
print(nombres)
# insertar un elemento en un indice
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)
# eliminamos un elemento
nombres.remove('Alberto')
print(nombres)
# eliminar el ultimo elemento
nombres.pop()
print(nombres)
# eliminar un indice especifico
del nombres[2]
print(nombres)
# eliminar borrar o limpiar todos los elementos de la lista
nombres.clear()
print(nombres)
# eliminar la lista
del nombres
#print(nombres)

# Definimos una tupla
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))
# acceder a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[0])
# mostrar de manera inversa
print(cocina[-1])

#acceder a un rango
print(cocina[0:2])
# ejemplo
verduras = ('papa',) # una tupla necesita aunque sea un elemento la coma

# Recorremos los elementos de la tupla
for cocinar in cocina:
    print(cocinar, end=' ')

cocinaLista = list(cocina)
cocinaLista[0] = 'plato'
cocina = tuple(cocinaLista)
print(cocina)



