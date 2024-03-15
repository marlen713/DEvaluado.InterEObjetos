
from tienda import Restaurante, Farmacia, Supermecado
from producto import Producto

# Crear una instancia de la tienda
tienda_restaurante = Restaurante("Tienda Restaurante", 5)
tienda_farmacia = Farmacia("Mi Farmacia", 5)
tienda_supermercado = Supermecado("El Supermercado", 5)

#Bienvenida y opcion de escoger alguna de las 3 tiendas por primera letra del nombre a traves del input.
print("------------------------------------------------------------------------------------------------------------------------------")
print('''Hola BIENVENIDOS!!. Sus Opciones son:
r = Restaurante
f = Farmacia 
s = Supermercado ''')
tienda_nombre = input("Digite letra de la Tienda: ").lower()

#SE IMPLEMENTA PARA QUE LA PERSONA VEA LA TIENDA QUE ESCOGIO
if tienda_nombre == "r":
    tienda_seleccionada = tienda_restaurante
    print("Restaurante")
elif tienda_nombre == "f":
    tienda_seleccionada = tienda_farmacia
    print("Farmacia")
elif tienda_nombre == "s":
    tienda_seleccionada = tienda_supermercado
    print("Supermercado")
else:
    print("Opcion No valida")

# Lógica para ingresar productos, listar productos y realizar ventas
while True:
    opcion = input("Ingrese '1' para ingresar un producto, '2' para listar productos, '3' para realizar una venta, o '4' para salir: ")
    
    # DEBES INGRESAR ALGUN PRODUCTO PARA QUE ESTE QUEDE ALMACENADO, PARA QUE LUEGO PUEDAS LISTAR O VENDER. si no lo ingresas no podras ver nada
    if opcion == '1':
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock del producto: "))
        producto = Producto(nombre, precio, stock)
        tienda_seleccionada.ingresar_producto(producto)
        
    #LUEGO DE INGRESAR EL PRODUCTO PUEDES CONSULTAR LA DISPONIBILIDAD, INCLUSO DESPUES DE LA VENTA PUEDES LISTAR PARA VER CUANTOS QUEDAN
    elif opcion == '2':
        print(tienda_seleccionada.listar_productos())
        
    #LUEGO QUE VENDES, PUEDES LISTAR PARA QUE VEAS LO QUE TE QUEDA DE PRODUCTO
    elif opcion == '3':
        nombre_producto = input("Ingrese el nombre del producto a vender: ")
        cantidad = int(input("Ingrese la cantidad a vender: "))
        precio_venta = float(input("Ingrese el precio de venta: "))
        print(tienda_seleccionada.realizar_venta(nombre_producto, cantidad))
    
    elif opcion == '4':
        break



