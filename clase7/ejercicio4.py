""" Ejecrcicio 4 
hacer un programa que cuando el usuario indique su edad, imprima en que eapa de su vida se encuentra
0 a 9 = La infancia es increible y bella
10 a 19 = Tienes muchos cambios, mucho que estudiar
20 a 29 = Amor y comienza el trabajo

"""

edad = int(input("Ingrese su edad"))

if 0 <= edad < 10:
  print("La infancia es increible y bella")
elif 10 <= edad <= 19:
  print("Tienes muchos cambios, mucho que estudiar")
elif 20 <= edad <= 29:
  print("Amor y comienza el trabajo")
elif 30 <= edad <= 65:
  print("estress, mucho que estudiar, poco dinero")
elif 66 <= edad <= 100:
  print("Despacio, difrute")
else:
  print("edad fuera de rago")