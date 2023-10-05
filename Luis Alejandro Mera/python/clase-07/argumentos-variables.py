
def listar_terminos(**terminos): 
    for key, value in terminos.items():
        print(f"{key} : {value}")
        

listar_terminos()
listar_terminos(IDE = "Integrated Develoment Enviorment", PK = "Primary Key")
listar_terminos(name = "Luis")

# Función que itere listas 

def desplegar_nombres(nombres):
    for nombre in nombres:
        print(nombre)
        

nombres = ["Juan", "Pedro", "Carlos"]

desplegar_nombres(nombres)

# Convertir los argumentos en tuplas iterables en caso de no tener un arreglo para pasar
desplegar_nombres((20,30,50,3,3))

# Convertir los argumentos en lista iterables en caso de no tener un arreglo para pasar
desplegar_nombres([20,30,50,3,3])

