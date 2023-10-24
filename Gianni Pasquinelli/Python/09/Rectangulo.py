class Rectangulo:
  """ debe tener 2 atributos: base y altura, y los métodos area y perimetro."""
  
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura
    
  def area(self):
    return self.base * self.altura
  
  def perimetro(self):
    return 2 * (self.base + self.altura)
  
base = int(input('Ingrese la base: '))
altura = int(input('Ingrese la altura: '))

rectangulo1 = Rectangulo(base, altura)
print('El área del rectángulo es: ', rectangulo1.area())