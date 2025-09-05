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

# método que crea una cuenta bancaria
def crear_cuenta(cuentas):
    nro_cuenta = input("Ingrese el nro de cuenta: ")
    try:
        saldo_inicial = float(input("Ingrese el saldo inicial: "))
    except ValueError:
        print("El saldo inicial debe ser un número.")   
        return
    cuentas[nro_cuenta] = Cuenta_Bancaria(nro_cuenta, saldo_inicial)
    print(f"Cuenta {nro_cuenta} creada con saldo inicial de {saldo_inicial} ")
    
# método que permite depositar en una cuenta bancaria existente
def depositar_en_cuenta(cuentas):
    nro_cuenta = input("Ingrese el nro de cuenta: ")
    try:
        monto = float(input("Ingrese el monto a depositar: "))
    except ValueError:
        print("El monto a depositar debe ser un número.")
        return
    if nro_cuenta in cuentas:
        try:
            cuentas[nro_cuenta].depositar(monto)
            print(f"Depósito de {monto} realizado en la cuenta {nro_cuenta}.")
        except ValueError as e:
            print("Error:", e)
    else:
        print("Cuenta no encontrada.")

# método que permite retirar saldo de una cuenta bancaria existente
def retirar_de_cuenta(cuentas):
    nro_cuenta = input("Ingrese el nro de cuenta: ")
    try:
        monto = float(input("Ingrese el monto a retirar: "))
    except ValueError:
        print("El monto a retirar debe ser un número.")
        return
    if nro_cuenta in cuentas:
        try:
            cuentas[nro_cuenta].retirar(monto)
            print(f"Retiro de {monto} realizado en la cuenta {nro_cuenta}. ")
        except ValueError as e:
            print("Error:", e)
    else:
        print("Cuenta no encontrada. ")

# método para transferir saldo entre dos cuentas bancarias existentes      
def trasferir_entre_cuentas(cuentas):
    nro_cuenta_origen = input("Ingrese el nro de cuenta origen: ")
    nro_cuenta_destino = input("Ingrese el nro de cuenta de destino: ")
    try:
        monto = float(input("Ingrese el monto a transferir: "))
    except ValueError:
        print("El monto a transferir debe ser un número.")
        return
    if nro_cuenta_origen in cuentas and nro_cuenta_destino in cuentas:
        try:
            cuentas[nro_cuenta_origen].retirar(monto)
            cuentas[nro_cuenta_destino].depositar(monto)
            print(f"Transferencia de {monto} desde la cuenta {nro_cuenta_origen} \
                a la cuenta {nro_cuenta_destino} realizada con exito. ")
        except ValueError as e:
            print("Error:", e)
    else:
        print("Cuenta de origen o de destino no encontrada. ")

# método para consultar el saldo disponible de una cuenta bancaria existente        
def consultar_saldo(cuentas):
    nro_cuenta = input("Ingrese el nro de cuenta: ")
    if nro_cuenta in cuentas:
        saldo = cuentas[nro_cuenta].get_saldo()
        print(f"El saldo de la cuenta {nro_cuenta} es de {saldo} ")
    else:
        print("Cuenta no encontrada. ")

# diccionario para almacenar tanto las cuentas bancarias y los objetos de Cuenta_Bancaria 
cuentas = {}

# bucle principal de control del programa
while True:
    print("\nMenu:")
    print("1. Crear cuenta")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Trasferir")
    print("5. Consultar saldo")
    print("6. Salir")
    
    opcion = input("Seleccione una opción entre 1 y 6: ")
    
    if opcion == '1':
        crear_cuenta(cuentas)
        
    elif opcion == '2':
        depositar_en_cuenta(cuentas)

    elif opcion == '3':
        retirar_de_cuenta(cuentas)
    
    elif opcion == '4':
        trasferir_entre_cuentas(cuentas)
            
    elif opcion == '5':
        consultar_saldo(cuentas)
        
    elif opcion == '6':
        print("Saliendo del programa. ")
        break
    
    else:
        print("Opción inválida. Por favor seleccione una opción entre 1 y 6. ")
