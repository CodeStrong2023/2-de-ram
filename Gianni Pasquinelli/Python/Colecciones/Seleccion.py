seleccionArgentina = {
  10: {'Nombre': 'Lionel Messi', 'Edad': '35', 'Altura': '1.70', 'valor': '100 Millones', 'Posicion': 'Delantero'},
  11: {'Nombre': 'Angel Di Maria', 'Edad': '33', 'Altura': '1.80', 'valor': '20 Millones', 'Posicion': 'Delantero'},
  12: {'Nombre': 'Emiliano Martinez', 'Edad': '28', 'Altura': '1.90', 'valor': '20 Millones', 'Posicion': 'Arquero'},
  13: {'Nombre': 'Nahuel Molina', 'Edad': '23', 'Altura': '1.80', 'valor': '10 Millones', 'Posicion': 'Defensor'},
  8: {'Nombre': 'Marcos Acuña', 'Edad': '29', 'Altura': '1.70', 'valor': '15 Millones', 'Posicion': 'Defensor'},
  9: {'Nombre': 'Lautaro Martinez', 'Edad': '23', 'Altura': '1.80', 'valor': '80 Millones', 'Posicion': 'Delantero'},
  7: {'Nombre': 'Rodrigo De Paul', 'Edad': '27', 'Altura': '1.80', 'valor': '40 Millones', 'Posicion': 'Mediocampista'},
  6: {'Nombre': 'Giovanni Lo Celso', 'Edad': '25', 'Altura': '1.80', 'valor': '40 Millones', 'Posicion': 'Mediocampista'},
  24: {'Nombre': 'Guido Rodriguez', 'Edad': '27', 'Altura': '1.80', 'valor': '20 Millones', 'Posicion': 'Mediocampista'},
  3: {'Nombre': 'Nicolas Tagliafico', 'Edad': '28', 'Altura': '1.70', 'valor': '20 Millones', 'Posicion': 'Defensor'},
  
}

print(seleccionArgentina[10])
print(seleccionArgentina.values())

for llave in seleccionArgentina:
  print(llave)
  
for llave, valor in seleccionArgentina.items():
  print(llave, valor)
  
for jugador in seleccionArgentina.values():
  print(jugador['Nombre'])
for jugador in seleccionArgentina.values():
  print(jugador['Posicion'])
