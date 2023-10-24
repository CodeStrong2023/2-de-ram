"""
Ejercicio 9: Mostrar una frase sin espacios y contar su longitud hacer un
programa desde el usuario ingrese una frase, se le devolvera la misma
frase  pero sin espacios en blanco, y ademas un contador de cuantos
caracteres tiene la frase (sin contar los espacios)
ejemplo: frase = vivir por siempre en paz
        frase final = vivirporsiempreenpaz
        n° de caracteres = 20
"""
frase = input("Ingrese una frase >")
frase2 = " "
for i in frase:
    if i != " ":
        frase2 += i
frase = frase2
print(f"\nfrase final: {frase}")
print(f'N° de caracteres: {len(frase)}')
