group_names = ["Luis", "Ramon", "Lorena", "Gianni", "Santiago", "Santiago", "Alan"]

# Forma que se me ocurrió primero, la ventaja es que no te altera el orden aleatoriamente si es necesario
new_list = []

for name in group_names:
    if name not in new_list:
        new_list.append(name)

# Quitamos los nombres repetidos de la lista
group_names = new_list.copy()
print(group_names)  # ['Luis', 'Ramon', 'Lorena', 'Gianni', 'Santiago', 'Alan']

### Forma más corta
group_names = list(
    set(group_names))  # Primero transforma la lista a un conjunto que filtra los elementos repetidos y luego lo vuelve a transformar en una lista
print(group_names)