#importar libreria de varios archivos

from interfaz import (menu, 
                      opcion_seleccionada,
                      datos_cuadrado, 
                      datos_triangulo,
                      datos_ciriculo,
                      mostrar_cuadrado,
                      mostrar_triangulo,
                      area)

from figuras import (area_cuadrado,
                     area_triangulo,
                     area_circulo)


#variables
opcion = 0
#funcion pricipal
while opcion != 4:
    op = menu()
    formas_geometricas = opcion_seleccionada()



#llamar menu
#opcion = menu
#llamar funcion op
#opcion_seleccionada(opcion)


#solicitar cuadrado
#datos_cuadrado()
#lado = datos_cuadrado
#mostrar_cuadrado(area)

#solicitar triangulo 
#datos_triangulo()
#base,altura = datos_triangulo
#area = area_triangulo(base,altura)
#mostrar_triangulo(area)

#solicitar ciriculo 
#datos_ciriculo()
#radio = datos_ciriculo()
#area = area_circulo(radio)
