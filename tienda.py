from producto import Producto

class Tienda:
    def __init__(self, nombre:str, delivery:float):
        self._nombre = nombre
        self._delivery = delivery
        self._productos = []
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def delivery(self):
        return self._delivery
    
    def ingresar_producto(self, producto, Producto):
        for p in self._productos:
            if p == producto:
                p + producto
                return
        self._productos.append(producto)