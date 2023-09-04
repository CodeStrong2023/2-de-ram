texto = "Hola Python"
for letra in texto:
  print(letra)
else:
  print("fin del ciclo")
  


# break
for letras in "Alemania":
  if letras == 'a':
    print(f'letra encontrada: {letras}')
    break
else:
  print("fin del ciclo")
  
  
# continue

for i in range(6):
  if i % 2 == 0:
    print(f'Valor: {i}')
    
for i in range(6):
  if i % 2 != 0:
    continue
  print(f'Valor: {i}')