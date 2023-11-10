class Persona: # Creamos una clase

    def __init__(self, nombre, apellido, edad): # Se lo llama método Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

persona1 = Persona('Ariel', 'Betancud', 40) # Necesitamos enviar argumentos
# print(persona1.nombre) # Tarea: Hacer el print igual que con el objeto 2
# print(persona1.apellido)
# print(persona1.edad)

print(f'El objeto 1 de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')

persona2 = Persona('Osvaldo', 'Giordanini', 45)
print(f'El objeto 2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(f'El objeto 1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona2.edad}')

# Los atributos son: caracteristicas
# Los métodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle() # La referencia en este caso se pasa de manera automatica
persona2.mostrar_detalle()

# Persona.mostrar_detalle(persona1) # Debemos pasarle una referencia para el self o dará error

# Crear un atributo para un objeto específico
persona1.telefono = "156242"
print(f"Este es el teléfono {persona1.telefono} de {persona1.nombre}")

persona3 = Persona("Juan", "Perez", 55124, 32, "Colon", 1113, "Barrio 14", Altura=1.71, Peso=63, Auto="Peugeot 206")
print(persona3.mostrar_detalle())
# print(persona3._dni) no se puede utilizar para encapsulamiento