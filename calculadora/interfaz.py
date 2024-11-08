
#Funcion menu principal
def menu ():
    """
    Muestra el menu de las figuras geometricas,
    retor la variable opcion
    """
    print("\n Bienvenido a la cálculadora de figuras")
    print("1. Cuadrado")
    print("2. Triangulo")
    print("3. Circulo")
    print("4. Pentagono")
    print("5. Trapecio")
    print("6. Romboide")
    print("7. Rombo")
    print("8. Rectangulo")
    print("8. Salir")
    
    op = int(input("Digite una opción del menú: "))
    return op
def opcion_seleccionada (op):
    """
    Mostrar lo seleccionado del menu
    """
    #Variables
    CUDRADO = 1
    TRIANGULO = 2
    CIRCULO = 3
    PENTAGONO = 4
    TRAPECIO = 5
    ROMBOIDE = 6 
    ROMBO = 7 
    RECTANGULO = 8
    SALIR = 9

    if op == 1:
        print(f"Usted selecciono la opción CUADRADO")
        return CUDRADO
    elif op == 2:
        print(f"Usted selecciono la opción TRIANGULO")
        return TRIANGULO
    elif op == 3:
        print(f"Usted selecciono la opción CIRCULO")
        return CIRCULO
    elif op == 4:
        print(f"Usted selecciono la opción PENTAGONO")
        return PENTAGONO
    elif op == 5:
        print(f"Usted selecciono la opción TRAPECIO")
        return TRAPECIO
    elif op == 6:
        print(f"Usted selecciono la opción ROMBOIDE")
        return ROMBOIDE
    elif op == 7:
        print(f"Usted selecciono la opción ROMBO")
        return ROMBO
    elif op == 8:
        print(f"Usted selecciono la opción RECTANGULO")
        return RECTANGULO
    elif op == 9:
        print(f"Saliendo de la calculadora....")
        return SALIR
    else:
        print(f"Opcion no valida!!!")
        return "Opcion no valida!!!"

#solicitud de datos
#cuadrado
def solicitud_cuadrado():
    """"
    solicita el lado para calcular el area
    lado, tipo de dato
    """
    lado = float(input("digite el lado: "))
    return lado

def solicitud_triangulo():
    """"
    solicita el lado para calcular el area
    , tipo de dato retorna primero a la base
    y luego a la altura
    """
    base = float(input("digite la base: "))
    altura = float(input("digite la altura: "))
    return base,altura

def solicitud_circulo():
    """"
    solicita el lado para calcular el area
    , tipo de dato retorna al radio
    """
    radio = float(input("digite el radio: "))
    return radio

def solicitud_pentagono():
    """"
    solicita datos para calcular el area de 
    un pentagono
    """
    perimetro = float(input("digite el perimetro: "))
    apotema = float(input("digite la apotema : "))
    return perimetro, apotema

def solicitud_trapecio():
    """"
    se requiere las dos bases y la atura 
    para poder calcular la base
    """
    basemayor = float(input("digite la base mayor: "))
    basemenor= float(input("digite la base menor: "))
    
    return basemayor, basemenor

def solicitud_romboide():
    """"
    solicita la base y la altura 
    para calcular el area
    """
    base = float(input("digite la base: "))
    altura = float(input("digite la altura: "))
    return base,altura

def solicitud_rombo():
    """"
    solcita diagonal mayor y la multiplica por 
    la diagonal menor para divir el resultado en dos 
    """
    diagonalmayor = float(input("digite la diagonal mayor: "))
    diagonalmenor = float(input("digite la diagonal menor: "))
    return diagonalmayor,diagonalmenor

def solicitud_rectangulo():
    """"
    solicita la base y la altura 
    para calcular el area
    """
    base = float(input("digite la base: "))
    altura = float(input("digite la altura: "))
    return base, altura


#mostrar informacion de las areas
#mostrar area cuadrado

def mostrar_cuadrado(area):
    """
    mostrar el area del cuadrado
    tipo float
    """
    print(f"el area del cuadrado es:{area}")


#mostrar triangulo
def mostrar_triangulo(area):
    """
    mostrar el area del triangulo
    tipo float
    """
    print(f"el area del circulo es:{area}")

#
def mostrar_circulo(area):
    """
    mostrar el area del circulo
    tipo float
    """
    print(f"el area del circulo es:{area}")

#
def mostrar_pentagono(area):
    """
    mostrar el area del 
    tipo float
    """
    print(f"el area del pentagono es:{area}")

#
def mostrar_trapecio(area):
    """
    mostrar el area del 
    tipo float
    """
    print(f"el area del trapecio es:{area}")

#
def mostrar_romboide(area):
    """
    mostrar el area del 
    tipo float
    """
    print(f"el area del romboide es:{area}")

#
def mostrar_rombo(area):
    """
    mostrar el area del 
    tipo float
    """
    print(f"el area del rombo es:{area}")

#
def mostrar_rectangulo(area):
    """
    mostrar el area del 
    tipo float
    """
    print(f"el area del rectangulo es:{area}")