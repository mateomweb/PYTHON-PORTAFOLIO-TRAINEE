notas = []


def agregar_notas(notas):
    nota = float(input("ingrese una nota: "))

    if nota < 1.0 or nota > 7.0:
        return "nota ingresada invalida"

    else:
        notas.append(nota)
        return "nota ingresada correctamente"


def mostrar_notas(notas):

    if len(notas) == 0:
        return "No ahi notas registradas"

    for nota in notas:
        print(f"Nota: {nota}")

    return "Fin de las notas"







def calcular_notas(notas):

    if len(notas) == 0:
        return "no ha ingresado ninguna nota"

    total = 0

    for nota in notas:
        total += nota
    promedio = total / len(notas)

    return promedio





def contador_notas(notas):
    if len(notas) == 0:
        return "no ahi notas ingresadas"


    contador_aprobadas = 0
    contador_desaprobadas = 0
    for nota in notas:
        if nota >= 4.0:
            contador_aprobadas += 1

        else:
            contador_desaprobadas += 1

    return f"notas aprobadas {contador_aprobadas} y de desaprobadas {contador_desaprobadas}"





while True:
    print("==== gestor de notas ===")

    print("1. agregar notas")
    print("2. mostrar notas")
    print("3. calcular notas")
    print("4. contar notas aprobadas y reprobadas")
    print("5. salir")

    op_usuario = int(input("ingrese una eleccion del menu: "))

    if op_usuario == 1:
        print("eligio agregar una nota")

        resultado = agregar_notas(notas)

        print(resultado)

    elif op_usuario == 2:
        print("eligio mostrar las notas")

        resultado = mostrar_notas(notas)

        print(resultado)

    elif op_usuario == 3:

        print("eligio calcular notas ")

        resultado =  calcular_notas(notas)

        print(resultado )

    elif op_usuario == 4:
        print("eligio contar notas aprobadas y reprobadas.")

        resultado = contador_notas(notas)
        print(resultado)

    elif op_usuario == 5:
        print("eligio salir del programa")
        break

    else:
        print("eleccion eligida invalida.")
