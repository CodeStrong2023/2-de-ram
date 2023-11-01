#Ejercicio 8: Menu interactivo - Cajero automatico
#Hacer un programa que simule un cajero automatico con un saldo
#inicial de 1000 y tendra el siguiente menu de opciones:
#                1. Ingresar dinero en la cuenta
#                2. Retirar dinero de la cuenta
#                3. Mostrar dinero disponible
#                4. Salir

saldo = 1000


while True:
    print(
        "\nMenú de opciones:\n1. Ingresar dinero en la cuenta\n2. Retirar dinero de la cuenta\n3. Mostrar dinero disponible\n4. Salir")
    opcion = int(input("Digite una opcion de menu: "))
    if (opcion < 1 or opcion > 4):
        print("\nIngrese una opción correcta")
    elif opcion == 1:
        dinero = float(input("Ingrese la cantidad de dinero a depositar: "))
        saldo+= dinero
        print(f"\nSe ingreso ${dinero} a su cuenta")
    elif opcion == 2:
        dinero = float(input("Ingrese la cantidad de dinero a retirar: "))
        saldo -= dinero
        print(f"\nSe retiro ${dinero} de su cuenta")
    elif opcion == 3:
        print(f"\nEl dinero disponible en su cuenta es: {saldo}")
    elif opcion == 4:
        salir = False

print("\nMuchas gracias por utilizar nuestros servicios")