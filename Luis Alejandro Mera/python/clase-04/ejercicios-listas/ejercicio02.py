
lista = list(range(1,11))

print("Lista original ", lista)

for i in lista:
    print(i, end="-")
    
valor = int(input("\nDigite un valor a mutiliplicar: "))

# Multiplicamos los elementos de una lista
for indice, i in enumerate(lista):
    lista[indice] *= valor

print(f"Lista final con los elementos mutiplicados por {valor}")

for i in lista:
    print(i, end="-")