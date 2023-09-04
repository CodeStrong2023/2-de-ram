# ejercicio 1

a = float(input("ingrese un valor para A:   "))
b = float(input("ingrese un valor para B:   "))
c = float(input("ingrese un valor para C:   "))

resultado = ((a ** 3) * (b ** 2 - 2 * a * c )) / (2 * b)
print(f' El resultado de la exprecion es: {resultado}')


# ejercicio 2
resultado = ( (3+5*8)<3 and ((-6/3*4)+2 < 2) ) or (a > b)
print(resultado)

# ejercicio 3, intercambio de variables

a = 10
b = 5
print(f'La variable a es: {a} y la variable b es: {b}')
aux = a
a = b
b = aux
print(f'La variable a es: {a} y la variable b es: {b}')

# sabia de esta opcion... así que la probe y funciono, tal vez es mas dificil de ver, pero funciona mejor ya que no agregamosuna nueva variable
[a,b] = [b,a]
print(f'La variable a es: {a} y la variable b es: {b}')


# ejercicio 4, área y longitud de un círculo

import math 
radio = float(input(" ingrese el radio del círculo:   "))
area = math.pi * (radio ** 2)
longitud = 2 * math.pi * radio
print(f'El radio {radio} del círculo, nos da que tiene un área de: {area} y una longitud de: {longitud}')





