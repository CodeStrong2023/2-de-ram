# ejercicio 8 menu interactivo - cajero automatico
# cajero conun saldo base de $1000 y las siguientes opciones:
# 1. ingresar dinero
# 2. retirar dinero
# 3. consultar saldo
# 4. salir

saldo = 1000
while True:
  print("MENU: ")
  print("1. Ingresar dinero")
  print("2. Retirar dinero")
  print("3. Consultar saldo")
  print("4. Salir")
  opcion = int(input("Ingrese una opcion: "))
  print()
  if opcion == 1:
    ingreso = int(input("Ingrese el monto a ingresar: "))
    saldo += ingreso
    print("El saldo actual es:", saldo)
  elif opcion == 2:
    retiro = int(input("Ingrese el monto a retirar: "))
    if retiro > saldo:
      print("El monto a retirar supera el saldo disponible")
    else:
      saldo -= retiro
      print("El saldo actual es:", saldo)
  elif opcion == 3:
    print("El saldo actual es:", saldo)
  elif opcion == 4:
    break
  else:
    print("Opcion incorrecta")
  print()
print("Gracias por utilizar el cajero automatico")
