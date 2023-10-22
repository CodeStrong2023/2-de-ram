"""
Ejercicio 4: Sumar números pares dentro de un rango
Hacer un programa para sumar números pares dentro de un rango
"""
a = int(input("Digite desde donde va a comenzar la suma >"))
b = int(input("Digite hasta que número quiere sumar >"))
suma = 0
for i in range(a,b+1):
    if i % 2 == 0:
        suma += i
print(f"La suma de números pares dentro del rango es {suma}")
