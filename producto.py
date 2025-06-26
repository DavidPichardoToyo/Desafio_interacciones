class Producto:
    def __init__(self, nombre:str, precio:float, stock: int = 0):
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
    def stock(self, nuevo_stock):
        self.__stock = nuevo_stock
    
    def __eq__(self, otro):
        if isinstance(otro, Producto):
            return self.nombre == otro.nombre
        return False
    
    def __add__(self, otro):
        if isinstance(otro, Producto) and self == otro:
            self.stock += otro.stock
        return self
    
    def __sub__(self, cantidad):
        self.stock = self.stock - cantidad
        return self        