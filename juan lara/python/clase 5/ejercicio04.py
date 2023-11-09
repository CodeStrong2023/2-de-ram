
a = int(input("Digite de donde va a comenzar la suma: "))
b = int(input("Digite hasta donde va a comenzar la suma: "))
suma = 0
for i in range(a,b+1):
    if i % 2 == 0:
        suma += i

print(f"\nLa suma de números pares dentro del rango es: {suma}")