from catalogo import *
class Factura:
    IVA = 0.19 

    def __init__(self):
        self.productos_comprados = []
        self.total = 0


    def agregar_producto(self, producto, cantidad):
        subtotal = producto.precio * cantidad
        self.productos_comprados.append({
            "producto": producto,
            "cantidad": cantidad,
            "subtotal": subtotal
        })
        self.total += subtotal

    def generar_factura(self):
        print("\nFACTURA ELECTRÓNICA ")
        print("Productos comprados:")
        for item in self.productos_comprados:
            producto = item["producto"]
            print(f"{producto.nombre} (x{item['cantidad']}) - COP{producto.precio:.2f} c/u - Subtotal: COP{item['subtotal']:.2f}")
        print(f"Subtotal: COP{self.total:.2f}")
        iva = self.total * self.IVA
        print(f"IVA (19%): COP{iva:.2f}")
        print(f"Total: COP{self.total + iva:.2f}")
    


#agregar producto a la factura 
def agregar_producto_factura(factura, catalogo):
    """Permite al usuario agregar un producto a la factura
    """
    codigo = input("Ingrese el código del producto: ")
    producto = buscar_producto(catalogo, codigo)
    if producto:
        try:
            cantidad = int(input(f"Ingrese la cantidad de {producto.nombre} a comprar: "))
            factura.agregar_producto(producto, cantidad)
            print(f"{cantidad} unidad(es) de {producto.nombre} agregadas al carrito.")
        except ValueError:
            print("Cantidad inválida. Intente de nuevo.")
    else:
        print("Producto no encontrado. Intente de nuevo.")