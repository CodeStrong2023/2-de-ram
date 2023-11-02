
lista = []
salir = False

while not salir:
    numero = int(input("Digite un número: "))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)

lista.sort() # La lista está ordenada

print(f"\nLista ordenada: \n{lista}")

