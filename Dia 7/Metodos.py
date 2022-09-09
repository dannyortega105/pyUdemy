class Pajaro:

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pio, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f"El pajaro a volado {metros} metros")

piolin = Pajaro('Amarillo', 'canario')

piolin.piar()
