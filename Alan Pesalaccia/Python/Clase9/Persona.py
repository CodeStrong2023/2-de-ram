class Persona:
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs):  # Método inicial de la clase llamado Init Dunder
        self.nombre = nombre  # self hace referencia a los elementos dentro de la clase como el this
        self.apellido = apellido
        self._dni = dni
        self.edad = edad
        self.args = args
        self.kwargs = kwargs


    def mostrar_detalle(self):
        print(
            f"Nombre: {self.nombre}, Apellido: {self.apellido}, DNI: {self._dni} , Edad: {self.edad}, Dirección: {self.args}, Datos Imporatnes: {self.kwargs}")



persona1 = Persona("Juan", "Perez", 3423332, 34)  # Instanciamos la clase

persona2 = Persona("Julio", "Triarca", 44534354, 44)
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

# Crear un u atributo para un objeto específico
persona1.telefono = "332432"
print(f"Este es el teléfono {persona1.telefono} de {persona1.nombre}")

persona3 = Persona("Maria", "Esteves", 442223, 24, "Av. Falsa", 123, "Barrio Negro", Altura=1.55, Peso=56, Auto="Fitito")
print(persona3.mostrar_detalle())
# print(persona3._dni) esto no se puede utilizar para encapsulamiento