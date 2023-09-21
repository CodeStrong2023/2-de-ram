'''
Sintaxis de range(inicio<opcional>), fin <requerido>, incremento<pcional>)

Ejercicio 1: Iterar un rango de 0 a 10 e imprimir numeros divisibles
entre 3
Ejemplo de ejecucion 4,5,7,9
Ejercicio 2: crear un rango de numeros de 2 a 6 e imprimelos
ejemplo de ejecucion: 2,3,4,5,6
Ejercicio 3: Crear un rango de 3 a 10 pero con incremeneto de 2 en 2 en lugar de 1 en 1
Ejemplo de ejecucion: 3,5,7,9
'''

#Ejercicio 1

for i in range(1, 10):
    if i%3==0:
        print(i)

#Ejercicio 2:

for i in range(2,7):
    print(i)

#Ejercico 3:

for i in range(3, 10,2):
    print(i)
