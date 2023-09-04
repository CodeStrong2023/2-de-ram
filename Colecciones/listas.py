# Comienzo segundo semestre 14/8 2023


nombres = ['Gianni', 'Belén', 'Astro', 'Milan']
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[-1])
print(nombres[-2])

print(nombres[0:2])

print(nombres[:3])
print(nombres[1:])

nombres[2] = 'Astor'
print(nombres)  

for nombre in nombres:
    print(nombre)
else:
    print('No existen más nombres en la lista')
    

print(len(nombres))

nombres.append('Nina')
print(len(nombres))
print(nombres)

nombres.insert(1, 'Ana')
print(nombres)

nombres.remove('Ana')
print(nombres)

nombres.pop()
print(nombres)

del nombres[0]  
print(nombres)

nombres.clear()
print(nombres)

del nombres
print(nombres)
