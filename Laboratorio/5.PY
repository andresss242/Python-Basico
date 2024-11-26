class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo_inicial=0):
        """
        Inicializa una cuenta bancaria con número de cuenta, titular y saldo inicial
        """
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto):
        """
        Realiza un depósito en la cuenta
        """
        if monto > 0:
            self.saldo += monto
            print(f"Depósito de COP{monto} realizado. Nuevo saldo: COP {self.saldo}.")
        else:
            print("El monto para depositar debe ser positivo")

    def retirar(self, monto):
        """
        Realiza un retiro de la cuenta si hay fondos suficientes
        """
        if monto > 0:
            if monto <= self.saldo:
                self.saldo -= monto
                print(f"Retiro de COP:{monto} realizado. Nuevo saldo: COP {self.saldo}.")
            else:
                print("Fondos insuficientes para realizar el retiro")
        else:
            print("El monto para retirar debe ser positivo")

    def consultar_saldo(self):
        """
        Devuelve el saldo actual de la cuenta
        """
        print(f"El saldo actual de la cuenta {self.numero_cuenta} es COP {self.saldo}.")
        return self.saldo


def mostrar_menu():
    """
    Muestra el menú de opciones para el usuario
    """
    print("\nMenú Banco")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Consultar saldo")
    print("4. Salir")


def interactuar_con_usuario(cuentas):
    """
    Permite interactuar con el usuario
    para realizar operaciones bancarias
    """
    while True:
        
        numero_cuenta = input("\nIngrese el número de cuenta: ")
        
        
        if numero_cuenta not in cuentas:
            print("Número de cuenta no encontrado. Intente nuevamente")
            continue
        
        cuenta = cuentas[numero_cuenta]
        print(f"Bienvenido, {cuenta.titular}")
        
        
        mostrar_menu()
        
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1": 
            monto = float(input("Ingrese el monto a depositar: "))
            cuenta.depositar(monto)
        elif opcion == "2": 
            monto = float(input("Ingrese el monto a retirar: "))
            cuenta.retirar(monto)
        elif opcion == "3":  
            cuenta.consultar_saldo()
        elif opcion == "4": 
            print("Gracias por usar el sistema bancario")
            break
        else:
            print("Opción no válida. Intente nuevamente")



cuentas = {
    "001": CuentaBancaria("001", "Andres Rios", 100000),
    "002": CuentaBancaria("002", "Camila Contreras", 150000),
    "003": CuentaBancaria("003", "Breyner Avila", 200000)
}


print("Bienvenido al sistema bancario")
interactuar_con_usuario(cuentas)
