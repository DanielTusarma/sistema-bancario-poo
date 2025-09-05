# Importacion de funciones
from services.operations import (
    crear_cuenta, 
    depositar_en_cuenta,
    retirar_de_cuenta,
    trasferir_entre_cuentas,
    consultar_saldo)

# Función principal del programa
def main():
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
            
            
if __name__ == "__main__":
    main()