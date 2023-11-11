
class Vehiculo:
    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._color = color
    @property
    def ruedas(self):
        return self._ruedas
    @ruedas.setter
    def ruedas(self, ruedas):
        self._ruedas = ruedas
    def __str__(self):
        return f'Vehiculo [color: {self._color}, ruedas: {self._ruedas}]'

class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self._velocidad = velocidad

    @property
    def velocidad(self):
        return self._velocidad
    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad
    def __str__(self):
        return f'Auto [color: {self._color}, ruedas: {self._ruedas}, velocidad: {self._velocidad}]'

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self._tipo = tipo
    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo
    def __str__(self):
        return f'Bicicleta [color: {self._color}, ruedas: {self._ruedas}, tipo: {self._tipo}]'



vehiculo1 = Vehiculo('azul', 4)
print(vehiculo1)

auto1 = Auto('rojo', 4, 120)
print(auto1)

bicicleta1 = Bicicleta('verde', 2, 'urbana')
print(bicicleta1)
