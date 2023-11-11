class Aritmetica:
    """
    El nombre de este tipo de comentario es: DocString

    Está calse va a realizar algunas operaciones matemáticas
    """

    def __init__(self, operando_a, operando_b):
        self.operando_a = operando_a
        self.operando_b = operando_b
        # Método para sumar
    def sumar(self):
        return self.operando_a + self.operando_b

    def restar(self):
        return self.operando_a - self.operando_b

    def multiplicar(self):
        return self.operando_a * self.operando_b

    def dividir(self):
        return self.operando_a / self.operando_b


aritmetica1 = Aritmetica(7, 9) #Le pasamos los argumentos para los operando
print(f"La suma de los números es: {aritmetica1.sumar()}")
print(f"La resta de los números es: {aritmetica1.restar()}")
print(f"La multiplicación de los números es: {aritmetica1.multiplicar()}")
print(f"La división de los números es: {aritmetica1.dividir():.2f}")