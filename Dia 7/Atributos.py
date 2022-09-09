class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro('negro', 'Guacamaya')

print(mi_pajaro.especie)

print(Pajaro.alas)