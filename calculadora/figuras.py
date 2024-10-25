#import math
import math

#area cuadrado
def area_cuadrado(lado):
    """
    calcula el area del cuadrado, 
    a = 1 * 1
    tipo float
    """
    
    area = lado * lado
    return area

#area triangulo
def area_triangulo(base,altura):
    """
    calcula el area de un triangulo 
    base*altura/2
    """
    area = (base * altura)/2
    return area

#area circulo
def area_circulo(radio):
    """
    calcula el area del circulo 
    pi*radio^2
    """
    area = math.pi * radio * radio
    return area


