#importar libreria de varios archivos

from interfaz import *
from figuras import *

calculos_area = {
    "CUADRADO": area_cuadrado,
    "TRIÁNGULO": area_triangulo,
    "CÍRCULO": area_circulo,
    "PENTÁGONO": area_pentagono,
    "TRAPECIO": area_trapecio,
    "ROMBO": area_rombo,
    "ROMBOIDE": area_romboide_rectangulo,
    "RECTÁNGULO": area_romboide_rectangulo
}

while True:
    op = menu()
    figura = opcion_seleccionada(op)
    
    # Si se selecciona "SALIR" o una opción no válida
    if figura == "SALIR":
        print("Saliendo de la calculadora...")
        break
    elif figura not in calculos_area:
        print("Opción incorrecta")
        continue
    
    # Solicitar datos, calcular área y mostrar el resultado
    datos = solicitud_datos(figura)
    area = calculos_area[figura](*datos)
    mostrar_area(figura, area)

print("Gracias por usar mi calculadora de figuras geométricas")