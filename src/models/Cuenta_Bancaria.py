# clase Cuenta_Bancaria que controla el saldo de una cuenta bancaria
class Cuenta_Bancaria:
    # constructor que inicializa el nro de cuenta y el saldo
    def __init__(self, nro_cuenta, saldo=0):
        self.__nro_cuenta = nro_cuenta
        self.__saldo = saldo
        
    # métodos getters para nro de cuenta y saldo
    def get_nro_cuenta(self):
        return self.__nro_cuenta

    def get_saldo(self):
        return self.__saldo

    # método para depositar saldo a la cuenta bancaria
    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor que cero.")
        else:
            self.__saldo += monto

    # método para retirar saldo de la cuenta bancaria
    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor que cero.")
        if monto > self.__saldo:
            raise ValueError("Fondos insuficientes. ")
        else:
            self.__saldo -= monto