
# Desempaquetado de listas o List Unpacking

def show(name, lastName):
    print(f"{name} {lastName}")
    

person = ["Juan", "Perez"]

show(person[0], person[1])

show(*person) # Tenemos el mismo resultado, lo que hacemos es pasar todos los elementos de la lista

print(*person)

person2 = ("Jose", "Garcia") # Tupla

show(*person2)

person3 = {"lastName": "Pedro", "name": "Aguirre"} # Diccionarios

show(**person3) # Con un asterisco solo muestra las clave, con dos asteriscos muestra el valor

