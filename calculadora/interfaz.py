def menu():
    """
    Muestra el menú de las figuras geométricas y retorna la opción seleccionada
    """
    opciones = [
        "Cuadrado", "Triángulo", "Círculo", "Pentágono",
        "Trapecio", "Romboide", "Rombo", "Rectángulo", "Salir"
    ]
    print("\nBienvenido a la calculadora de figuras")
    for i, figura in enumerate(opciones, start=1):
        print(f"{i}. {figura}")
    
    try:
        op = int(input("Seleccione una opción del menú: "))
        return op if 1 <= op <= len(opciones) else None
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return None
def opcion_seleccionada(op):
    """
    Muestra y retorna el nombre de la figura seleccionada
    """
    opciones = {
        1: "CUADRADO", 2: "TRIÁNGULO", 3: "CÍRCULO",
        4: "PENTÁGONO", 5: "TRAPECIO", 6: "ROMBOIDE",
        7: "ROMBO", 8: "RECTÁNGULO", 9: "SALIR"
    }
    figura = opciones.get(op)
    if figura:
        print(f"Usted seleccionó: {figura}")
    else:
        print("Opción no válida.")
    return figura

def solicitud_datos(figura):
    """
    Solicita y retorna los datos necesarios para cada figura
    """
    if figura == "CUADRADO":
        lado = float(input("Digite el lado: "))
        return (lado)
    elif figura == "TRIÁNGULO" or figura == "ROMBOIDE" or figura == "RECTÁNGULO":
        base = float(input("Digite la base: "))
        altura = float(input("Digite la altura: "))
        return base, altura
    elif figura == "CÍRCULO":
        radio = float(input("Digite el radio: "))
        return (radio,)
    elif figura == "PENTÁGONO":
        perimetro = float(input("Digite el perímetro: "))
        apotema = float(input("Digite la apotema: "))
        return perimetro, apotema
    elif figura == "TRAPECIO":
        base_mayor = float(input("Digite la base mayor: "))
        base_menor = float(input("Digite la base menor: "))
        altura = float(input("Digite la altura: "))
        return base_mayor, base_menor, altura
    elif figura == "ROMBO":
        diag_mayor = float(input("Digite la diagonal mayor: "))
        diag_menor = float(input("Digite la diagonal menor: "))
        return diag_mayor, diag_menor
def mostrar_area(figura, area):
    """
    Muestra el área calculada de la figura seleccionada
    """
    print(f"El área del {figura} es: {area}cm")
opcion = menu()
figura = opcion_seleccionada(opcion)
if figura and figura != "SALIR":
    datos = solicitud_datos(figura)