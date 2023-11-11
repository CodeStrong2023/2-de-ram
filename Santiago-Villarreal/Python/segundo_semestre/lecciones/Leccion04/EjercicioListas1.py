#Ejercicio 1: llenar una lista
#Llenar una lista con los numeros de 1 al 50, luego mostrar lalista
#con el bucle for, los elementos deben mostrarse de la
#siguiente manera: 1-2-3-4-...-50

lista= list(range(1,51))
for i in lista:
    print(i, end='-')
    