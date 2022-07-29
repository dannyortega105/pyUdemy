texto = input("Por favor ingresa un texto: ")
letra = []

texto = texto.lower()

letra.append(input("Ingresa la primera letra: ").lower())
letra.append(input("Ingresa la segunda letra: ").lower())
letra.append(input("Ingresa la tercera letra: ").lower())

print("\n")
print("CANTIDAD DE LETRAS: ")
cantidad_letras = texto.count(letra[0])
cantidad_letras2 = texto.count(letra[1])
cantidad_letras3 = texto.count(letra[2])

print(f"Hemos encontrado la letra '{letra[0]}' repetida {cantidad_letras} veces")
print(f"Hemos encontrado la letra '{letra[1]}' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra '{letra[2]}' repetida {cantidad_letras3} veces")

print("\n")
print("CANTIDAD DE PALABRAS: ")
palabras = texto.split()
print(f"Hemos encontra {len(palabras)} palabras en tu texto")

print("\n")
print("PRIMERA Y ULTIMA PALABRA: ")
print(f"La primera palabra del texto es '{texto[0]}' y la ultima es '{texto [-1]}'")

print("\n")
print("PALABRAS EN ORDEN INVERSO: ")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Tu texto invertido seria: '{texto_invertido}'")

print("\n")
print("BUSCANDO PALABRA PYTHON: ")
buscar_python = 'python' in texto
dic = {True:"si",False:"no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")



