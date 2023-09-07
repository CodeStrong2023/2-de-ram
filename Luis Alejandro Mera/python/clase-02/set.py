# Una colección de tipo set es una colección sin orden y sin indices

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



