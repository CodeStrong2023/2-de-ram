
# Funciones recursivas

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)

number_input = int(input("Ingrese un número para calcular el factorial: "))

result = factorial(number_input)

print(f"El factorial del número {number_input} es: {result}")

