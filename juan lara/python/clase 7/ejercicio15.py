
# Ejercicio: Convertidor de temperaturas

# Función que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheint_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

celsius = float(input("Digite el valor de celsius: "))
resultado = celsius_fahrenheit(celsius)

print(f"{celsius} C a F -> {resultado:.2f}")

fahrenheit = float(input("Digite el valor de fahrenheit: "))
resultado = fahrenheint_celsius(fahrenheit)
print(f"{fahrenheit} F a C -> {resultado:.2f}")


