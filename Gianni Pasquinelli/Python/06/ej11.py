# ejercicio 11. simular una agenda de contactos. con un diccionario donde la clave es el nombre del contacto y el valor es el telefono del contacto. el programa tendra un menu con las siguientes opciones: 
# 1. añadir contacto
# 2. eliminar contacto
# 3. mostrar contactos
# 4. salir

agenda = {}
while True:
    print("1. Añadir contacto")
    print("2. Eliminar contacto")
    print("3. Mostrar contactos")
    print("4. Salir")
    opcion = input("Introduce una opcion: ")
    if opcion == "1":
        nombre = input("Introduce el nombre del contacto: ")
        if nombre in agenda:
            print("El contacto ya existe")
        else:
            telefono = input("Introduce el telefono del contacto: ")
            agenda[nombre] = telefono
    elif opcion == "2":
        nombre = input("Introduce el nombre del contacto: ")
        if nombre in agenda:
            del agenda[nombre]
        else:
            print("El contacto no existe")
    elif opcion == "3":
        for nombre, telefono in agenda.items():
            print(nombre, telefono)
    elif opcion == "4":
        break
    else:
        print("Opcion incorrecta")
    print()