# Este es un metodo que vamos a utilizar con listas y se trata de trabajar siempre con el ultimo elemento, es decir que el ultimo elemento ingresado es el primero en salir.
#SIEMPRE TRABAJAMOS CON EL ULTIMO ELEMENTO

pila = [1, 2, 3]

# Agregar

pila.append(4)
pila.append(5)
print(pila)

# Elimianndo elementos por el final

pila.pop() # Este elemento saca justamente el ultimo elemento
print(pila)

# SACAMOS EL ULTIMO ELEMENTO Y LO GUARDAMOS EN UNA VARIABLE

elementoBorrado = pila.pop()
print(f"Sacamos el elemento {elementoBorrado}")
print(f"La pila ahora quedó así: {pila}")