
# Las tuplas a diferencias de las listas son inmutables

cocina = ("cuchara", "cuchillo", "tenedor")

print(cocina) # ('cuchara', 'cuchillo', 'tenedor')

print(len(cocina)) # 3

# Acceder a un elemneto 
print(cocina[0]) # cuchara
print(cocina[-1]) # temedor

# Acceder a un reango
print(cocina[0:2]) # ('cuchara', 'cuchillo')

# Recorrer elementos de la tupla 
for cocinar in cocina: 
    print(cocinar)

# Convertir de tupla a lista
cocina_lista = list(cocina)

print(cocina_lista)

# Converitr una lista a tupla
cocina_tupla = tuple(cocina_lista)
print(cocina_tupla)

# Eliminar una tupla 

# del cocina