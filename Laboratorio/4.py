class Producto:
    def __init__(self, nombre, precio, cantidad):
        """
        Inicializa un producto con nombre, precio y cantidad en stock
        """
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def aumentar_stock(self, cantidad):
        """
        Aumenta el stock del producto
        """
        if cantidad > 0:
            self.cantidad += cantidad
            print(f"Se han agregado {cantidad} unidades de {self.nombre}.")
        else:
            print(f"La cantidad para aumentar debe ser positiva.")

    def disminuir_stock(self, cantidad):
        """
        Disminuye el stock del producto, si hay suficiente inventario
        """
        if cantidad > 0:
            if cantidad <= self.cantidad:
                self.cantidad -= cantidad
                print(f"Se han vendido {cantidad} unidades de {self.nombre}.")
            else:
                print(f"No hay suficiente stock de {self.nombre} para disminuir {cantidad}.")
        else:
            print(f"La cantidad para disminuir debe ser positiva.")

    def __str__(self):
        """
        Representación en texto del producto
        """
        return f"{self.nombre}: Precio COP:{self.precio}, Stock {self.cantidad}"


inventario = [
    Producto("Manzanas", 500, 100),
    Producto("Naranjas", 700, 150),
    Producto("Plátanos", 600, 200),
    Producto("Mandarinas", 600, 150),
    Producto("Uvas", 800, 120)
]

def mostrar_inventario(inventario):
    """
    Muestra el inventario completo
    """
    print("\nInventario:")
    for i, producto in enumerate(inventario):
        print(f"{i + 1}. {producto}")

def menu_interactivo():
    """
    Muestra un menú interactivo para gestionar el inventario
    """
    while True:
        print("\nGestión de Inventario")
        print("1. Ver inventario")
        print("2. Aumentar stock de un producto")
        print("3. Disminuir stock de un producto")
        print("4. Salir")
        
        opcion = input("Seleccione una opción : ")
        
        if opcion == "1":
            mostrar_inventario(inventario)
        elif opcion == "2":
            mostrar_inventario(inventario)
            try:
                indice = int(input("Seleccione el número del producto para aumentar stock: ")) - 1
                cantidad = int(input("Ingrese la cantidad a aumentar: "))
                if 0 <= indice < len(inventario):
                    inventario[indice].aumentar_stock(cantidad)
                else:
                    print("Producto no válido.")
            except ValueError:
                print("Entrada inválida. Por favor, introduzca números.")
        elif opcion == "3":
            mostrar_inventario(inventario)
            try:
                indice = int(input("Seleccione el número del producto para disminuir stock: ")) - 1
                cantidad = int(input("Ingrese la cantidad a disminuir: "))
                if 0 <= indice < len(inventario):
                    inventario[indice].disminuir_stock(cantidad)
                else:
                    print("Producto no válido.")
            except ValueError:
                print("Entrada inválida. Por favor, introduzca números.")
        elif opcion == "4":
            print("Saliendo del programa. ¡Gracias!")
            break
        else:
            print("Opción no válida. Por favor, seleccione entre 1 y 4.")

# Iniciar el programa interactivo
menu_interactivo()

