"""def funcion():
    lista = []
    for x in range(1, 5):
        lista.append(x * 10)
    return lista

def generador():
    for x in range(1,5):
        yield x * 10

g = generador()

print(funcion())
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))"""

def generador():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

g = generador()
print(next(g))
print(next(g))
print(next(g))

