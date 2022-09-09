class Pajaro:

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pio, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f"El pajaro a volado {metros} metros")
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(self.color)

    @classmethod
    def poner_huevos(cls, cantidad):
        print(cantidad)

piolin = Pajaro('Amarillo', 'canario')
Pajaro.poner_huevos(3)

piolin.volar(50)