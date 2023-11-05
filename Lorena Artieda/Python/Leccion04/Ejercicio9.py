#Ejercicio 9: mostrar una frase sin espacios y contar su longitud
#Hacer un programa donde el usuario ingrese una frase, se le
#devolvera la misma frase pero sin espacios en blanco, y ademas un contador
# de cuantos caracteres tiene la frase
#Sin contar los espacios en blanco

frase = input("Ingrese una frase: ")
frase_final = frase.replace(" ", "")
cantidad_caracteres = len(frase_final)

print(f"\nFrase original: {frase}")
print(f"\nFrase sin espacios: {frase_final}")
print(f"\nN° de caracteres de la frase es: {cantidad_caracteres}")