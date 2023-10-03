# Diccionarios: están compuestos por dos elementos, una key y un value

usuario = {
    "id": "2",
    "name": "Luis",
    "last_name": "Mera" 
}

print(usuario) # {'id': '2', 'name': 'Luis', 'last_name': 'Mera'}

# Longitud de elementos
print(len(usuario)) # 3

# Acceder a un elemento de un diccionario
print(usuario["name"])  # Luis

# Otra forma de acceder a un elemento
print(usuario.get("last_name")) # Mera

# Modificar los elementos del diccionario
usuario["id"] = "4"
print(usuario) # {'id': '4', 'name': 'Luis', 'last_name': 'Mera'}

# Recorrer las key de un diccionario 
for key in usuario:
    print(key)
    
# Recorrer las key y valores de un diccionario con el método items()
for key, value in usuario.items():
    print(key, value)

# Otras maneras de acceder a las key de un diccionario con el método keys()
for key in usuario.keys(): 
    print(key)

# Otras maneras de acceder a los value de un diccionario con el método values()
for value in usuario.values(): 
    print(value)
    
# Comprobar la existencia de una key en un diccionario
print("id" in usuario) # True

# Agregar un elemento al diccionario
usuario["age"] = 37
print(usuario) # {'id': '4', 'name': 'Luis', 'last_name': 'Mera', 'age': 37}

# Eliminar un elemento de un diccionario 
usuario.pop("age")
print(usuario) # {'id': '4', 'name': 'Luis', 'last_name': 'Mera'}

# Vaciar un diccionario
usuario.clear()
print(usuario) # { }

# Eliminar diccionario
del usuario
