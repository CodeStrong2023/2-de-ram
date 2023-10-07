
#Ejercicio: Funciones recursivas

def imprimir_numeros_recursivos(numero):
    if numero >= 1:
        print(numero)
        imprimir_numeros_recursivos(numero - 1)
    elif numero == 0:
        return
    elif numero <= 0:
        print("El valor ingresado incorrecto")

number_input = int(input("Ingrese un número: "))

imprimir_numeros_recursivos(number_input)
print("------------------------")
imprimir_numeros_recursivos(4)
print("------------------------")
imprimir_numeros_recursivos(0)
