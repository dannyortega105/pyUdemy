from random import *

numero_aleatorio = randint(1,100)
intentos = 8
numero = 0

print("BIENVENIDO AL JUEGO 'ADIVINA EL NUMERO' \n")
name = input("Escribe tu nombre: ")
print(f"{name}, pense un numero entre 1 y 100, debes adivinar cual es)\n")

while intentos >0:
    numero = int(input("Cual crees que es el numero? "))
    intentos -= 1
    if numero not in(range(1,101)):
        print(f"Eligiste un numero que este en el rango permitido, te quedan {intentos} intentos")
        continue
    elif numero < numero_aleatorio:
        print(f"Elegiste un numero menor al correcto, te quedan {intentos} intentos")
        continue
    elif numero > numero_aleatorio:
        print(f"Elegiste un numero mayor al correcto, te quedan {intentos} intentos")
        continue
    elif numero == numero_aleatorio:
        if intentos == 1:
            print(f"Felicidades {name} ganaste, te quedo {intentos} intento")
        else:
            print(f"Felicidades {name} ganaste, te quedo {intentos} intentos")
        break
if numero != numero_aleatorio:
    print(f"Perdiste, te quedaste sin intentos, el numero ganador es {numero_aleatorio}")






