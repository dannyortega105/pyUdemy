"""def suma(*args):
    total = 0

    for arg in args:
        total += arg
    return total

print(suma(5,6,6,500))"""

#Ejercicio 1

"""def suma_cuadrados(*args):
    total = 0
    for arg in args:
        total += (arg **2)
    return total

print(suma_cuadrados(1,2,6))"""
##Ejercicio 2
def suma_absolutos(*args):
    total = 0
    for arg in args:
        if arg < 0:
            total += (arg * -1)
        else:
            total += arg
    return total

print(suma_absolutos(1,4,-1))

#Ejercicio 3

"""def numeros_personas(nombre,*args):
    suma_numeros = 0
    suma_numeros = sum(args)
    print(f"{nombre}, la suma de tus numeros es {suma_numeros}")

print(numeros_personas("Danny",1,2,5,6))"""

