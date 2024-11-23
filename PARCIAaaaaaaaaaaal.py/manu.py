from catalogo import *
from facturacion import *
def menu_principal():
    """Función principal del sistema de facturación."""
    catalogo = crear_catalogo()
    factura = Factura()

    while True:
        print("\n MENÚ PRINCIPAL")
        print("1. Mostrar catálogo")
        print("2. Agregar producto al carrito")
        print("3. Generar factura")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_catalogo(catalogo)
        elif opcion == "2":
            agregar_producto_factura(factura, catalogo)
        elif opcion == "3":
            factura.generar_factura()
        elif opcion == "4":
            print("Gracias por usar el sistema de facturación. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    menu_principal()