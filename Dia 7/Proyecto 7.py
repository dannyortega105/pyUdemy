class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Hola {self.nombre} {self.apellido} tu balance es {self.balance}"

    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print("Deposito aceptado")

    def retirar(self, monto_retiro):

        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("Retiro realizado")
        else:
            print("Fondos insuficientes")

def crear_cliente():
    nombre = input("Escribe tu nombre: ")
    apellido = input("Escribe tu apellido: ")
    numero_cuenta = input("Ingrese su numero de cuenta: ")
    cliente = Cliente(nombre, apellido, numero_cuenta)
    return cliente

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)

    opciones = 0
    while opciones != 'Salir':
        print("Elige una opcion")
        print('D', 'R', 'S')
        opciones = input()

        if opciones == 'D':
            monto_dep = int(input("Monto a depositar: "))
            mi_cliente.depositar(monto_dep)
        elif opciones == 'R':
            monto_ret = int(input("Monto a retirar: "))
            mi_cliente.retirar(monto_ret)
        elif opciones == 'S':
            break
        print(mi_cliente)
        print("Gracias por operar en Banco Python")

inicio()


