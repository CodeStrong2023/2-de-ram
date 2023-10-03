
cadena = input("Ingrese la cadena de texto: ")
lista = []
for caracter in cadena:
    lista.append(caracter)

nueva_lista = list(set(lista))

print(nueva_lista)