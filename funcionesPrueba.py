productos = []

# Agregar productos --> Francisco Vera
def agregar_productos():
    codigo = int(input("Ingrese el código del producto: "))
    nombre_producto = input("Ingrese el nombre del producto: ").upper()
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = int(input("Ingrese el precio del producto: "))
    producto = {"codigo": codigo, "nombre_producto": nombre_producto, "cantidad": cantidad, "precio": precio}
    productos.append(producto)
    print("Producto añadido a inventario.")
    crear_planilla_txt(codigo, nombre_producto, cantidad, precio)

# Ver productos --> Francisco Vera
def mostrar_productos():
    if len(productos) == 0:
        print("No hay productos en inventario.")
    else:
        print("Listado de productos:")
        for i, producto in enumerate(productos, start=1):
            codigo = producto["codigo"]
            nombre_producto = producto["nombre_producto"]
            cantidad = producto["cantidad"]
            print(f"{i}. {codigo} - {nombre_producto} - {cantidad}")

# Modificar un producto --> Cristóbal González
def modificar_producto(codigo):
    for producto in productos:
        if producto["codigo"] == codigo:
            nuevo_nombre = input(f"Ingrese el nuevo nombre para '{producto['nombre_producto']}': ").upper()
            nuevo_cantidad = int(input(f"Ingrese la nueva cantidad para '{producto['nombre_producto']}': "))
            nuevo_precio = int(input(f"Ingrese el nuevo precio para '{producto['nombre_producto']}': "))
            # Actualizar los datos del producto
            producto["nombre_producto"] = nuevo_nombre
            producto["cantidad"] = nuevo_cantidad
            producto["precio"] = nuevo_precio
            print(f"Producto con código {codigo} modificado correctamente.")
            # Actualizar la planilla de texto
            with open("listado_de_productos.txt", "w") as file:
                for i in productos:
                    file.write(f"Codigo del producto: {i['codigo']}\n")
                    file.write(f"Producto: {i['nombre_producto']}\n")
                    file.write(f"Cantidad de productos: {i['cantidad']}\n")
                    file.write(f"Precio del producto: {i['precio']}\n\n")
            return
    print(f"No se encontró ningún producto con el código {codigo}.")

# Función para eliminar un producto por su código --> Cristóbal González
def eliminar_producto(codigo):
    for producto in productos[:]:
        if producto["codigo"] == codigo:
            productos.remove(producto)
            print(f"Producto con código {codigo} eliminado del inventario.")
            return
    print(f"No se encontró ningún producto con el código {codigo}.")

# Crear planilla de txt --> Benjamin García
def crear_planilla_txt(codigo, nombre_producto, cantidad, precio):
    with open("listado_de_productos.txt", "a") as archivo:
        archivo.write(f"Codigo del producto: {codigo}\n")
        archivo.write(f"Producto: {nombre_producto}\n")
        archivo.write(f"Cantidad de productos: {cantidad}\n")
        archivo.write(f"Precio del producto c/u: {precio}\n")
        archivo.write("\n")
