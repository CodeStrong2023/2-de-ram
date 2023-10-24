# self es equivalente al this de Java o javascript y se usa para referirse a la clase misma
# self es un parametro que se pasa implicitamente a los metodos de una clase
# self es una referencia a la instancia de la clase

class Persona:
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): # *args y **kwargs son opcionales, se llama init dunder
        self.__nombre = nombre
        self.apellido = apellido
        self._dni = dni # _dni es un atributo privado 
        self.edad = edad
        self.args = args # *args es una tupla 
        self.kwargs = kwargs # **kwargs es un diccionario

    def mostrar_detalle(self):
        print(f'la clase Persona tiene estos datos: {self.__nombre} {self.apellido} {self._dni} {self.edad},la direccion es: {self.args}, los datos importantes son: {self.kwargs} ')
    

persona1 = Persona('Gianni', 'Pasquinelli', 27879997, 42)
persona2 = Persona('Juan', 'Perez', 3333333333, 28)
persona1.mostrar_detalle()
persona2.mostrar_detalle()

persona1.telefono = '123456789' # se puede agregar un atributo a un objeto en cualquier momento
print(persona1.telefono)

persona3 = Persona('Astor', 'Piazzolla', 123581321, 71, 'teléfono', 211385321, 'Av. Corrientes', 1234, Altura=1.80, Peso=80, intrumento='bandoneón')
persona3.mostrar_detalle()
print(persona3._dni) # se puede acceder a un atributo privado desde afuera de la clase pero no es recomendable
persona3.__nombre = 'Astor' # no se puede modificar un atributo privado desde afuera de la clase

