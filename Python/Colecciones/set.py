# set es una coleccion sin orden y sin indices, no permite elementos repetidos
# y los elementos no se pueden modificar, pero si agregar nuevos o eliminar

planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)
print(len(planetas))

print("Marte" in planetas)
print("Tierra" in planetas)

planetas.add("Tierra")
print(planetas)

planetas.remove("Jupiter") # Si el elemento no existe, lanza un error 
print(planetas)
planetas.discard("Tierra") # Si el elemento no existe, NO lanza un error
print(planetas)

planetas.clear()
print(planetas)

del planetas


print("--------------------------------------------------")
print()
print("Conjuntos")
print()
print()
# conjunto = set() un set es un conjunto de elementos desordenados, a los cuales no se puede acceder por indice
conjunto = set() # se crea un conjunto vacio
conjunto1 = {} # esto es un diccionario vacio, no un conjunto vacio
conjunto2 = {"bye",} # si no se pone la coma, no se considera conjunto, sino es un string
conjunto.add(7) 
conjunto.add('hola') 
conjunto2.add('hola') 
print(conjunto) 


print(3 not in conjunto) # True

print(conjunto == conjunto2) # False


conjunto3 = conjunto | conjunto2 # union de conjuntos, | es el operador de union
print(conjunto3) 

conjunto3 = conjunto & conjunto2 # interseccion de conjuntos, & es el operador de interseccion
print(conjunto3) 

conjunto3 = conjunto - conjunto2 # diferencia de conjuntos, - es el operador de diferencia
print(conjunto3)

conjunto3 = conjunto ^ conjunto2 # diferencia simetrica de conjuntos, ^ es el operador de diferencia simetrica
print(conjunto3)


# subconjunto
conjunto3 = conjunto | conjunto2
print(conjunto.issubset(conjunto3)) # True
print(conjunto3.issubset(conjunto)) # False
# issubset() devuelve True si el conjunto es subconjunto del conjunto3, sino devuelve False

print(conjunto.issuperset(conjunto3)) # False
print(conjunto3.issuperset(conjunto)) # True
# issuperset() devuelve True si el conjunto es superconjunto del conjunto3, sino devuelve False

print(conjunto.isdisjoint(conjunto3)) # False
print(conjunto.isdisjoint(conjunto2)) # True
# isdisjoint() devuelve True si el conjunto no tiene elementos en comun con el conjunto3, sino devuelve False

conjunto = frozenset # es un conjunto inmutable, no se puede modificar, ni agregar ni eliminar elementos  
 
