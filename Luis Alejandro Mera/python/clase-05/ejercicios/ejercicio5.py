
numero = int(input("Digite un número: "))

while numero < 0:
    print("Error -> El número tiene que ser positivo")
    numero = int(input("Digite un número: "))

factorial = 0

for i in range(1, numero+1):
    factorial += i
    
print(f"\nEl factorial del número {numero} positivo ingresado es: {factorial}")
    