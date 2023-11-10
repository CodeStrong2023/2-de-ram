class Persona: 
  def __init__(self, nombre, apellido, edad): # constructor, self es como el this de java, pero se pone como parametro
    self.nombre = nombre 
    self.apellido = apellido
    self.edad = edad
    
  def mostrar_detalle(self): # metodo
    print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


print(type(Persona)) 

persona1 = Persona("Gianni", "Pasquinelli", 20) # instanciar un objeto
print(type(persona1)) # tipo de dato de persona1
print(persona1.nombre) # acceder a un atributo de persona1
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona("Juan", "Perez", 30)
print(f'Nombre: {persona2.nombre}, Apellido: {persona2.apellido}, Edad: {persona2.edad}')

persona1.edad = 43 # modificar un atributo
print(persona1.edad)


# metodos, son funciones dentro de una clase

persona1.mostrar_detalle() # llamar a un metodo
persona2.mostrar_detalle()
