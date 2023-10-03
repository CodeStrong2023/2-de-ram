# La tarea consiste en ingresar elementos al diccionario llamado seleccionArgentina, lo elementos a ingresar deben ser como mínimo 4, estos elementos son los jugadores con su número de camiseta, nombre, apellido, edad, altura, precio y posición de juego, por supuesto ver el video anterior.

SeleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 36, 'Altura': 1.70, 'Precio': '50 MILLONES', 'Posición': 'Extremo Derecho'},
    11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 MILLONES', 'Posición': 'Extremo Izquierdo'},
    21: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 MILLONES', 'Posición': 'Media Punta'},
    19: {'Nombre': 'Nicolás Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3,5 MILLONES', 'Posición': 'Defensa Central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3,5 MILLONES', 'Posición': 'Portero'},
    9: {'Nombre': 'Julián Álvarez', 'Edad': 36, 'Altura': 1.70, 'Precio': '50 MILLONES', 'Posición': 'Delantero'},
    24: {'Nombre': 'Enzo Fernandez', 'Edad': 22, 'Altura': 1.79, 'Precio': '24 MILLONES', 'Posición': 'Mediocampista Defensivo'},
    26: {'Nombre': 'Nahuel Molina', 'Edad': 25, 'Altura': 1.75, 'Precio': '11 MILLONES', 'Posición': 'Lateral Derecho'},
    3: {'Nombre': 'Nicolás Tagliafico', 'Edad': 31, 'Altura': 1.72, 'Precio': '8MILLONES', 'Posición': 'Lateral Izquierdo'},
}

print(SeleccionArgentina)
print(SeleccionArgentina[10])
print(SeleccionArgentina.values())

for llave in SeleccionArgentina: # Para recorrer las lalves (dorsales)
    print(llave)

for  valor in SeleccionArgentina.values(): # Para recorrer las valores (caracteristicas)
    print(valor)

for llave, valor in SeleccionArgentina.items(): # Realizamos todo el recorrido con llaves y valores
    print(llave, valor)

print(len(SeleccionArgentina))

