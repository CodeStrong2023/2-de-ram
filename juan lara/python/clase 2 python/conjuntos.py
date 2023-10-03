# IGUALDAD ENTRE CONJUNTOS

conjunto1 = (1, 2, 3)
print(conjunto1)

conjunto2 = (4, 5, 6)
print(conjunto2)

print(conjunto1 == conjunto2)

# OPERACIONES EN CONJUNTOS

#INTEGRAR DOS O MÁS CONJUNTOS
conjunto3 = conjunto1+conjunto2
print(conjunto3)

# CONJUNTOS
conjunto1 = set() # Si queremos que nuestro conjunto comience sin nada y luego ir agregandolee valores, deemos especificar que es de tipo set y colocarle los parentesis 
conjunto1 .add(8) # Solo podemos agregar de a un valor y no podemos utilizar la propiedad .extend para poner mas de uno
conjunto1 .add(10)
conjunto2 = {'Hola', }
conjunto2 .add('Vamos RIVER')
print(conjunto2)
print(8 in (conjunto2)) # PRUEBA SI ENCUENTRA EL 8 EN EL CONJUNTO 2
print(conjunto1 == conjunto2) # PRUEBA SI CONJUNTO1 ES IGUAL AL CONJUNTO2

# OPERACIONES ENTRE CONJUNTOS

# SUMA
conjunto3 = conjunto1 | conjunto2 # SUMA DE CONJUNTOS (CONCATENACIÓN)
print(conjunto3)

# RESTA
conjunto3 = conjunto1 - conjunto2 # Asigna los valores del conjunto 1 y no los del 2
print(conjunto3)

conjunto3 = conjunto2 - conjunto1 # Asigna los valores del conjunto 2 y no los del 1
print(conjunto3)

# ELEMENTOS EN COMUN

conjunto3 = conjunto1 & conjunto2
print(conjunto3) # Devuelve que elementos tienen en comun (no tienen ninguno)

#ELEMENTOS QUE NO TIENEN EN COMUN

conjunto3 = conjunto1 ^ conjunto2 # Devuelve los elementos que no encuentre coincidencias entre los conjuntos (8, 10, Hola y Vamos River)
print(conjunto3)

# Prueba si los conjuntos mencionados están dentro del conjunto colocado con posterioridad al operador .issubset

conjunto3 = conjunto1 | conjunto2 
print(conjunto1.issubset(conjunto3))
print(conjunto1.issubset(conjunto3)) 

# CONVERTIR UN CONJUNTO EN INMUTABLE

conjunto1 = frozenset #se realiza con el operador frozenset