#importar libreria de varios archivos

from interfaz import (menu, 
                      opcion_seleccionada, 
                      solicitud_cuadrado,
                      solicitud_triangulo,
                      solicitud_circulo,
                      solicitud_pentagono,
                      solicitud_trapecio,
                      solicitud_romboide,
                      solicitud_rombo,
                      solicitud_rectangulo,
                      mostrar_cuadrado,
                      mostrar_triangulo,
                      mostrar_circulo,
                      mostrar_pentagono,
                      mostrar_trapecio,
                      mostrar_romboide,
                      mostrar_rombo,
                      mostrar_rectangulo)

from figuras import (area_cuadrado,
                     area_triangulo,
                     area_circulo,
                     area_pentagono,
                     area_rectangulo,
                     area_rombo,
                     area_romboide,
                     area_trapecio)


#variables
opcion = 0
#funcion pricipal
while opcion != 4:
    op = menu()
    formas_geometricas = opcion_seleccionada(op)
    #condiciones
    #cuadrado
    if formas_geometricas == 1:
        lado = solicitud_cuadrado()
        area = area_cuadrado(lado)
        mostrar_cuadrado(area)
    
    #triangulo
    elif formas_geometricas == 2:
        lado = solicitud_triangulo()
        area = area_triangulo(lado)
        mostrar_triangulo(area)
    
    #circulo
    elif formas_geometricas == 3:
        lado = solicitud_circulo()
        area = area_circulo(lado)
        mostrar_circulo(area)
    
    #pentagono
    elif formas_geometricas == 4:
        lado = solicitud_pentagono()
        area = area_pentagono(lado)
        mostrar_pentagono(area)
    
    #trapecio
    elif formas_geometricas == 5:
        lado = solicitud_trapecio()
        area = area_trapecio(lado)
        mostrar_trapecio(area)
    
    #romboide
    elif formas_geometricas == 6:
        lado = solicitud_romboide()
        area = area_romboide(lado)
        mostrar_romboide(area)
    
    #rombo
    elif formas_geometricas == 7:
        lado = solicitud_rombo()
        area = area_rombo(lado)
        mostrar_rombo(area)
    
    #rectangulo
    elif formas_geometricas == 8:
        lado = solicitud_rectangulo()
        area = area_rectangulo(lado)
        mostrar_rectangulo(area)
        
    elif formas_geometricas == 9:
        print("saliendo de la calculadora....")
        break
    else: 
        print("opcion incorrecta")

print("gracias por usar mi calculadora de figuras geometricas")

