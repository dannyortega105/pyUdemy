
#Esto es para que agregue los valores que si cumplen con ser de 2 cibras a la lista

"""def chequear(lista):

    listas = []

    for i in lista:
        if i in range(100,1000):
            listas.append(i)
        else:
            pass
    return listas

resultado = chequear([555,66,758])
print(resultado)"""

"""lista = [2,66,88,-1]

def todos_positivos(lista):
    for i in lista:
        if i < 0:
            return False
        else:
            pass
    return True"""

lista_numeros = [3,4,66,789]

def suma_menores(lista_numeros):
    suma =0
    for i in lista_numeros:
        if i in range(1,1000):
           suma += i
        else:
            pass
    return suma
