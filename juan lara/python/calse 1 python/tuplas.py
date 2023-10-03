# La gran diferencia entre listas y tuplas es que las primeras son mutables y las segunda no, SON INMUTABLES.abs
# En python se considera a las Listas como colectores
# En las tuplas no se usan [] sino que se usan () y es muy importante que luego del elemento tiene que haber una , 

cocina = ("Cuchillo", "Cuchara", "Tenedor")
print(cocina)

# Como saber el largo o la cantidad de elementos que tiene una tupla

comedor = ("Sillon", "Silla", "Mesa")
print(len(comedor))

# Accediendo a uno o varios elementos
print(comedor[0])
print(comedor[0:3])

# Recorrer los elementos de la tupla: lo vamos a hacer con un ciclo for

for utensillos in cocina:
    print(utensillos)

# Cambiar una tupla no es una buena práctica, per se puede hacer.

cocinaLista = list(cocina)
cocinaLista[0] = "plato"
cocina = tuple(cocinaLista)
print(cocina)

# Lo unico que si se puede es eliminar una tupla

#del cocina
