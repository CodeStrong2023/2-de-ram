# Las listas se consideran en otros lenguajes como arreglos o vectores
# En python se considera a las Listas como colectores
# Ademas una lista puede tener diferentes tipos de datos, como cadenas de texto (string), numeros enteros (int), numeros decimales (float) y valores true or false (booleano)

nombres = ["Ramon","Gregorio","Silvia","Eduardo"]
# Podemos recorrer todos los valores de la variable
print(nombres)

# Podemos imprimir un valor en concreto
print(nombres[0])
print(nombres[1])

# Podemos recorrer desde un valor hacia otro sin que sea necesario mencionarlos a todos, simplemente con :
print(nombres[0:4])

# Si no le ponemos nignun valor al primero se cosnidera 0
print(nombres[ :2])

# Si no le ponemos nignun valor al segundo se considera que va hasta el final
print(nombres[1:])

# Iterar una lista: 
for nombre in nombres: 
    print(nombres)
else:
    print("se acabaron los elementos de la lista")

# Modificar un valor
nombres[2] = "Calderon"
print(nombres)

# Eliminar el ultimo elemento
nombres.pop()
print(nombres)

# Eliminar un índice en específico
del nombres[2] #del signfica delate
print(nombres)

# Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)