# Set no tiene un orden, y no permite almacenar elementos duplicados o reptidos, pero si se puede eliminar.

# No mantiene ningun indice, es decir que el orden es completamente aleatorio.

# La coleccion de tipo set nos puede servir para filtrar datos duplicados que podamos llegar a tener en una DB por ejemplo.

clubes = {'River', 'Macnhester City', 'Barcelona'}
print(clubes)

# podemos utilizar la funcion len para determinar el largo de nuestro set

print(len(clubes))

# Revisar si un eleento existe dentro del set. El elemento debe estar exactamente igual en el set que en el test, incluyendo acentos.

print('River' in clubes)
print('Boca' in clubes)

# Agregar un elemeto con la funcion .add

clubes.add('Independiente')
print(clubes)

# Eliminar elementos, puede arrojar un error si el elemento no existe

clubes.remove('Independiente')
print(clubes)

# Existe otra funcion que también elimina un elemento y es .discard. Las diferencias que existen es que .discard no nos presenta nignun error al momento de no encontrar el elemento y nuestro programa va a continuar. 

# Limpiar el set con la función .clear
clubes.clear()
print(clubes)

# Si quereos eliminar el set colocando del
del clubes
print(clubes)