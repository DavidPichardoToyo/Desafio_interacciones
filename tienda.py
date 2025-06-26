from producto import Producto
from abc import ABC, abstractmethod


class Tienda(ABC):
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

    @abstractmethod
    def listar_producto(self):
        pass
    
    @abstractmethod
    def realizar_venta(self, nombre_producto: str, cantidad:str):
        pass


# Clase Restaurante
class Restaurante(Tienda):
    def ingresar_producto(self, producto: Producto):
        producto.stock = 0
        super().ingresar_producto(producto)

    def listar_producto(self):
        resultado = f"Productos de Restaurante {self.nombre}:\n"
        for p in self._productos:
            resultado += f" - {p.nombre} | ${p.precio}\n"
        
        return resultado
    
    def realizar_venta(self,nombre_producto: str, cantidad: int):
        pass # No modifica stock

#Clase Supermercado
class Supermercado(Tienda):
    def listar_producto(self):
        resultado = f"Productos de Supermercado {self.nombre}:\n"
        for p in self._productos:
            info_stock = f"{p.stock}"
            if p.stock < 10:
                info_stock += "Pocos productos disponibles"
            resultado += f"- {p.nombre} | ${p.precio} | Stock: {info_stock}\n"
        return resultado