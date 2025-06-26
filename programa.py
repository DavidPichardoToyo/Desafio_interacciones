import os
from tienda import Restaurante, Supermercado, Farmacia
from producto import Producto

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def crear_tienda():
    limpiar_pantalla()
    print("=CREAR TIENDA=")
    tipo = input("Tipo de tienda (restaurante/supermercado/farmacia): ").lower()
    nombre = input("Nombre de la tienda : ")
    costo = float(input("Costo de delivery : "))
    if tipo == "restaurante":
        return Restaurante(nombre, costo)
    
    elif tipo == "supermercado":
        return Supermercado(nombre, costo)
    
    elif tipo == "farmacia":
        return Farmacia(nombre, costo)
    
    else:
        print("Tipo de tienda no válido. Intente nuevamente")
        return crear_tienda
    
def ingresar_productos(tienda):
    while True:
        limpiar_pantalla()
        print(f"= INGRESAR PRODUCTOS a {tienda.nombre} =")
        nombre = input("Nombre del producto : ")
        precio = float(input("Precio del producto : "))
        stock_input = input("Stock (enter para 0) : ")
        stock = int(stock_input) if stock_input else 0
        p = Producto(nombre, precio, stock)
        tienda.ingresar_producto(p)
        if input("¿Ingresar otro producto? (s/n): ").lower() != "s":
            break

def menu(tienda):
    while True:
        limpiar_pantalla()
        print(f"= MENÚ {tienda.nombre} =")
        print("1. Listar productos")
        print("2. Realizar venta")
        print("3. Salir")
        opcion = input("Selecciona opción : ")

        if opcion == "1":
            limpiar_pantalla()
            print(tienda.listar_producto())
            input("\nPresiona Enter para continuar...")

        elif opcion == "2":
            nombre = input("Nombre del producto : ")
            cantidad = int(input("Cantidad : "))
            tienda.realizar_venta(nombre, cantidad)
            print("Venta procesada (si fue válida).")
            input("\nPresiona Enter para continuar...")

        elif opcion == "3":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida.")
            input("\nPresiona Enter para continuar...")

def main():
    tienda = crear_tienda()
    ingresar_productos(tienda)
    menu(tienda)

if __name__ == "__main__":
    main()