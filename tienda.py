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
    
    def ingresar_producto(self, producto: Producto):
        for p in self._productos:
            if p == producto:
                p + producto
                return
        self._productos.append(producto)

    def listar_producto(self):
        raise NotImplementedError
    
    def realizar_venta(self):
        raise NotImplementedError
    
    class Restaurante(Tienda):
        def ingresar_producto(self, producto: Producto):
            producto.stock = 0
            super().ingresar_producto(producto)

        def listar_producto(self):
            result = f"Productos de Restaurante {self.nombre}:\n"
            for p in self._productos:
                result += f" - {p.nombre} | ${p.precio}\n"
            
            return result
        
        def realizar_venta(self,nombre_procuto: str, cantidad: int):
            pass # No modifica stock