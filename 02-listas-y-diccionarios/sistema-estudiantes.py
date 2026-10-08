diccionario = {}

contador = 1

while True:

    print("")
    print("================================")
    print("     SISTEMA DE ESTUDIANTES")
    print("================================")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Eliminar estudiante")
    print("4. Salir")

    op_usuario = int(input("Ingrese una opcion: "))


    if op_usuario == 1:

        print("")
        print("===== AGREGAR ESTUDIANTE =====")

        nombre_estudiante = input("Ingrese el nombre del estudiante: ")
        edad_estudiante = int(input("Ingrese la edad del estudiante: "))
        curso_estudiante = input("Ingrese el curso del estudiante: ")
        promedio_estudiante = float(input("Ingrese el promedio del estudiante: "))

        diccionario[contador] = {}

        diccionario[contador]["nombre"] = nombre_estudiante
        diccionario[contador]["edad"] = edad_estudiante
        diccionario[contador]["curso"] = curso_estudiante
        diccionario[contador]["promedio"] = promedio_estudiante

        print("")
        print("Estudiante agregado correctamente.")
        print(f"ID asignado: {contador}")

        contador += 1

    elif op_usuario == 2:

        print("")
        print("===== ESTUDIANTES REGISTRADOS =====")

        if len(diccionario) == 0:

            print("No hay estudiantes registrados.")

        else:

            for id, estudiantil in diccionario.items():

                print("")
                print(f"ID: {id}")
                print(f"Nombre: {estudiantil['nombre']}")
                print(f"Edad: {estudiantil['edad']}")
                print(f"Curso: {estudiantil['curso']}")
                print(f"Promedio: {estudiantil['promedio']}")
                print("--------------------------------")

    elif op_usuario == 3:

        print("")
        print("===== ELIMINAR ESTUDIANTE =====")

        id_estudiante = int(
            input("Ingrese el ID del estudiante que desea eliminar: ")
        )

        if id_estudiante in diccionario:

            del diccionario[id_estudiante]

            print("")
            print("Estudiante eliminado correctamente.")

        else:

            print("")
            print("El estudiante que eligio no existe.")


    elif op_usuario == 4:

        print("")
        print("Saliendo del programa...")
        print("Gracias por utilizar el sistema.")
        break

    
    else:

        print("")
        print("Opcion no valida.")
        print("Seleccione una opcion entre 1 y 4.")