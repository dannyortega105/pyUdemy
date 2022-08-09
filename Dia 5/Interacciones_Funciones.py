from random import *

#lista inicial

"""palitos = ['-','--','---','----']

#mezclar palitos
def mezcla(lista):
    shuffle(lista)
    return lista

#pedirle intento
def probar():
    intento = ''

    while intento not in ['1', '2', '3', '4']:
        intento = input("Elige un numero del 1 al 4: ")

    return int(intento)

#comprobar intento
def chequear(lista,intento):
    if lista[intento -1] == '-':
        print("A lavar los platos")
    else:
        print("Hoy te has salvado")
    print(f"Te ha tocado {lista[intento -1]}")

#De esta manera se mezcla las funciones
palitos_mezclados = mezcla(palitos)
seleccion = probar()
chequear(palitos_mezclados,seleccion)"""


"""def lanzar_dados():
    lanzar = randint(1,7)
    lanzar2 = randint(1,7)
    return lanzar, lanzar2

sumar = 0
def evaluar_jugada(lanzar, lanzar2):
    sumar = lanzar + lanzar2
    return sumar

print(evaluar_jugada)
evaluar_jugada(lanzar_dados())"""
#Ejercicio 1
import random

"""suma = 0
def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma = dado1 + dado2
    return suma

def evaluar_jugada(suma):

    if suma <= 6:
        return f"La suma de tus dados es {suma}. Lamentable"
    elif suma > 6 and suma < 10:
        return f"La suma de tus dados es {suma}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma}. Parece una jugada ganadora"

resultado = evaluar_jugada(lanzar_dados())
print(resultado)"""

#Ejercico 2
"""lista_numeros = [1,2,15,7,2]

def reducir_lista(lista):
    lista = list(set(lista))
    lista.sort()
    lista.pop(-1)
    return lista

def promedio(lista):
    valor_medio = sum(lista) / len(lista)
    return valor_medio"""

#Ejercicio 3

moneda = ['Cara', 'Cruz']
lista_numeros = [1,5,6]

def lanzar_moneda():
    lance = choice(moneda)
    return lance

def probar_suerte(lance,lista):
    if lance == 'Cara':
        print("La lista se autodestruira")
        return []
    else:
        print("La lista fue salvada")
        return lista
    
print(probar_suerte(lanzar_moneda(),lista_numeros))







