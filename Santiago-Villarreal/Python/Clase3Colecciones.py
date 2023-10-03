# Repaso de set o conjunto
# Para definir un conjunto
conjunto = set()
conjunto1 = {"bye", }
conjunto.add(7)
conjunto.add("Hola")
print(conjunto)
conjunto1.add("hola")
print(conjunto1)
print(3 not in conjunto1) #devuelve valor booleano
# Igualdad de conjuntos
print(conjunto == conjunto1)
# Operaciones
conjunto2 = conjunto | conjunto1
print(conjunto2)
conjunto2 = conjunto - conjunto1 # muestra solo conjunto
print(conjunto2)
conjunto2 = conjunto1 - conjunto # muestra solo conjunto1
print(conjunto2)
conjunto2 = conjunto ^ conjunto1 # muestra los elementos que no comparten
print(conjunto2)

conjunto2 = conjunto | conjunto1
print(conjunto1.issubset(conjunto2)) # pregunta si conjunto1 es sub set de conjunto2
print(conjunto2.issubset(conjunto1))
print(conjunto2.issuperset(conjunto)) # pregunta si conjunto2 es un super set
print(conjunto.issuperset(conjunto2))

# preguntar si conjuntos presentas elementos en comun
print(conjunto.isdisjoint(conjunto1))

# convertir en inmutable un conjunto
conjunto1 = frozenset

# Repaso diccionario
diccionarioNuevo = {'azul':'blue', 'rojo':'red', 'verde':'green','amarillo':'yellow'}
# eliminar del diccionario
del(diccionarioNuevo['azul'])
print(diccionarioNuevo)

# Distintos tipos de datos
diccionario2 = {'Ariel':{'edad':40,'altura':1.83},'Osvaldo':[45,1.85], 'Natalia':[35,1.67]}
print(diccionario2)

seleccionArgentina = {
    10:{'nombre': 'Lionel Messi', 'edad':35, 'altura':1.70,'precio':'50 millones','´posicion':'Extremo derecho'},
    11:{'nombre': 'Angel Di Maria','edad':34, 'altura':1.80,'precio':'12 millones','posicion':'Extremo izquierdo'},
    24:{'nombre': 'Enzo Fernandez', 'edad':22,'altura':1.78,'precio':'120 millones','posicion':'Mediocampista'},
    9:{'nombre':'Julian Alvarez','edad':23,'altura':1.70,'precio':'50 millones','posicion':'Centrodelantero'}
}
for llave, valor in seleccionArgentina.items():
    print(llave, valor)

# pilas usando listas
pila = [1,2,3]

# agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# eliminar elementos desde el final
elementoBorrado = pila.pop()
print(f'elemento eliminado: {elementoBorrado}')
print(f'estado actual de la pila: {pila}')

# colas con listas
# estructura de datos de tipo fifo
cola = ['Ariel','Osvaldo','Liliana','Pilar']

# agregar elementos al final
cola.append('Natalia')
cola.append('Jose')
print(cola)

# eliminar elementos de la cola
seRetira = cola.pop(0)
print(f'atendido {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'atendido {seRetira}')
print(cola)
