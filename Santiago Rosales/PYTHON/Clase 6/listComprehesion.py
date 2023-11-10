names = ["Gianni", "Astor", "Milan", "Belen"]
alongP = [p for p in names if p[0] == "M"]
print(alongP)

botellasC = [
  {"name": "Quilmes", "country": "Argentina"},
  {"name": "Corona", "country": "Mexico"},
  {"name": "Heineken", "country": "Holanda"},
  {"name": "Budweiser", "country": "USA"},
]

arg = [b["name"] for b in botellasC if b["country"] == "Argentina"]
print(arg)
print(botellasC)


def mi_funcion(name, lastname):
  print(f"Hello {name} {lastname}")

mi_funcion("Gianni", "Pasquinelli")
mi_funcion(lastname="Pasquinelli", name="Gianni")


def sumar(a, b):
  return a + b

print(sumar(1, 2))

def sumar2(a = 0, b = 0):
  return a + b, a - b

print(sumar2(1, 2))
print(sumar2())


def lista_nombre(*nombres):
  for nombre in nombres:
    print(nombre)
    
lista_nombre("Gianni", "Astor", "Milan", "Belen")
lista_nombre("Juan", "Pedro", "Maria", "Jose")

