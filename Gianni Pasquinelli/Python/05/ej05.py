# ejercicio 6 tabla de multiplicar
# pedir un numero y mostrar la tabla de multiplicar de ese numero, del 1 al 10

numero = int(input("Ingrese un numero: "))
lista = []
for i in range(1, 11):
    lista.append(numero * i)
print(lista)

for indice,i in enumerate(lista):
    print(numero, "x", indice+1, "=", lista[indice])


