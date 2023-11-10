class Persona:
  def __init__ (self, nombre, apellido, edad):
    self._nombre = nombre
    self._apellido = apellido
    self._edad = edad
    
  def mostrar_detalles(self):
    print("Persona: ", self._nombre, self._apellido, self._edad)
    
  @property
  def nombre(self):
    print("Llamando metodo get nombre")
    return self._nombre
  
  @nombre.setter
  def nombre(self, nombre):
    print("Llamando metodo set nombre")
    self._nombre = nombre
    
  
  @property
  def apellido(self):
    print("Llamando metodo get apellido")
    return self._apellido
  
  @apellido.setter
  def apellido(self, apellido):
    print("Llamando metodo set apellido")
    self._apellido = apellido
    
  @property
  def edad(self):
    print("Llamando metodo get edad")
    return self._edad
  
  @edad.setter
  def edad(self, edad):
    print("Llamando metodo set edad")
    self._edad = edad
    
  def __del__(self):
    print(f'Destruyendo el objeto {self._nombre} {self._apellido}')
    
    
    
if __name__ == '__main__':
    
  persona1 = Persona("Gianni", "Pasquinelli", 43)
  print(persona1.nombre)

  persona1.nombre = "Juan"
  print(persona1.nombre)
  print(persona1.mostrar_detalles())

  # persona1.edad = 44
  # print(persona1.edad)
  # si no se define el setter, no se puede modificar el valor de la propiedad por lo que es un atributo de solo lectura


  persona2 = Persona("Maria", "Gomez", 30)
  persona2.nombre = "Juana"
  persona2.apellido = "Perez"
  persona2.edad = 31
  print(persona2.mostrar_detalles())

  persona3 = Persona("Carlos", "Lopez", 40)
  persona3.nombre = "Marcos"
  persona3.apellido = "Gomez"
  persona3.edad = 41
  print(persona3.mostrar_detalles())

  persona4 = Persona("Ana", "Gomez", 50)
  persona4.nombre = "Ania"
  persona4.apellido = "Gomes"
  persona4.edad = 12
  print(persona4.mostrar_detalles())


print(__name__)