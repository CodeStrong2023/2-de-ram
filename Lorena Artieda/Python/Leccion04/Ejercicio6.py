#Ejercicio 6: Tabla de multiplicar
#Hacer un programa que pida un numero por teclado y guarde
#en unalista su tabla de multiplicar hasta el 10.

numero = int(input("Digite un número: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} X {i} = {resultado}")