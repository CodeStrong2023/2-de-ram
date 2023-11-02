# Esta compuesto por dos elemetos. Una llave y un valor.

diccionario = {
    'IDE': 'Integreted Development Environment',
    'POO': 'Programacion Orientada a Objetos',
    'SABD': 'Sistema de Administración de Base De Datos'
}

print(diccionario)

# Para contar la cnatidad de elemento empleamos la propiadad len

print(len(diccionario))

# Si queremos visualizar el valor que integra esa llave, pero debe estar exactamente escrita 

print(diccionario['POO'])

#  Otra forma de obtener el valor de una llave es con la propiedad .get

print(diccionario.get('POO'))

# Recorrer los elementos para acceder solo con las llaves con el bucle for

for llave in diccionario:
    print(llave)

# Para acceder a los valores de llas llaves debemos utilizar el operador de .items().

for llave, valor in diccionario.items():
    print(llave, valor)
    
# OTRAS FORMAS DE RECORRER UN DICCIONARIO SON: para las llaves utilizar el operador .keys y para los valores el .values

# Comprobar la existencia de un elemento

print('POO' in diccionario)
print('PYTHON' in diccionario)

# MODIFICAR un elemento

diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# AGREGAR un elemento 
diccionario['PK'] = 'Primary Key'
print(diccionario)

# ELIMINAR un elemento

diccionario.pop('PK')
print(diccionario)

# VACIAR un diccionario

diccionario.clear()
print(diccionario)

# ELIMINAR un diccionario

del diccionario