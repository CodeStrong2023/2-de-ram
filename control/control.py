#  if else en python

condicion = False

if condicion:
  print("condición verdadera")
else:
  print("condición falsa")
  
valor = "cadena de texto"
if valor == True:
  print("condición verdadera")
elif valor == False:
  print("condición falsa")
else:
  print("condición no booleana")
  
# sintaxis simplificada de if else    
print(("condición verdadera") if condicion else ("condición falsa"))
  
  
# numero a texto
num = int(input("escriba un nummero entre el 1 y el 3"))
numTexto = ''
if num == 1:
  numTexto = "numero uno"
elif num == 2:
  numTexto = "numero dos"
elif num == 3:
  numTexto = "numero tres"
else:
  numTexto = "numero fuera de rango"
  
print(f' El numero ingresado es: {num} - {numTexto}')
    
