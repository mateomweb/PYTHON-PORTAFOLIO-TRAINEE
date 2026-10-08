import json

ARCHIVO = "inventario.json"


class StockInsuficienteError(Exception):
    pass


def cargar_inventario():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def guardar_inventario(inventario):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(inventario, archivo, indent=4, ensure_ascii=False)


def pedir_numero(mensaje, tipo=int):
    while True:
        try:
            valor = tipo(input(mensaje))
            if valor < 0:
                raise ValueError("no puede ser negativo")
            return valor
        except ValueError as error:
            print("Valor invalido:", error)


def agregar_producto(inventario):
    nombre = input("Nombre del producto: ").strip().lower()
    if nombre == "":
        print("El nombre no puede estar vacio.")
        return

    precio = pedir_numero("Precio: ", float)
    cantidad = pedir_numero("Cantidad: ")

    if nombre in inventario:
        inventario[nombre]["cantidad"] += cantidad
        inventario[nombre]["precio"] = precio
        print("Producto actualizado.")
    else:
        inventario[nombre] = {"precio": precio, "cantidad": cantidad}
        print("Producto agregado.")

    guardar_inventario(inventario)


def vender_producto(inventario):
    nombre = input("Producto a vender: ").strip().lower()
    cantidad = pedir_numero("Cantidad a vender: ")

    try:
        producto = inventario[nombre]
        if cantidad > producto["cantidad"]:
            raise StockInsuficienteError(f"solo quedan {producto['cantidad']} unidades")

        producto["cantidad"] -= cantidad
        total = cantidad * producto["precio"]
    except KeyError:
        print("Ese producto no existe en el inventario.")
    except StockInsuficienteError as error:
        print("No se pudo vender:", error)
    else:
        guardar_inventario(inventario)
        print(f"Venta realizada. Total a pagar: ${total:.2f}")


def mostrar_inventario(inventario):
    if not inventario:
        print("El inventario esta vacio.")
        return

    valor_total = 0
    print("\n=== INVENTARIO ===")
    for nombre, datos in inventario.items():
        subtotal = datos["precio"] * datos["cantidad"]
        valor_total += subtotal
        print(f"{nombre}: ${datos['precio']:.2f} x {datos['cantidad']} = ${subtotal:.2f}")
    print(f"Valor total del inventario: ${valor_total:.2f}")


def exportar_reporte(inventario):
    nombre_reporte = input("Nombre del archivo de reporte: ").strip()
    if not nombre_reporte.endswith(".txt"):
        nombre_reporte += ".txt"

    try:
        with open(nombre_reporte, "w", encoding="utf-8") as reporte:
            reporte.write("REPORTE DE INVENTARIO\n")
            for nombre, datos in inventario.items():
                reporte.write(f"{nombre} - precio: {datos['precio']} - cantidad: {datos['cantidad']}\n")
    except OSError as error:
        print("No se pudo crear el reporte:", error)
    else:
        print("Reporte creado en", nombre_reporte)
    finally:
        print("Proceso de exportacion finalizado.")


inventario = cargar_inventario()

while True:
    print("\n=== INVENTARIO DE TIENDA ===")
    print("1. Agregar producto")
    print("2. Vender producto")
    print("3. Mostrar inventario")
    print("4. Exportar reporte")
    print("5. Salir")

    try:
        opcion = int(input("Elige una opcion: "))
    except ValueError:
        print("Debes ingresar un numero.")
        continue

    if opcion == 1:
        agregar_producto(inventario)
    elif opcion == 2:
        vender_producto(inventario)
    elif opcion == 3:
        mostrar_inventario(inventario)
    elif opcion == 4:
        exportar_reporte(inventario)
    elif opcion == 5:
        print("Cerrando inventario...")
        break
    else:
        print("Opcion invalida.")
