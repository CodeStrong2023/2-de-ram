# conversor de temperaturas. crear una funcion que convierta de grados celsius a fahrenheit

def celsius_fahrenhiet(celsius):
  fahrenheit = celsius * 9/5 + 32
  return fahrenheit

def fahrenheit_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * 5/9
  return celsius

celsius = float(input('Ingresa los grados celsius: '))
fahrenheit = celsius_fahrenhiet(celsius)
print(f'Los grados fahrenheit son: {fahrenheit}')


fahrenheit = float(input('Ingresa los grados fahrenheit: '))
celsius = fahrenheit_celsius(fahrenheit)
print(f'Los grados celsius son: {celsius}')