import math
def area_cuadrado(lado):
    """
    calcula el area del cuadrado, 
    a = 1 * 1
    """
    return lado * lado
def area_triangulo(base,altura):
    """
    calcula el area de un triangulo 
    a = base*altura/2
    """
    return (base * altura)/2
#area circulo
def area_circulo(radio):
    """
    calcula el area del circulo 
    a = pi*radio^2
    """
    return math.pi * radio * radio
def area_pentagono(lado, apotema):
    """
    calcula el area de un pentagono
    """
    return (5 * lado * apotema) / 2
def area_trapecio(base_menor, base_mayor, altura):
    """
    calcula el area de un trapecio
    a = Bm=BM * h / 2
    """ 
    return ((base_menor + base_mayor) * altura) / 2
def area_rombo(diagonal_mayor, diagonal_menor):
    """
    calcula el area de un rombo 
    a = DM * Dm / 2
    """
    return (diagonal_mayor * diagonal_menor) / 2
def area_romboide_rectangulo(base, altura):
    """
    Calcula el area de un rombiode o rectangulo
    a = b * h
    """
    return base * altura