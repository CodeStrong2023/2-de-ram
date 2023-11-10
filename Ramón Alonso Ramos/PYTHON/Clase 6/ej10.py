# ejercicio 10. no repetir caracteres, pedir una cadena y mostrarla sin repetir caracteres

cadena = input("Introduce una cadena: ")
lista = []
for i in cadena:
    if i not in lista: # si el caracter no esta en la lista 
        lista.append(i) # lo añadimos
print("".join(lista)) # mostramos la lista como una cadena

print(f'lista sin repetir caranteres {lista}')