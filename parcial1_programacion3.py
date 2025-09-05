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
                 
                 return
             print("Producto no encontrado en el catalogo")

    
    def mostrar_reporte(self,ordenar_por = "ingreso"):
        print("\n === Reporte de ventas ===")
        if not self.ventas:
         print("No hay ventas registradas.")
        return
    

    # resumen de productos.

    resumen = {}

    for producto, cantidad,total in self.ventas:
        if producto.nombre not in resumen:
            resumen[producto.nombre]= {
                "producto": producto,
                "cantidad": 0,
                "ingreso": 0,
            }

    resumen[producto.nombre]["Cantidad"] += cantidad
    resumen[producto.nombre["ingreso"]] += total

    # ordenando segun la clave elegida.

    orden = sorted( 
        resumen.values(),
        key= lamba X: x[ordenar_por],
        reverse=True
    )

     # Mostrar
    print(f"{'Producto':<15}{'Cantidad':<10}{'Ingreso($)':<10}")
    for item in orden:
        print(f"{item['producto'].nombre:<15}{item['cantidad']:<10}{item['ingreso']:<10.2f}")


    # ejemplo de uso.

    if __name__=="_main_":
        gestor = GestorVentas()


 # Cargar algunos productos
    gestor.agregar_producto(Producto("P01", "Manzana", "Fruta", 0.5))
    gestor.agregar_producto(Producto("P02", "Leche", "Lácteo", 1.2))
    gestor.agregar_producto(Producto("P03", "Pan", "Panadería", 0.25))


  # Registrar ventas
    gestor.registrar_venta()
    gestor.registrar_venta()

    

  

    

            

    













    
    