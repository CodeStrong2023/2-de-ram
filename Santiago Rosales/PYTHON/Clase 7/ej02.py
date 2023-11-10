# funcion con * arg para multiplicar. multiplicar los valores

def multiplicar(*args):
    resultado = 1
    for i in args:
        resultado *= i
    return resultado
  
print(multiplicar(1,2,3,4,5,6,7,8,9,10))


def listarTerminos(**kwargs): # kwargs es clave valor
    for llave, valor in kwargs.items():
        print(f'{llave}: {valor}')
        
listarTerminos(IDE = 'PyCharm', Lenguaje = 'Python', Version = '3.8.5')


def desplegar_nombres(nombres):
    for nombre in nombres:
        print(nombre)
        
nombres2 = ['Juan', 'Karla', 'Guillermo']
desplegar_nombres(nombres2)
# desplegar_nombres(10) # error porque no es iterable
desplegar_nombres((10, 9, 8, 7, 6, 5, 4, 3, 2, 1)) # si es iterable porque es una tupla
desplegar_nombres((88,)) #recordar que la coma es importante para que sea una tupla
desplegar_nombres([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) # si es iterable porque es una lista 

#  funciones recursivas

# caso base y caso recursivo
def factorial(numero):
    if numero == 1: # caso base
        return 1
    else: 
        return numero * factorial(numero - 1) # caso recursivo
  
resultado = factorial(5) # 5 * 4 * 3 * 2 * 1 = 120
print(resultado)
numero_factorial = int(input('Ingresa un numero: '))   
resultado = factorial(numero_factorial)
print(resultado)