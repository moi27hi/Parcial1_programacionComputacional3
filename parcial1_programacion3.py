#Enunciado

class Producto:

    def __init__(self,codigo,nombre,categoria,precio):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio



class GestorVentas:
    def __init__(self):
        self.catalogo = []
        self.ventas = []

    def agregar_producto(self,producto):
        self.catalogo.append(producto)
        print(f'Producto agregado : {Producto.no}')


        


    def registrar_venta(self):
         self.nombre_producto = input("Ingrese el nombre del producto")
         cantidad = int(input("Ingrese la cantidad: "))

         for producto in self.catalogo:
             if producto.nombre == nombre_producto: 
                 total =producto.precio * cantidad
                 self.ventas.append((producto,cantidad,total))
                 print(f"Venta registrada: {cantidad} x {producto.nombre} = ${total}")





    
    