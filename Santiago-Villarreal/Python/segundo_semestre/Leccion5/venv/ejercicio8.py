"""
Ejercicio 8: Menú interactivo - Cajero automático
Hacer un programa que simule un cajero automatico con un salgo inicial de $1000
y tendrá el siguiente menú de opciones:
            1. Ingresar dinero en la cuenta
            2. Retirar dinero de la cuenta
            3. Mostrar dinero disponible
            4. Salir
"""
saldo = 1000
while True:
    print("\t.:MENU:.")
    print("1. Ingresar dinero a la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostar dinero disponible")
    print("4. Salir")
    opcion = int(input("Ingrese una opción del menu >"))
    print()
    if opcion == 1:
        extra = float(input("Cuánto dinero desea ingresar -> "))
        saldo += extra
        print(f'Dinero disponible: ${saldo}')
    elif opcion == 2:
        retirar = float(input("Cuánto dinero desea retirar -> "))
        if retirar > saldo:
            print("La cuenta no dispone de dicha cifra")
        else:
            saldo -= retirar
            print(f"Dinero disponible: ${saldo}")
    elif opcion == 3:
        print(f"Dinero disponible: ${saldo}")
    elif opcion == 4:
        print("Gracias por utilizar el cajero automático")
        break
    else:
        print("Incorrecto, ingrese un número entre las opciones")
        print()