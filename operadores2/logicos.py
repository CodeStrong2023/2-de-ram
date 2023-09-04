# Operadores lógicos

a = False
b = True
resultado = a and b
print(resultado)

resultado = a or b
print(resultado)

resultado = not a
print(resultado)

# valor dentro de un rango
valor = int(input("escriba un numero: "))
minimo = 0
maximo = 5
dentroRango = (valor >= minimo and valor <= maximo)
if dentroRango:
    print(f'El valor {valor} esta dentro del rango')
else:
    print(f'El valor {valor} esta fuera del rango')
    

# ejercicio or

vacaciones = False
descanso = False
if vacaciones or descanso:
    print("Puede asistir al juego")
else:
    print("Esta trabajando")

# Rango edades
edad = int(input("¿Cual es su edad?"))
veinte = edad >= 20 and edad < 30
print(veinte)
treinta = edad >= 30 and edad < 40
print(treinta)

if veinte:
    print("Estas dentro del rango de los 20\'s años")
elif treinta:
    print("Estas dentro del rango de los 30\'s años")
else:
    print("Estas fuera del rango de edad")
    

# mayor de dos numero
num1 = int(input("Digite un numero"))
num2 = int(input("Digite un numero"))
if num1 == num2:
    print("Los numerso son iguales")
elif num1 > num2:
    print("el primer numero es mayor")
else:
    print("el segundo numero es mayor")


# ejercicio tienda de libros

titulo = input("titulo del libro: ")
idLibro = int(input("ID del libro: "))
precio = float(input("precio del libro: "))
envio = input("Es envio gratuito (si/no): ")
if envio == "si":
    envio = True
elif envio == "no":
    envio = False
else:
    envio = "Error"

print(f'El Libro {titulo} numero {idLibro} cuesta ${precio}, con envio gratuito {envio}')