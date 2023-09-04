# Cacular el factorial de un número mayor o igual a 0
factorialDe = 0

while factorialDe <= 0:
  factorialDe = int(input("Ingrese el número a factorizar "))

print(f'Vamos a sacar el factoria de {factorialDe}')

resultado = 1

for factorial in range(1, factorialDe +1):
  resultado *= factorial
  
print(f'el factoria de {factorialDe} es {resultado}')