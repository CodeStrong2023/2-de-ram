class Persona:
    def __init__(self, nombre, apellido, edad):  # Método inicial de la clase llamado Init Dunder
        self.nombre = nombre  # self hace referencia a los elementos dentro del la clase como el this
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}")


persona1 = Persona("Juan", "Perez", 34)  # Instanciamos la clase

print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona("Julio", "Triarca", 44)
print(f"Nombre: {persona2.nombre}, Apellido: {persona2.apellido}, Edad: {persona2.edad}")
# Tarea
print(f"Nombre: {persona1.nombre}, Apellido: {persona1.apellido}, Edad: {persona1.edad}")

# Modificar los atributos de un objeto
persona1.nombre = "Esteban"
persona1.apellido = "Flores"
persona1.edad = 20
print(f"Nombre: {persona1.nombre}, Apellido: {persona1.apellido}, Edad: {persona1.edad}")

# Accedemos al los métodos de la clase
print("---------- Accediendo al método mostrar_detalle() ------------")
persona1.mostrar_detalle()
persona2.mostrar_detalle()
