
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
    print("4. Salir")
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
    SALIR = 4

#Condicionales
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
        print(f"Saliendo de la calculadora....")
        return SALIR
    else:
        print(f"Opcion no valida!!!")
        return "Opcion no valida!!!"

#solicitud de datos
#cuadrado
def datos_cuadrado():
    """"
    solicita el lado para calcular el area
    lado, tipo de dato
    """
    lado = float(input("digite el lado: "))
    return lado

def datos_triangulo():
    """"
    solicita el lado para calcular el area
    , tipo de dato retorna primero a la base
    y luego a la altura
    """
    base = float(input("digite la base: "))
    altura = float(input("digite la altura: "))
    return base,altura

def datos_ciriculo():
    """"
    solicita el lado para calcular el area
    , tipo de dato retorna al radio
    """
    radio = float(input("digite el radio: "))
    return radio


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


def mostrar_circulo(area):
    """
    mostrar el area del circulo
    tipo float
    """
    print(f"el area del circulo es:{area}")
