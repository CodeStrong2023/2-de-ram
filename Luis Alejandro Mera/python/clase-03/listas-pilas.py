
# Pilas usando listas

lista = [1, 2, 3]

# Agregar elementos a una pila por el final
lista.append(4)
lista.append(5)
print(lista) # [1, 2, 3, 4, 5]

# Quitar elementos a una pila por el final 
lista.pop()
print(lista) # [1, 2, 3, 4] 

# Almacenar elemento eliminado en una variable
elemento_eliminado = lista.pop()
print(lista) # [1, 2, 3]
print(elemento_eliminado) # 4


