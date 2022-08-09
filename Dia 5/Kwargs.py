"""def prueba(num1, num2, *args, **kwargs):
    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")


    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

args = [100,200,300,400,500]
kwargs = {'x':'uno', 'y':'dos'}

prueba(15,50,*args, **kwargs)"""

#ejercicio1

"""def cantidad_atributos(**kwargs):
    cantidad = 0
    for kwarg in kwargs.items():
        cantidad += 1
        return cantidad

print(cantidad_atributos(x=3,y=4,g=6,u=5))"""

#Ejercicio 2

"""def lista_atributos(**kwargs):
    lista = []
    for kwarg in kwargs.values():
        lista.append(kwarg)
        return lista"""
#Ejercicio 3
def describir_persona(nombre, **kwargs):
    print(f"{nombre}")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

print(describir_persona("Danny",a="amarillo", b='blanco'))
