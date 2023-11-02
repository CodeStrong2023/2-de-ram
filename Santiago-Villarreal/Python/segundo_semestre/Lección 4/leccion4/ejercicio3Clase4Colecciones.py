# Ejercicio 3: agregar personajes a una lista
# escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos
# nombre: aragon
# clase: guerrero
# raza: dúnadan del norte

# nombre: gandalf
# class: mago
# raza: istar

# nombre: legolas
# clase: arquero
# raza: elfo sindar

SenorDeLosAnillos = {
    'personaje1': {'nombre': 'aragon', 'clase': 'guerrero', 'raza': 'dúnadan'},
    'personaje2': {'nombre': 'gandalf', 'clase': 'mago', 'raza': 'instar'},
    'personaje3': {'nombre': 'legolas', 'clase': 'mago', 'raza': 'instar'}
}
SenorDeLosAnillos['personaje1'] = {'nombre': 'frodo', 'clase': 'espadachin', 'raza': 'hobbit'}
SenorDeLosAnillos['personaje2'] = {'nombre': 'sauron', 'clase': 'nigromante', 'raza': 'maiar'}
SenorDeLosAnillos['personaje3'] = {'nombre': 'gollum', 'clase': 'dueño del anillo', 'raza': 'hobbit corrompido'}
personajes = []
P = {'nombre': 'aragon', 'clase': 'guerrero', 'raza': 'dúnadan'}
personajes.append(P)
P = {'nombre': 'gandalf', 'clase': 'mago', 'raza': 'instar'}
personajes.append(P)
P = {'nombre': 'legolas', 'clase': 'mago', 'raza': 'instar'}
personajes.append(P)
personajes.append(SenorDeLosAnillos['personaje1'])
personajes.append(SenorDeLosAnillos['personaje2'])
personajes.append(SenorDeLosAnillos['personaje3'])
print(personajes)
