
# Función con argumentos para multiplicar

# Definimos la función para multiplicar

def multiplicar_valores(*numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado

print(multiplicar_valores(3,5,15,50,4))

