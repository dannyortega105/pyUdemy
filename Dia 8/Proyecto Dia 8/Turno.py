def cosmetico():
    for n in range(1, 101):
        yield f"C -{n}"

def perfume():
    for n in range(1, 101):
        yield f"P - {n}"

def farmacia():
    for n in range(1, 101):
        yield f"F - {n}"

c = cosmetico()
f = farmacia()
p = perfume()


def decora_funcion(funcion):
    print("Su turno es: ")
    if funcion == "P":
        print(next(p))
    elif funcion == "F":
        print(next(f))
    else:
        print(next(c))
    print("Pronto sera atendido")





