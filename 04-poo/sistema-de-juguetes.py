
class Jugete:
    def __init__(self, nombre , precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock


    def descripcion(self):
        print(f"su jugete es un : {self.nombre}")
        print(f"su jugete tiene un valor de : ${self.precio}")
        print(f"stock de su jugete: {self.stock}")


lista_jugetes = [

]

def ver_jugetes(lista_jugetes):

    if len(lista_jugetes) == 0:
        print("No hay juguetes en la tienda aún.")
    for jugetitos in lista_jugetes:
        jugetitos.descripcion()




def agregar_jugete(lista_jugetes, nombre, precio, stock):

    for jugete in lista_jugetes:
        if jugete.nombre == nombre:
            return "el juegete que quiere agregar ya existe"


    nuevo = Jugete(nombre,precio,stock)
    lista_jugetes.append(nuevo)
    return "jugete agregado"



def comprar_jugete(lista_jugetes,nombre_buscado):

    for eleccion in lista_jugetes:

        if eleccion.nombre == nombre_buscado:
            if eleccion.stock > 0:

                eleccion.stock-= 1
                return f"precio del jugete es {eleccion.precio}"

            else:
                return "la compra no se puede realizar ya que no queda stock"

    return "compra invalida el buscado no existe"




while True:

    print("1. ver todos los jugetes ")
    print("2. agregar un nuevo jugete ")
    print("3. comprar un jugete ")
    print("4. salir ")

    try:

        op_usuario = int(input("ingrese una opcion:"))

        if op_usuario == 1:

            resultado = ver_jugetes(lista_jugetes)


        elif op_usuario == 2:

            try:
                nombre_objeto=input("ingrese el nombre del jugete: ")

                precio_objeto=float(input("ingrese el precio del jugete: "))

                stock_objeto = int(input("ingrese la cantidad de stock: "))



                resultado  = agregar_jugete(lista_jugetes, nombre_objeto, precio_objeto, stock_objeto)
                print(resultado)

            except ValueError:

                print("ingrese valores indicados porfavor")

                continue


        elif op_usuario == 3:
            try:
                eleccion = input("ingrese el nombre del juegete que desea buscar: ")

                resultado = comprar_jugete(lista_jugetes, eleccion)
                print(resultado)
            except ValueError:
                print("ingrese un nombre valido porfavor")


        elif op_usuario == 4:
            print("eligio salir del programa")
            break

    except ValueError:
        print("ingrese un  numero del menu porfavor")
        continue
