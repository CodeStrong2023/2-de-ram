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

