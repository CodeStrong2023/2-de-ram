# EJERICISIO 1: Llenar una lista 
# Llenar una lista con los números del 1 al 50, luego mostra la lista con el bucle for
# Los elementos deben mostrarse de la siguiente manera: 1-2-3-4-5...-50

lista = []
i = 1
while i <= 50:
    lista.append(i)
    i += 1
for i in lista:
    print(i,end='-')

# Para acortar el algoritmo podemos usar esto

lista1 = list(range(1, 51))
for i1 in lista1:
    print(i1,end='-')