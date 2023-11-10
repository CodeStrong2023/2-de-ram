# ejercicio 3 funcion recursiva, imprimir los numeros del 5 al 1 de manera descendente 


def imprimir_numeros(numero):
    if numero >= 1:
        print(numero)
        return imprimir_numeros(numero - 1)
    elif numero == 0:
      return
    elif numero <= 0:
        print("valor no valido")
        
      
imprimir_numeros(0) 
