from datetime import datetime

ARCHIVO = "diario.txt"


def escribir_entrada():
    texto = input("Escribe tu entrada del dia: ").strip()
    if texto == "":
        print("No puedes guardar una entrada vacia.")
        return

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

    try:
        with open(ARCHIVO, "a", encoding="utf-8") as archivo:
            archivo.write(f"[{fecha}] {texto}\n")
        print("Entrada guardada.")
    except PermissionError:
        print("No se pudo guardar, el archivo no tiene permisos.")


def leer_diario():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        print("Todavia no has escrito nada en tu diario.")
        return

    if len(lineas) == 0:
        print("El diario esta vacio.")
        return

    print("\n=== MI DIARIO ===")
    for linea in lineas:
        print(linea.strip())


def contar_entradas():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            cantidad = len(archivo.readlines())
        print("Tienes", cantidad, "entradas en tu diario.")
    except FileNotFoundError:
        print("Tienes 0 entradas en tu diario.")


def buscar_palabra():
    palabra = input("Palabra a buscar: ").strip().lower()
    encontradas = 0

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            for numero, linea in enumerate(archivo, start=1):
                if palabra in linea.lower():
                    print(f"Linea {numero}: {linea.strip()}")
                    encontradas += 1
    except FileNotFoundError:
        print("El diario no existe todavia.")
        return
    finally:
        print("Busqueda terminada.")

    if encontradas == 0:
        print("No se encontro la palabra.")


def borrar_diario():
    confirmacion = input("Seguro que quieres borrar todo? (si/no): ").strip().lower()
    if confirmacion != "si":
        print("No se borro nada.")
        return

    try:
        with open(ARCHIVO, "w", encoding="utf-8"):
            pass
        print("Diario borrado.")
    except PermissionError:
        print("No se pudo borrar el diario.")


while True:
    print("\n=== DIARIO PERSONAL ===")
    print("1. Escribir entrada")
    print("2. Leer diario")
    print("3. Contar entradas")
    print("4. Buscar palabra")
    print("5. Borrar diario")
    print("6. Salir")

    opcion = input("Elige una opcion: ").strip()

    if opcion == "1":
        escribir_entrada()
    elif opcion == "2":
        leer_diario()
    elif opcion == "3":
        contar_entradas()
    elif opcion == "4":
        buscar_palabra()
    elif opcion == "5":
        borrar_diario()
    elif opcion == "6":
        print("Hasta luego!")
        break
    else:
        print("Opcion invalida.")
