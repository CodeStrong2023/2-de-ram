import math # importamos la clase math para hacer uso de la función sqrt

# Dada la siguiente tupla 
tupla = (13, 1, 8, 3, 2, 5, 8)
# Crear una lista que solo incluya numero menores a 5
# Imprima por consola (1, 3, 2)
lista = []
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)

# Ejercisio de matematicas
# Para sacar la raiz cuadrada de un numero positivo
numero = int(input("Digite un numero positivo: "))
while numero < 0:
    print("Error -> Debería ser un numero positivo")
    numero = int(input("Diguite un numero positivo: "))
print(f"/nSu raíz cuadrada es: {math.sqrt(numero):.2f}") # el 2f se utiliza para que 