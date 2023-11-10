class Cubo:
  """ clase cubo con atributos ancho, alto y profundidad """
  def __init__(self, ancho, alto, profundidad):
    self.ancho = ancho
    self.alto = alto
    self.profundidad = profundidad
    
  def volumen(self):
    return self.ancho * self.alto * self.profundidad
  
ancho = int(input('Ingrese el ancho: '))
alto = int(input('Ingrese el alto: '))
profundidad = int(input('Ingrese la profundidad: '))
  
cubo1 = Cubo(ancho, alto, profundidad)
print('El volumen del cubo es: ', cubo1.volumen())