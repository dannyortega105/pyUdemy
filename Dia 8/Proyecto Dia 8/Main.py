import Turno as t

def preguntar():

    while True:
        print("Elige una opcion")
        print('P', 'C', 'F')
        try:
            opcion = input("Elija su opcion: ").upper()
            ["P", "F", "C"].index(opcion)
        except ValueError:
            print("Esa no es una opcion correcta")
        else:
            break

    t.decora_funcion(opcion)

def inicio():

    while True:
        preguntar()
        try:
            otro_turno = input("Quieres sacar otro turno? ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opcion valida")
        else:
            if otro_turno == "N":
                print("Gracias")
    """if opciones == 'P':
        p = t.perfume()
        t.decora_funcion(p)
        print(next(p))
    elif opciones == 'C':
        c = t.cosmetico()
        t.decora_funcion(c)
        print(next(c))
    elif opciones == 'F':
        f = t.farmacia()
        t.decora_funcion(f)
        print(next(f))
    #print(next(decorar))
"""

inicio()