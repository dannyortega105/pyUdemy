
"""def cambiar_letra(tipo):

    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == "may":
        return mayuscula
    elif tipo == "min":
        return minuscula

operacion = cambiar_letra("may")

operacion("palabra")"""

def decorar_saludo(funcion):

    def otra(palabra):
        print("Hola")
        funcion(palabra)
        print("adios")
    return otra


def mayuscula(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())

mayuscula_decorada = decorar_saludo(mayuscula)

mayuscula_decorada("Fede")
mayuscula("fede")