# diccionario = {'clave':'valor'}
# diccionario = {'clave':'valor', 'clave':'valor'}
# el dicc

diccionario = {'nombre':'Carlos', 'edad':22, 'cursos':['Python','Django','JavaScript']}

print(diccionario)  # {'nombre': 'Carlos', 'edad': 22, 'cursos': ['Python', 'Django', 'JavaScript']}
print(len(diccionario))

print(diccionario['nombre'])  # Carlos

print(diccionario.get('nombre'))  # Carlos  
print(diccionario.get('nombree'))  # None

diccionario['nombre'] = 'Juan' # Modificando un valor
print(diccionario)


# Iterando un diccionario
for termino in diccionario:
    print(termino)  # nombre, edad, cursos  

for termino, valor in diccionario.items(): # items() devuelve clave y valor
    print(termino, valor)  # nombre Carlos, edad 22, cursos ['Python', 'Django', 'JavaScript']
    
for termino in diccionario.keys(): # keys() devuelve las claves
    print(termino)  # nombre, edad, cursos
    
for valor in diccionario.values(): # values() devuelve los valores
  print(valor)  # Carlos, 22, ['Python', 'Django', 'JavaScript']
  
# Comprobar existencia de un elemento
print('nombre' in diccionario)  # True
print('nombree' in diccionario)  # False



# Agregar un nuevo elemento
diccionario['direccion'] = 'Calle 13'
print(diccionario)  # {'nombre': 'Carlos', 'edad': 22, 'cursos': ['Python', 'Django', 'JavaScript'], 'direccion': 'Calle 13'} 

# Remover un elemento
diccionario.pop('edad')
print(diccionario)  # {'nombre': 'Carlos', 'cursos': ['Python', 'Django', 'JavaScript'], 'direccion': 'Calle 13'}

# vaciar el diccionario
diccionario.clear()
print(diccionario)  # {}

del diccionario