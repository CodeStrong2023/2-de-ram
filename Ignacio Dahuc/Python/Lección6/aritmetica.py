class Aritmetica:
  def __init__(self, a, b):
    self.a = a
    self.b = b
  
  def sumar(self):
    return self.a + self.b

  def restar(self):
    return self.a - self.b

  def multiplicar(self):
    return self.a * self.b

  def dividir(self):
    return self.a / self.b

aritmetica1 = Aritmetica(2, 4)
# print(aritmetica1.sumar())

print(f'Suma: {aritmetica1.sumar()}')
print(f'Resta: {aritmetica1.restar()}')
print(f'Multiplicacion: {aritmetica1.multiplicar()}')
print(f'Division: {aritmetica1.dividir():.2f}')