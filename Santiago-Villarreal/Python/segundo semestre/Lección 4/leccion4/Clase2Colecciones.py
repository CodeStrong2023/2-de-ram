# Tipo set
planetas = {'marte','jupiter','venus'}
print(len(planetas)) # funcion len de lenght = largo
print('marte' in planetas) # revisa si un elemento existe dentro del set y da una respuesta logica
# agregar un elemento
planetas.add('tierra')
print(planetas)
# Eliminar un elemento
planetas.remove('jupiter')
print(planetas)
planetas.discard('tierra')
print(planetas)
# Limpiar set o conjunto
planetas.clear()
print(planetas)
# Eliminar set o conjunto
del planetas

# Diccionario: esta compuesto por dos elementos
# Llave + valor
# dict(key,value)
diccionario = {
    'IDE':'integrated development environment',
    'POO':'Programación orientrada a objetos',
    'SABD':'Sistema de administración de base de datos',
}
print(diccionario)
print(len(diccionario))

# acceder a un elemento del diccionario
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))

# Modificar elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Recorrer diccionario
for termino in diccionario: # Recorrer mostrando solo las llaves
    print(termino)
# Funcion para recorrer el diccionario
for termino, valor in diccionario.items():
    print(termino, valor)
# Otras maneras de reccorer
for termino in diccionario.keys():
    print(termino)
for valor in diccionario.values():
    print(valor)
# Comprobar existencia de elemento
print('IDE')

# Agregar un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario

# concatenar listas
Lista1 = [1,2,3]
Lista2 = [4,5,6]
lista3 = Lista1 + Lista2
print(lista3)

# agregar varios elementos a la lista
lista3.extend([7,8,9])
print(lista3)

# Para ubicar el indice
print(lista3.index(3))

# para saber valores repetidos
print(lista3.count(1))

# lista en reversa
lista3.reverse()
print(lista3)

# Multiplicar listas
listorti = [1,2,3] * 2
print(listorti)

# Ordenar lista
lista3.sort()
print(lista3)
lista3.sort(reverse=True)
print(lista3)

#repaso tupla
tupla = (4,'hola',6.78,[1,2,78],4,'Hola')
print(tupla)

# respuesta booleana
print(4 in tupla)




