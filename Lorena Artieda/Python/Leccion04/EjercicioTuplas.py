import math
#Dada ña siguiente tupla
tupla=(13,1,8,3,2,5,8)
#Crear una lista quw solo incluya los numneros menores a 5
#E imprima por consola [1,3,2]

# Inicializa una lista vacía para almacenar los números menores a 5.
lista_resultado = []

# Itera a través de la tupla y agrega los números menores a 5 a la lista_resultado.
for numero in tupla:
    if numero < 5:
        lista_resultado.append(numero)

# Imprime la lista_resultado por consola.
print(lista_resultado)

#Ejercicio de matematicas
#Para sacar la raiz cuadrada de un numero positivo
numero= int(input('Digite un numero positivo: '))
while numero<0:
    print('Error -> Deberia ser un numero positivo')
    numero= int(input('Digite un numero positivo: '))
print(f'\nSu raiz cuadrada es: {math.sqrt(numero):.2f}')
