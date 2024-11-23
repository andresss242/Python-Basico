#productos del catalogo 
class Producto:
    def __init__(self, codigo, nombre, precio, categoria):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
#creacion del catalogo
def crear_catalogo():
    """Crea y retorna el catálogo inicial de productos
    """
    return [
        Producto("0001A", "Refrigerador", 1900000, "Línea Blanca"),
        Producto("0002A", "Lavadora", 2000000, "Línea Blanca"),
        Producto("0003A", "Licuadora", 120000, "Pequeños Electrodomésticos"),
        Producto("0004A", "Tostadora", 130000, "Pequeños Electrodomésticos"),
        Producto("0005A", "Televisor", 3000000, "Entretenimiento"),
        Producto("0006A", "Equipo de soonido", 2000000, "Entretenimiento"),
        Producto("0007A", "Aire Acondicionado", 5000000, "Aires Acondicionados")
    ]
#mostrar catalogo
def mostrar_catalogo(catalogo):
    """
    Muestra los productos del catálogo
    """
    print("\n-- CATÁLOGO DE PRODUCTOS--")
    for producto in catalogo:
        print(f"{producto.codigo}: {producto.nombre} - COP-{producto.precio:.2f} ({producto.categoria})")
#buscar en el catalogo
def buscar_producto(catalogo, codigo):
    """
    Busca un producto por su código en el catálogo
    
    """
    for producto in catalogo:
        if producto.codigo == codigo:
            return producto
    return None