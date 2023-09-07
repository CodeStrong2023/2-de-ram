# Una colección de tipo set es una colección sin orden y sin indices, solo tiene valore únicos por lo tanto no pueden tener duplicados

planetas = {"Marte", "Júpiter", "Venus"}

print(planetas) # Cambia de manera aelatoria

# Longitud de un set
print(len(planetas)) # 3

# Revisar si un elemento existe dentro del set
print("Marte" in planetas) # True

# Agregar un elemento a set.
planetas.add("Tierra")
print(planetas) # {'Tierra', 'Júpiter', 'Marte', 'Venus'}

planetas.add("Tierra")
# En los set no se pueden agregar elementos duplicados, al ya estar el mismo elemento no lo agrega
print(planetas) # {'Tierra', 'Júpiter', 'Marte', 'Venus'}

# Eliminar un elemento en un set, puede arrojar un erro si el elemento no existe
planetas.remove("Tierra")
print(planetas) # {'Venus', 'Marte', 'Júpiter'}

# planetas.remove("Mercurio") nos da error por que Mercurio no existe en el set

# Si queremos eliminar un elemento sin que nos de un error podemos usar discart
planetas.discard("Marte")
print(planetas) # {'Júpiter', 'Venus'}

planetas.discard("Urano")
print(planetas) # {'Júpiter', 'Venus'} No da ningún error

# Limpiar el set
planetas.clear()
print(planetas) # set()

# Eliminar el set
del planetas

# Definir un set vació
conjunto = set() 

conjunto.add("Hola")
conjunto.add(7)
conjunto.add("Nombre")
print(conjunto) # {'Nombre', 'Hola', 7}

# Operaciones en set

conjunto1 = {"Nombre", 44}

# Unir dos set
conjunto_unido = conjunto | conjunto1
print(conjunto_unido) # {'Nombre', 'Hola', 44, 7} No se suman los elementos repetidos solo se muestra uno

# Obtener los elementos en común que tienen los conjuntos
conjunto_comun = conjunto & conjunto1
print(conjunto_comun) # {'Nombre'}

# Obtener los elementos que no están en otro conjunto
conjunto_diferentes = conjunto - conjunto1 # Almacenamos los elementos de conjunto que no están en conjunto1
print(conjunto_diferentes) # {'Hola', 7}

# Obtener los elementos que no comparten entre ambos conjuntos
conjunto_no_compartidos = conjunto ^ conjunto1
print(conjunto_no_compartidos) # {44, 7, 'Hola'}

# Como saber si un conjunto pertenece a toro conjunto 
print(conjunto.issubset(conjunto1)) # False
print(conjunto.issubset(conjunto_unido)) # True Porque es una union de conjunto y conjunto1

# Como saber si un conjunto contiene otro conjunto
print(conjunto_unido.issuperset(conjunto)) # True
print(conjunto_unido.issuperset(conjunto1)) # True

# Convertir un set en inmutable
conjunto = frozenset

