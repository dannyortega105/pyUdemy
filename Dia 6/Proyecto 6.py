import os
from pathlib import Path
from os import system

ruta = Path(Path.home(), "Recetas")

def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1

    return contador

def inicio():
    system('cls')
    print(' ' * 5 + "BIENVENIDO AL ADMINISTRADOR DE RECETAS")
    print(" " * 50)
    print(f"La receta se encuentra en la siguiente ruta: {ruta}")
    print(f"Total recetas: {contar_recetas(ruta)}")

    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Elige una opcion: ")
        print('''
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoria nueva
        [4] - Eliminar receta
        [5] - Eliminar categoria
        [6] - Salir del programa''')
        eleccion_menu = input()
    return int(eleccion_menu)

def mostrar_categoria(ruta):
    print("Categorias:")
    ruta = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1

    return lista_categorias

def elegir_categoria(lista):
    eleccion_correcta = 'x'

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input("\nElije una categoria: ")
    return lista[int(eleccion_correcta) - 1]

def mostrar_recetas(ruta):
    print("Recetas:")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador += 1

    return lista_recetas

def elegir_recetas(lista):
    eleccion_receta = 'x'

    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range (1, len(lista) + 1):
        eleccion_receta = input("\nElije una receta:")

    return lista[int(eleccion_receta) - 1]

def leer_receta(receta):
    print(Path.read_text(receta))

def crear_receta(ruta):
    exist = False

    while not exist:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + '.txt'
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            exist = True
        else:
            print("Lo siento esta receta ya existe")

def crear_categoria(ruta):
    exist = False

    while not exist:
        print("Escribe el nombre de tu categoria: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu nueva categoria {nombre_categoria} ha sido creada")
            exist = True
        else:
            print("Lo siento esta categoria ya existe")

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada")

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"La categoria {categoria.name} ha sido eliminada")

def volver_inicio():
    eleccion_regresare = 'x'

    while eleccion_regresare.lower() != 'v':
        eleccion_regresare = input("\nPresione v para volver al menu: ")
# Mostrar menu inicio

finalizar_programa = False

while not finalizar_programa:
    menu = inicio()
    if menu == 1:
        mis_categorias = mostrar_categoria(ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print("no hay recetas en esta categoría.")
        else:
            mi_receta = elegir_recetas(mis_recetas)
            leer_receta(mi_receta)
        mi_receta = elegir_recetas(mis_recetas)
        leer_receta(mi_receta)
        volver_inicio()

    elif menu == 2:
        mis_categorias = mostrar_categoria(ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()

    elif menu == 3:
        crear_categoria(ruta)
        volver_inicio()

    elif menu == 4:
        mis_categorias = mostrar_categoria(ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_recetas(mis_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()

    elif menu == 5:
        mis_categorias = mostrar_categoria(ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()

    elif menu == 6:
        finalizar_programa = True

