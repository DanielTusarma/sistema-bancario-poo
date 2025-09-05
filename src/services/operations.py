#importamos la clase Cuenta_Bancaria desde el moódulo de cuenta_bancaria
from models.Cuenta_Bancaria import Cuenta_Bancaria

# función que crea una cuenta bancaria
def crear_cuenta(cuentas):
    nro_cuenta = input("Ingrese el nro de cuenta: ")
    try:
        saldo_inicial = float(input("Ingrese el saldo inicial: "))
    except ValueError:
        print("El saldo inicial debe ser un número.")   
        return
    cuentas[nro_cuenta] = Cuenta_Bancaria(nro_cuenta, saldo_inicial)
    print(f"Cuenta {nro_cuenta} creada con saldo inicial de {saldo_inicial} ")
    
# función que permite depositar en una cuenta bancaria existente
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

# función que permite retirar saldo de una cuenta bancaria existente
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

# función para transferir saldo entre dos cuentas bancarias existentes      
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

# función para consultar el saldo disponible de una cuenta bancaria existente        
def consultar_saldo(cuentas):
    nro_cuenta = input("Ingrese el nro de cuenta: ")
    if nro_cuenta in cuentas:
        saldo = cuentas[nro_cuenta].get_saldo()
        print(f"El saldo de la cuenta {nro_cuenta} es de {saldo} ")
    else:
        print("Cuenta no encontrada. ")

