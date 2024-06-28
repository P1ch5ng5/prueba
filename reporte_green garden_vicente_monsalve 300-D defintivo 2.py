import json
import os

registro = "registro+.json"

def cargar_datos():
    if os.path.exists(registro):
        with open(registro, "r") as file:
            return json.load(file)
    else:
        return []

def guardar_datos(ventas):
    with open(registro, "w") as file:
        json.dump(ventas, file, indent=4)
    print("Datos guardados correctamente")

def ingresar_venta(ventas):
    nombre = input("Ingrese el nombre del cliente: ")
    rut = input("Ingrese el rut: ")
    direccion = input("Ingrese el la direccion: ")
    producto1= input("ingrese el nombre del producto")
    producto2 = int(input("Ingrese la cantidad de los productos que desee solicitar: "))
    precio= int((input("porfavor indique el precio:")))
    total= print("total=",producto1,producto2*precio)
    venta = {
        "Nombre": nombre,
        "rut": rut,
        "direccion": direccion,
        "productos": producto1,
        "Productos": producto2,
        "precio": precio,
        "total": total,
    }
    
    ventas.append(venta)
    print("Venta registrada correctamente")

def actualizar_registro(ventas):
    Id = input("Ingrese el número de Id de la venta a actualizar: ")
    for venta in ventas:
        if venta["Id"] == Id:
            direccion = input("Ingrese la nueva direccion: ")
            nombre = input("Ingrese el nuevo nombre: ")
            producto = input("Ingrese el/los nuevos productos: ")
            precio = input("ingrese el precio del producto: ")
            venta["direccion"] = direccion
            venta["Nombre"] = nombre
            venta["Productos"] = producto
            venta["precio"] = precio 
            print("Actualización exitosa.")
            return
    print("Id no encontrada.")

def eliminar_registro(ventas):
    Id = input("Ingrese el número de Id de la venta a eliminar: ")
    for i, venta in enumerate(ventas):
        if venta["Id"] == Id:
            del ventas[i]
            print("Venta eliminada exitosamente")
            return
    print("Id no encontrada.")
def menu_productos(ventas):
    
        print("""Productos y Precios
        Abono = 1200$
        Tierra = 1000$
        Lirio = 1100$ 
        Rosas rojas = 1700$
        Margaritas = 1100$""")
        print("""cantidad disponible
            abono = 50
            tierra = 35
            lirio = 40  
            rosas rojas = 43
            margaritas = 10
                """)

def menu():
    ventas = cargar_datos()
    
    
    while True:
        print("\nOpciones:")
        print("1. menu productos ")
        print("2. Ingresar una venta")
        print("3. Actualizar una venta")
        print("4. Eliminar una venta")
        print("5. Guardar cambios")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_productos(ventas)
        elif opcion == "2":
            ingresar_venta(ventas)
        elif opcion == "3":
            actualizar_registro(ventas)
        elif opcion == "4":
            eliminar_registro(ventas)
        elif opcion == "5":
            guardar_datos(ventas)
        
        elif opcion == "6":
            print("boleta"
                  ,ventas,
                  """resumen de ventas 
                  gracias por su compra
                  """)
            break
        else:
            print("Opción no válida. Intente de nuevo.")
        

if __name__ == "__main__":
    menu()
