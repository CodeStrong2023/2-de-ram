# python es un lenguaje orientado a objetos
a = "tipos de datos"
print(a)
print(type(a))  # string
b = 10
print(b)
print(type(b))  # int
c = 10.67
print(c)
print(type(c))  # float
d = True
print(d)
print(type(d))  # boolean

# manejo de cadenas
miGrupoFavorito = "Haken"
estiloMusical = "Prog Metal"
print("mi banda favorita es:", miGrupoFavorito, estiloMusical)

numero1 = "2"
numero2 = "8"
print(numero1 + numero2)  # concatena
print(numero1, numero2)  # concatena
print(int(numero1) + int(numero2))  # conversion de dato

#  booleanos V F
miBool = True
print(miBool)
miBool2 = 1 > 2
print(miBool2)

if miBool2:
    print("resultado verdadero")
else:
    print("el resultado es falso")


#  pedir info al usuario con input
resultado = input("ingrese un numero: ")  #  devuelve un dato tipo string
print(resultado)

#  conversion de la entrada de datos
numero = input("ingresa un numero: ")
sumar = input("ingresa otro numero")
result = int(numero) + int(sumar)
print("El resultado es: ", result)
