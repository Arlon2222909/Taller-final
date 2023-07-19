from datetime import datetime

class Producto:

    def __init__(self,nombre,codigo,precio,stock):
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio
        self.stock = stock

    def informe(self):
        return f"{self.codigo} - {self.nombre} - Precio: ${self.precio} - Stock: {self.stock}"
    
class Inventario:

    def __init__(self):
        self.productos =[]

    def agregar(self,producto):
        self.productos.append(producto)

    def buscar_producto_por_codigo(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None
    
    def actualizar(self,codigo,cantidad):
        producto = self.buscar_producto_por_codigo(codigo)
        if producto:
            producto.stock += cantidad

    def generar_informe(self):
        informe = "Inventario:\n"
        for producto in self.productos:
            informe += str(producto) + "\n"
        return informe
    
class Venta:

    def __init__(self):
        self.ventas = []

    def agregar_venta(self,codigo,cantidad):
        self.ventas.append({"codigo": codigo, "cantidad": cantidad })

    def generar_total_ventas(self, inventario):
        total = 0
        for venta in self.ventas:
            producto = inventario.buscar_producto_por_codigo(venta["codigo"])
            if producto:
                subtotal = producto.precio * venta["cantidad"]
                total += subtotal
        return total
    

    def generar_informe_ventas(self,inventario, fecha_inicio,fecha_fin):
        informe = "Informe de ventas:\n"
        try:
            fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
            fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
            for venta in self.ventas:
                producto = inventario.buscar_producto_por_codigo(venta["codigo"])
                if producto:
                    fecha_venta = datetime.now()  # Suponemos que la venta ocurre en el momento actual
                    if fecha_inicio <= fecha_venta <= fecha_fin:
                        subtotal = producto.precio * venta["cantidad"]
                        informe += f"{producto.nombre} - Cantidad vendida: {venta['cantidad']} - Monto total: ${subtotal}\n"
        except ValueError:
            informe = "Error: El formato de fecha debe ser 'YYYY-MM-DD'"
        return informe


if __name__ == "_main_":
    inventario = Inventario()

    producto1 = Producto(1, "Camiseta", 20, 100)
    producto2 = Producto(2, "Pantalón", 30, 80)

    inventario.agregar_producto(producto1)
    inventario.agregar_producto(producto2)

    print(inventario.generar_informe())

    venta = Venta()
    venta.agregar_venta(1, 3)
    venta.agregar_venta(2, 2)

    total_venta = venta.generar_total_venta(inventario)
    print(f"Total venta: ${total_venta}")

    inventario.actualizar_stock(1, -3)
    print(inventario.generar_informe())

    venta.agregar_venta(1, 2)
    venta.agregar_venta(2, 4)

    informe_ventas = venta.generar_informe_ventas(inventario, "2023-04-24", "2023-06-18")
    print(informe_ventas)

    
    inventario.agregar_stock(1, 10)
    print(inventario.generar_informe())


        
        