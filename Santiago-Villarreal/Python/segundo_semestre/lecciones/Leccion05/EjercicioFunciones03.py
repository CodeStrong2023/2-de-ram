#Ejercicio 3: Funciones Recursivas
#Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas
#puede ser cualquier valor positivo, por ejemplo, si pasamos el valor de 5, debe imprimir:
#5
#4
#3
#2
#1
#En caso de ser el numero 3 debe imprimir:
#3
#2
#1
#Si se ingresan numeros negarivos no imprime nada

def imprimir_numeros_recursivos(numero):
    if numero >= 1:
        print(numero)
        imprimir_numeros_recursivos(numero - 1)
    elif numero == 0:
        return
    elif numero <= 0:
        print("Valor ingresado incorrecto")

number_input = int(input("Ingrese un número: "))

imprimir_numeros_recursivos(number_input)

imprimir_numeros_recursivos(1)

