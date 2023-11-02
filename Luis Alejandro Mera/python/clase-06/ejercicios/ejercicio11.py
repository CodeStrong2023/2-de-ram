



agenda = {}

while True:
    print("\n1 - Nuevo contacto\n2 - Borrar contacto \n3 - Ver contactos existentes \n4 - Salir")
    opcion = int(input("\nIngrese la opción desea: "))
    
    if opcion == 1: 
        nombre = input("Ingrese el nombre de contacto: ")
        telefono = input("Ingrese el teléfono de contacto: ")
        if nombre not in agenda: # Si el nombre no está en la agenda
            agenda[nombre] = telefono
            print("Contacto agregado exitosamente")
        else: 
            print("El contacto ya existe")
    elif opcion == 2:
        nombre = input("Ingrese el nombre de contacto: ")
        if nombre in agenda: 
            del (agenda[nombre])
            print("Contacto eliminado exitosamente")
        else:
            print("El contacto no existe")
    elif opcion == 3:
        print("Agenda de contactos")
        
        for clave, valor in agenda.items():
            print(f"Nombre: {clave}, Teléfono: {valor}")
    elif opcion == 4:
        print("Gracias por utilizar su agenda de contactos")
        break        
         
            
            
