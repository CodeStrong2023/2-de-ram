# ejercicio 09 mostrar una frase sin espacios y contar su longitud

frase = input("Ingrese una frase: ")
frase2 = " "

for i in frase:
    if i != " ":
        frase2 += i
frase = frase2
print(frase)
print("La longitud de la frase es:", len(frase))