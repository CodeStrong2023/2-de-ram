
saldo_inicial = 1000


# print("Menú de opciones:\n1 - Ingresar dinero en la cuenta\n2 - Retirar dinero de la cuenta\n3 - Mostrar dinero disponible\n4 - Salir")
# opcion = int(input("Digite el número de opción: "))
salir = True

while salir:
    print("\nMenú de opciones:\n1 - Ingresar dinero en la cuenta\n2 - Retirar dinero de la cuenta\n3 - Mostrar dinero disponible\n4 - Salir")
    opcion = int(input("Digite el número de opción: "))
    if(opcion < 1 or opcion > 4):
        print("\nIngrese una opción correcta")
    elif opcion == 1:
        dinero = float(input("Ingrese la cantidad de dinero a depositar: "))
        saldo_inicial += dinero
        print(f"\nSe ingreso ${dinero} a su cuenta")
    elif opcion == 2:
        dinero = float(input("Ingrese la cantidad de dinero a retirar: "))
        saldo_inicial -= dinero
        print(f"\nSe retiro ${dinero} de su cuenta")
    elif opcion == 3:
        print(f"\nEl dinero disponible en su cuenta es: {saldo_inicial}")
    elif opcion == 4:
        salir = False
        
print("\nMuchas gracias por usar nuestros servicios")
        
    