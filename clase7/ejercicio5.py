""" Ejercicio 5
crear un sistema de calificaciones.
ingresar un valor del 0 a 10
si ingreso 9 o 10 imprimimos A
si ingreso 8 o 9 imprimimos B
si ingreso 7 o <8 imprimimos C
si ingreso 6 o <7 imprimimos D
si ingreso 0 o <6 imprimimos F
"""

nota = int(input("ingrese su nota"))

if 9<=nota<=10:
  print("A")
elif nota == 8:
  print("B")
elif nota == 7:
  print("C")
elif nota == 6:
  print("D")
elif 0<=nota<=5:
  print("F")
else:
  print("Valor de nota incorrecto")