
# Me piden que utilice ENCAPSULAMIENTO)

class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock (self, cantidad):
        if cantidad < 0:
            self.__stock = 0
        else:
            self.__stock = cantidad
            
#NAM