#Ejercicio 1: crear una funcion para sumar los valores recibidos de tipo
#numerricos, utilizando argumentos variables #args como parametro de la
#funcion y agregar como resultado la suma de todos los valores pasados
#como argumento

def sum_args(*args):
    total = 0
    for arg in args:
        total += int(arg)
    print(f"El total de la suma de argumentos es {total}")


sum_args(1,2,4,56,89,56,38,2)