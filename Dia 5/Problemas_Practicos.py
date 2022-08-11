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

#Ejercicio 2
"""def ejercicio2 (palabra):
    lista = list(set(palabra))
    lista.sort()
    return lista
print(ejercicio2('danny'))
"""

#Ejercicio 3

"""def validar(*args):

    contadore = 0

    for num in args:

        if contadore + 1 == len(args):
            return False
        elif args[contadore] == 0 and args[contadore + 1] == 0:
            return True
        else:
            contadore += 1

    return False

print(validar(5,8,0,3,2,0,6,4,3,6,8,1,2,9,0))"""

#Ejercicio 4

def contar_primos(num):
    primos = [2]
    itereacion = 3

    if num < 2:
        return 0

    while itereacion <= num:

        for n in range(3, itereacion, 2):

            if itereacion % n == 0:
                itereacion += 2
                break
        else:
            primos.append(itereacion)
            itereacion += 2

    print(primos)
    return  len(primos)

print(contar_primos(50))
