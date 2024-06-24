import funcionesPrueba as funcion
import time
import os

Flag=True

# Menú --> Benjamín García
while Flag:
    print("\n:::: TIENDA PAILITA ::::\n")
    print("1.- Agregar un producto")
    print("2.- Ver todos los productos")
    print("3.- Modificar un producto")
    print("4.- Eliminar un producto")
    print("5.- Guardar colección en un archivo")
    print("6.- Salir del programa")
    try:
        opcion=int(input("\nPor favor ingrese una opción: "))
    except:
        print("Por favor ingrese una opción valida")
    else:
        if opcion==1:
            funcion.agregar_productos()
        elif opcion==2:
            funcion.mostrar_productos()
        elif opcion==3:
            codigo=int(input("Ingrese el codigo que desea modificar: "))
            funcion.modificar_producto(codigo)        
        elif opcion==4:
            codigo=int(input("Ingrese el codigo que desea modificar: "))
            funcion.eliminar_producto(codigo)
        elif opcion==5:
            print("Para ver el listado de productos DÍRIJASE AL ARCHIVO .txt al lado izquierdo.")
        elif opcion == 6:
            print("Saliendo del programa...")
            time.sleep(1.2)
            # Eliminar el archivo "listado_de_productos.txt".
            try:
                os.remove("listado_de_productos.txt")
                print("El archivo 'listado_de_productos.txt' ha sido eliminado.")
            except FileNotFoundError:
                print("El archivo 'listado_de_productos.txt' no fue encontrado")
                Flag=False
                break # Cerrar el programa.
        else:
            print("Por favor ingrese una opción válida.") # El usuario necesita ingresar una opción válida.
