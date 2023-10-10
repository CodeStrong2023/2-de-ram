# :Listas
# :Lista = Ariel, Liliana, Natalia, Osvaldo

nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
print(nombres)
print(nombres[0])
print(nombres[3])
print(nombres[-3])
print(nombres[-1])
print(nombres[0:2])  # muestra 0 y 1, no incluye 2
print(nombres[ :3])  # Indices a mostrar 0, 1, 2
print(nombres[1: ])  # muestra desde 1 al final
# :Modificación
nombres[2] = 'Liliana'
print(nombres)
# :iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

# :preguntar cuantos elementos contiene
print(len(nombres))
# :agregar un elemento
nombres.append('Marcelo')
print(nombres)
# :Insertar un elemento en un indice especifico
nombres.insert(1, 'alberto')
nombres.insert(3, 'debora')
print(nombres)
# eliminar un elemento
nombres.remove('alberto')
print(nombres)
# eleminar el ultimo elemento
nombres.pop()
print(nombres)
# eliminar un indice especifico
del nombres[2]
print(nombres)
# eliminar todos los elementos
nombres.clear()
print(nombres)

# eliminar la lista
del nombres

# definir tupla
cocina = ('cuchara','cuchillo', 'tenedor')
print(cocina)

# acceder a un elemento
print(cocina[0])
# inversa
print(cocina[-1])

# acceder a un rango
print(cocina[0:1])

# recorrer la tupla
for cocinar in cocina:
    print(cocinar, end=' ')

# para modificar la tupla
cocinaLista = list(cocina)
cocinaLista[0] = 'plato'
cocina = tuple(cocinaLista)
print(cocina)

