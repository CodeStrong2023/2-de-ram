""" 
Ejercicio3
pedir al usuario que ingrese un mes del año, el valor debe ser entre 1 y 12, luego le decimos en que estacion esta
"""
mes = int(input("ingrese un mes en formato númer (1 - 12)"))

if 1 <= mes <=3:
  print("la estacion de ese mes es Verano")
elif 4 <= mes <=6:
  print("la estacion de ese mes es Otoño")
elif 7 <= mes <=9:
  print("la estacion de ese mes es invierno")
elif 10 <= mes <=12:
  print("la estacion de ese mes es Primavera")
else:
  print("Error, ingreso equivocado")