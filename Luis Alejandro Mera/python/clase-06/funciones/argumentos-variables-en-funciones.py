
def listar_nombres(*nombres): # con el * indicamos que es un número indefinido de argumentos que se pueden enviar
    for nombre in nombres:
        print(nombre)


listar_nombres("Juan", "Tito", "Helga", "Tronco")

print("Separo las dos funciones")

listar_nombres("Juan", "Tito", "Helga", "Tronco")
# En la clase está mal explicado, los argumentos no se añaden solo se imprimen de manera continua 
