import json

ARCHIVO = "contactos.json"


def cargar_contactos():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("No existe el archivo de contactos, se creara uno nuevo.")
        return []
    except json.JSONDecodeError:
        print("El archivo de contactos esta dañado, se empezara una agenda vacia.")
        return []


def guardar_contactos(contactos):
    try:
        with open(ARCHIVO, "w", encoding="utf-8") as archivo:
            json.dump(contactos, archivo, indent=4, ensure_ascii=False)
        print("Contactos guardados correctamente.")
    except PermissionError:
        print("No tienes permisos para escribir el archivo.")


def agregar_contacto(contactos):
    nombre = input("Nombre: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacio.")
        return

    telefono = input("Telefono: ").strip()
    if not telefono.isdigit():
        print("El telefono solo debe tener numeros.")
        return

    try:
        edad = int(input("Edad: "))
        if edad <= 0:
            raise ValueError("La edad debe ser mayor que 0.")
    except ValueError as error:
        print("Edad invalida:", error)
        return

    contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "edad": edad
    }
    contactos.append(contacto)
    guardar_contactos(contactos)


def mostrar_contactos(contactos):
    if len(contactos) == 0:
        print("No hay contactos registrados.")
        return

    for posicion, contacto in enumerate(contactos, start=1):
        print(f"{posicion}. {contacto['nombre']} - {contacto['telefono']} - {contacto['edad']} años")


def buscar_contacto(contactos):
    nombre_buscado = input("Nombre a buscar: ").strip().lower()

    for contacto in contactos:
        if contacto["nombre"].lower() == nombre_buscado:
            print("Contacto encontrado:", contacto)
            return

    print("Contacto no encontrado.")


def eliminar_contacto(contactos):
    mostrar_contactos(contactos)

    try:
        posicion = int(input("Numero del contacto a eliminar: "))
        eliminado = contactos.pop(posicion - 1)
        guardar_contactos(contactos)
        print("Se elimino a", eliminado["nombre"])
    except ValueError:
        print("Debes ingresar un numero.")
    except IndexError:
        print("Ese numero de contacto no existe.")


contactos = cargar_contactos()

while True:
    print("\n=== AGENDA DE CONTACTOS ===")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

    try:
        opcion = int(input("Elige una opcion: "))
    except ValueError:
        print("Opcion invalida, ingresa un numero.")
        continue

    if opcion == 1:
        agregar_contacto(contactos)
    elif opcion == 2:
        mostrar_contactos(contactos)
    elif opcion == 3:
        buscar_contacto(contactos)
    elif opcion == 4:
        eliminar_contacto(contactos)
    elif opcion == 5:
        print("Saliendo de la agenda...")
        break
    else:
        print("Esa opcion no existe.")
