
pin = int(input("ingrese su pin: "))

intentos = 0 
restantes = 3
print()

opcion = 0 
while opcion != 4:

    print("\nSeleccione una opcion")
    print("1. Consultar saldo.")
    print("2. Realizar deposito.")
    print("3. Realizar un retiro.")
    print("4. Salir.")
    
    opcion =int(input(("ingrese su opcion")))
    if opcion == 1:
            dinero = (int(input("ingrese su saldo: ")))
            print(f"su saldo es de {dinero}")
    elif opcion == 2:
            deposito =int(input("Ingrese la cantidad a depositar: "))
            total = dinero + deposito
            print(f"su saldo es de {total}")
    elif opcion == 3:
            retiro = int(input("ingrese la cantidad que va a retirar: "))
            totalr = total - retiro
            print(f"su saldo es de:{totalr} ")
    elif opcion == 4:
            print("saliendo...")
    else:
            print("seleccione una opcion correcta")    

