#Me piden que utilice ABSTRACCIÓN y ENCAPSULAMIENTO

from abc import ABC, abstractmethod
from producto import Producto

class Tienda(ABC):
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []
        
    @property
    def nombre(self):
        return self.__nombre

    @property
    def costo_delivery(self):
        return self.__costo_delivery

    @property
    def productos(self):
        return self.__productos

    @abstractmethod
    def ingresar_producto(self, producto):
        pass

    @abstractmethod
    def listar_productos(self):
        pass

    @abstractmethod
    def realizar_venta(self, nombre_producto, cantidad):
        pass
    
#AQUI CREO MI TIENDA RESTAURANTE            
class Restaurante(Tienda):
    def ingresar_producto(self, producto):
        for p in self.productos:
            if p.nombre == producto.nombre:
                p.stock += producto.stock
                return
        self.productos.append(producto)
    def listar_productos(self):
        productos_str = ""
        for producto in self.productos:
            productos_str += f"Nombre: {producto.nombre}, Precio: {producto.precio}\n"    #NO MOSTRARA EL STOCK
        return productos_str

    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                if producto.stock >= cantidad:
                    producto.stock -= cantidad
                    return f"Venta realizada: {cantidad} unidades de {nombre_producto}"
                else:
                    return "No hay suficiente stock para realizar la venta"
        return "Producto no encontrado en la tienda"

tienda_restaurante = Restaurante("Tienda Restaurante", 5)


#AQUI CREO MI TIENDA FARMACIA
class Farmacia(Tienda):
    def ingresar_producto(self, producto):
        for p in self.productos:
            if p.nombre == producto.nombre:
                p.stock += producto.stock
                return
        self.productos.append(producto)
    def listar_productos(self):
        productos_str = ""
        for producto in self.productos:
            if producto.precio > 15000:  #OJO AQUI AVISO EN LISTAR CUANDO UN PRODUCTO VALE MAS DE 15000 QUE EL ENVIO ES GRATIS
                productos_str += f"Nombre: {producto.nombre}, Precio: {producto.precio} -> Envío gratis al solicitar este producto"
            else:
                productos_str += f"Nombre: {producto.nombre}, Precio: {producto.precio}\n"  #NO MOSTRARA EL STOCK
        return productos_str

    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                if producto.stock >= cantidad:
                    producto.stock -= cantidad
                    return f"Venta realizada: {cantidad} unidades de {nombre_producto}"
                else:
                    return "No hay suficiente stock para realizar la venta"
        return "Producto no encontrado en la tienda"
    
tienda_farmacia = Farmacia("Mi Farmacia", 5)

#AQUI CREO MI TIENDA SUPERMERCADO
class Supermecado(Tienda):
    def ingresar_producto(self, producto):
        for p in self.productos:
            if p.nombre == producto.nombre:
                p.stock += producto.stock
                return
        self.productos.append(producto)
    def listar_productos(self):
        productos_str = ""
        for producto in self.productos:
            productos_str += f"Nombre: {producto.nombre}, Precio: {producto.precio}, Stock: {producto.stock}\n"
        return productos_str

    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                if producto.stock >= cantidad:
                    producto.stock -= cantidad
                    return f"Venta realizada: {cantidad} unidades de {nombre_producto}"
                else:
                    return "No hay suficiente stock para realizar la venta"
        return "Producto no encontrado en la tienda"
    
tienda_supermercado = Supermecado("El Supermercado", 5)


