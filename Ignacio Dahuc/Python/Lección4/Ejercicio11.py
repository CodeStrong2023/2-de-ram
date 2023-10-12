# Ejercicio 11: Agenda telefonica
# Hacer un programa que simule una agenda de contactos. Crear un
# diccionario donde la clave sea el nombre del usuario y el valor
# sea el telefono, el programa tendrá el siguiente menú de opciones:
#       1. Nuevo contacto
#       2. Borrar contacto
#       3. Ver contactos existentes
#       4. Salir

agenda = {
    "Juan": 425639
}

while True:
    print(".:AGENDA DE CONTACTOS:.")
    print("OPCIONES")
    print("1 - NUEVO CONTACTO")
    print("2 - BORRAR CONTACTO")
    print("3 - VER CONTACTOS EXISTENTES")
    print("4 - SALIR")

    opcion = int(input("SELECCIONE UNA OPCIÓN: "))

    if opcion == 1:
        nombre = input("Ingrese el nombre del nuevo contacto: ")
        telefono = int(input("Ingrese el telefono del nuevo contacto: "))
        if nombre not in agenda:
            agenda[nombre] = telefono
            print("Contacto agregado exitosamente")
        else:
            print("Este nombre de contacto ya existe")

    elif opcion == 2:
        nombre = input("Cual es el nombre del contacto que desea borrar: ")
        if nombre in agenda:
            del(agenda[nombre])
            print("Se ha eliminado el contacto requerido")
        else:
            print("Este contacto no existe en la agenda")

    elif opcion == 3:
        print("\nAGENDA DE CONTACTOS")
        for clave, valor in agenda.items():
            print(f"NOMBRE: {clave}, TELEFONO: {valor}")

    elif opcion == 4:
        print("\nSALIENDO")
        break
    else:
        print("Se equivoco de opción de menú")
    print()
