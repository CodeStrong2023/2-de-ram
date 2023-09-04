# clase 4 operadores


operandoA = 8
operandoB = 5
suma = operandoA + operandoB
print('la suma es: ', suma)
print(f'El resulta de la suma es: {suma}')

resta = operandoA - operandoB
print(f'La resta es: {resta}')

multiplicacion = operandoA * operandoB
print(f'La multiplicación es: {multiplicacion}')

division = operandoA / operandoB
print(f'La division es: {division}')
division = operandoA // operandoB #? con el doble // nos da el valor del entero solamente
print(f'La division es: {division}')

modulo = operandoA % operandoB
print(f'El resto de la division es: {modulo}')

exponente = operandoA ** operandoB
print(f'La potencia es: {exponente}')


#* operadores de asignación

variable1 = 10
print(variable1)

#reasiganr valores
variable1 = variable1 + 1
print(variable1)

variable1 += 1
print(variable1)
variable1 -= 2
print(variable1)
variable1 *= 3
print(variable1)
variable1 //= 2
print(variable1)

# EN STRINGS + realiza concatenación y * repeticin del string
saludo1 = "hola "
saludo2 = "mundo"
concat = saludo1 + saludo2
print(concat)
print(concat * 4)

y = 4
x = 2
resultado = y == x
print(resultado)
distinto = y != x
print(distinto)
mayor = y > x
print(mayor)
menor = y < x
print(menor)





