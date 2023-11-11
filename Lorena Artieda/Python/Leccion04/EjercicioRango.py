#Ejercicio 1: Iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3
#Ejemplo de ejecucion: 0,3,6,9

for numero in range(0, 11, 3):
    print(numero)

#Ejercicio 2: crear un rango de numeros de 2 a 6 e imprimelos
#Ejemplo de ejecucion: 2,3,4,5,6

for numero in range(2, 7):  # Esto creará un rango de números desde 2 hasta 6 (incluyendo el 2 pero excluyendo el 7).
    print(numero)  # Imprime cada número en el rango.

'''
Sintaxis de range(inicio<opcional>, fin<requerido>, incremento<opcional>)

Ejercicio 3: crear un rango de 3 a 10 pero con un incremento de 2 en 2,
en lugar de 1 en 1 Ejemplo de ejecucion 3,5,7,9
'''
for numero in range(3, 11, 2):
    print(numero)




