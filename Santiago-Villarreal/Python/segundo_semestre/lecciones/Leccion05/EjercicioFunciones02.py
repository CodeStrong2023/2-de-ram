#Ejercicio 2: Funcion con *args para multiplicar
#Crear una funcion para multiplicar los valores recibidos
#de tipo numerico, utilizando argumentos variables *args
#como parametro de la funcion y regresar como resultado
#la multiplicacion de todos los valores pasados como argumento


def multiplicar_valores(*numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado

print(multiplicar_valores(2,4,45,56,8))