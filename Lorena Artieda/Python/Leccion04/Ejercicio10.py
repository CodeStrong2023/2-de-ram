#Ejercicio 10: no repetir caracteres
#Hacer un programa que pida una cadena por teclado, luego
#meter los caracteres en una lista sin repetir caracteres

cadena = input("Ingrese por favor una cadena de texto: ")
lista = []
for caracter in cadena:
    lista.append(caracter)

nueva_lista = list(set(lista))

print(nueva_lista)