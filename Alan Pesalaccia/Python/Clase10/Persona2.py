
class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    def mostrar_detalle(self):
        print(f"Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}")

    @property # decorador que nos permite acceder al método de manera directa sin tener que ejecutar
    def nombre(self): # Método getter
        return self._nombre

    @nombre.setter
    def nombre(self, nombre): # Método setter
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, edad):
        self._edad = edad
    def __del__(self):
        print(f"Persona2: {self._nombre} {self._apellido} {self._edad} eliminada")


if __name__ == "__main__": # Esto nos permite ejecutar el código solo si estamos en el módulo principal
    persona1 = Persona2("Juan", "Perez", 32)

    print(persona1.nombre) # Gracias al decorador @property accedemos directamente al metodo getter sin tener que ejectuar
    persona1.nombre = "Julio"
    print(persona1.nombre)

    # Tarea
    persona2 = Persona2("Maria", "Esteves", 22)
    persona2.nombre = "Ana"
    persona2.apellido = "Gomez"
    persona2.edad = 33
    persona2.mostrar_detalle()

    persona3 = Persona2("Pedro", "Gonzalez", 44)
    persona3.nombre = "Esteban"
    persona3.apellido = "Flores"
    persona3.edad = 55
    persona3.mostrar_detalle()

    persona4 = Persona2("Julio", "Triarca", 44)
    persona4.nombre = "Pepe"
    persona4.apellido = "Gonzalez"
    persona4.edad = 55
    persona4.mostrar_detalle()

    print(__name__) # Esto nos muestra el nombre del módulo que estamos ejecutando

