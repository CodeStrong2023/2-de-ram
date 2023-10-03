# ejercicio 4: sumar numeros pares dentro de un rango

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
suma = 0

for i in range(a, b+1):
    if i % 2 == 0:
        suma += i
print("La suma de los numeros pares entre", a, "y", b, "es:", suma)

# ejercicio 5: factorial de un numero positivo

num = int(input("Ingrese un numero positivo: "))
while num < 0:
    print("El numero ingresado no es positivo")
    num = int(input("Ingrese un numero positivo: "))
factorial = 1
for i in range(1, num+1):
    factorial *= i
print("El factorial de", num, "es:", factorial)