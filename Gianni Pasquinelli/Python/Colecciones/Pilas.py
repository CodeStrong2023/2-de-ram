# pilas usando listas

pila = [1, 2, 3]
# agregando elementos a la pila, ultimo en entrar, primero en salir (LIFO)
print(pila)
pila.append(4)
pila.append(5)
print(pila)

elemBorado = pila.pop() # saca el ultimo elemento de la pila y lo devuelve
print(elemBorado)
print(pila)

# cola usando listas

cola = [10, 11, 12]
# agregando elementos a la cola, primero en entrar, primero en salir (FIFO) 
print(cola)
cola.append(13)
cola.append(14)
print(cola)

retiro = cola.pop(0) # saca el primer elemento de la cola y lo devuelve, el 0 es el indice del elemento a sacar
print(retiro)
print(cola)

