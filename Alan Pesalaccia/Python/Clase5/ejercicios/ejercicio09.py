
frase = input("Ingrese una frase: ")
frase_final = frase.replace(" ", "")
cantidad_caracteres = len(frase_final)

print(f"\nFrase original: {frase}")
print(f"\nFrase sin espacios: {frase_final}")
print(f"\nN° de caracteres de la frase es: {cantidad_caracteres}")