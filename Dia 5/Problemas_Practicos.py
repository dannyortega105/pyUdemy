"""lista = []
suma = 0

def devolver_distintos(num1, num2, num3):
    lista = [num1, num2, num3]
    lista.sort()
    suma = num1 + num2 + num3

    if suma > 15:
        return max(num1, num2, num3)
    elif suma < 10:
        return min(num1, num2, num3)
    elif suma in range(10,16):
        print(lista[1])


print(devolver_distintos(1,6,6))"""


def ejercicio2 (palabra):
    lista = list(set(palabra))
    lista.sort()
    return lista
print(ejercicio2('danny'))

