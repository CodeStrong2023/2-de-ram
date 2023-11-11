class Cubo:
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def calcular_voulumen(self):
        return self.ancho * self.alto * self.profundidad

ancho_usr = int(input("Ingrese el ancho del cubo: "))
alto_usr = int(input("Ingrese el alto del cubo: "))
profundiad_usr = int(input("Ingrese la profundiad del cubo: "))

cubo1 = Cubo(ancho_usr, alto_usr, profundiad_usr)

print(f"El volumen del cubo es: {cubo1.calcular_voulumen()}")