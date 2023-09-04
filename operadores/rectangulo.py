'''
Rectangulo
Calcular el área y perimetro de un rectangulo
el usuario debe ingrsar los valores y rescivir el resultad
'''


alto = int(input( "ingrese el alto en cm:"))
ancho = int(input("ingrese el ancho en cm:"))

area = (alto * ancho)
perimetro = (alto + ancho) * 2

print(f"El área del rectangulo es: {area}")
print(f"El perímetro del rectangulo es: {perimetro}")
