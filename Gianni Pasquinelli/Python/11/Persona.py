class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __str__(self):
        return f'Persona [nombre: {self._nombre}, edad: {self._edad}]'

class Empleado(Persona): # Hereda de Persona (clase padre) 
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo
    @property
    def sueldo(self):
        return self._sueldo
    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo
    def __str__(self):
        return f'Empleado [nombre: {self._nombre}, edad: {self._edad}, sueldo: {self._sueldo}]'




empleado1 = Empleado('Astor', 28, 50000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)

empleado2 = Empleado('Belén', 30, 60000)
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)

empleado2.nombre = 'María Belén'
empleado2.edad = 31
empleado2.sueldo = 70000

print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)