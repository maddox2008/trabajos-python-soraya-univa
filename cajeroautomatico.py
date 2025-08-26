saldo = 1000
pin_correcto = "1234"
intentos = 3

def consultar():
    print(f" Su saldo actual es: {saldo}")

def retirar():
    global saldo
    monto = int(input("Ingrese cantidad a retirar: "))
    if monto > saldo:
        print("Retiro rechazado. Dinero insuficientes.")
    elif monto <= 0:
        print(" El monto debe ser mayor a 0.")
    else:
        saldo -= monto
        print(f" Retiro exitoso. Saldo restante: {saldo}")

def depositar():
    global saldo
    monto = int(input("Ingrese cantidad a depositar: "))
    if monto <= 0:
        print(" El depósito debe ser mayor a 0.")
    else:
        saldo += monto
        print(f" Depósito exitoso. Saldo actual: {saldo}")

# --- Programa principal ---
while intentos > 0:
    pin = input("Ingrese su PIN: ")
    if pin == pin_correcto:
        print(" Bienvenido al cajero automático")
        while True:
            print("\nMENÚ ")
            print("1. Consultar saldo")
            print("2. Retirar dinero")
            print("3. Depositar dinero")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                consultar()
            elif opcion == "2":
                retirar()
            elif opcion == "3":
                depositar()
            elif opcion == "4":
                print("👋 Gracias por usar el cajero.")
                exit()
            else:
                print(" Opción no válida.")
    else:
        intentos -= 1
        if intentos > 0:
            print(f" PIN incorrecto. Intentos restantes: {intentos}")
        else:
            print(" Cuenta bloqueada.")
