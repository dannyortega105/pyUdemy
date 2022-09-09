class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " Dice Muu")

class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " Dice bee")

vaca1 = Vaca('Marta')
oveja1 = Oveja('Lupita')

def animal_habla(animal):
    animal.hablar()

animal_habla(oveja1)