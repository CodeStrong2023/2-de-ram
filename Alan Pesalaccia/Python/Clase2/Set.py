# Tipo set
planetas = {'Marte', 'Jupiter', 'Venus'}
print(len(planetas)) #usamos la funcion len que significa largo
#revisar si uun elemento existe dentro del set
print('Marte' in planetas)
# agregar un elemento
planetas.add('Tierra')
print(planetas)
#eliminar elementos
planetas.remove('Marte')
print(planetas)
planetas.discard('tierra')
print(planetas)

#limpiar set
planetas.clear()
print(planetas)

#eliminar set
del planetas
