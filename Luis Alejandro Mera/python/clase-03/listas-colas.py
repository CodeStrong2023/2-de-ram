
# Las colas son estructuras de datos de tipo fifo (first input / first output) primero en entrar y primero en salir

lista = [1,2,3]

# Agregar elementos a la cola
lista.append(4)
lista.append(5)
print(lista) # [1, 2, 3, 4, 5]

# Quitamos elementos de la cola 
primer_elemento_quitado = lista.pop(0) # quitamos el elemento de la primera posición
print(lista) # [2, 3, 4, 5]