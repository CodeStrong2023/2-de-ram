#Comenzamos con funciones
# mi_funcion() #No se puede llamar antes de definir una funcion
#Definimos una funcion
def mi_funcion(): #Para identificar a la funcion utilizamos parentesis
    print("Saludos a todos los alumnos de la tecnicatura")

mi_funcion()#Estamos llamando a la funcion
mi_funcion()#Se puede llamar a la funcion N cantidad de veces

#Desempaquetando de listas o list unpacking

def show(name, lastName):
    print(name+ ' ' +lastName)
person = ["Ariel", "Betancud"]
show(person[0], person[1])#Pasamos uno por uno los datos de la lista a la funcion
show(*person)#Esto es lo mismo que lo anterior pero le pasamos todo junto
person2= ("Osvaldo" "Giordanini") #Desempaquetando a traves de una tupla
person3 = {"lastName": "Lucero", "name" : "Natalia" }
show(**person3)

numbers = [1,2,3,4,5]

for n in numbers:
    print(n)
    if n==3:
        break # La única forma que no se ejecute el else
else:
    print("Esto se termina") # Podemos poner luego que termine el recorrido for


# List comprehension o lista de comprensión

names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]

alongP = [p for p in names if p[0] == "P"] #   Esto regresa una nueva lista

print(alongP)

bottleC= [{"name":"Quilmes", "country" :"Arg"},
          {"name":"Corona", "country" :"Mex"},
          {"name":"Stella Artois", "country" :"Belgium"},]

Arg=[b for b in bottleC if b["country"]== "Arg"]
print(Arg)
print(bottleC)


# Paso de argumentos

def mi_funcion2(name, lastName):
    print(f"Nombre: {name}, Apellido: {lastName}")

mi_funcion2 ("Jorge", "Lucero")
mi_funcion2("Pedro", "Garcia")

#La palabra return en funciones
#creamos una funcion para sumar

def sumar(a,b):
    return a + b

resultado= sumar(78,22)
print(f"El resultado de la suma es: {resultado}")


# Valores por default en los parámetros

def sumar2(a = 0, b = 0): # Se le asigna el valor por default si no se le ingresa ningún argumento
    return a + b

resultado = sumar2()

print(f"Resultado de la suma: {resultado}")

#Argumentos variables en funciones

def listarNombres(*nombres): # con el * indicamos que es un número indefinido de argumentos que se pueden enviar
    for nombre in nombres:
        print(nombre)


listarNombres("Lucas", "Jose", "Claudia", "Rosa", "Maria")

print("Separo las dos funciones")

listarNombres("Marcos", "Daniel", "Marcela", "Romina", "Carlos")
