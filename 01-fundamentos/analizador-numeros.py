print("=== USO DE BUCLES FOR Y WHILE ===")

while True:
    print("\n1. Ingresar números")
    print("2. Salir")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        print("\nEligió ingresar números")

        positivos = 0
        negativos = 0
        ceros = 0
        suma_total = 0

        ingresos_deseados = int(input("¿Cuántos números quiere ingresar?: "))

        for num in range(ingresos_deseados):
            numero = int(input("Ingrese un número: "))

            suma_total += numero

            if numero > 0:
                print("Su número es positivo")
                positivos += 1

            elif numero == 0:
                print("Su número es cero")
                ceros += 1

            else:
                print("Su número es negativo")
                negativos += 1

        print("\n=== RESUMEN ===")
        print(f"Cantidad de positivos: {positivos}")
        print(f"Cantidad de ceros: {ceros}")
        print(f"Cantidad de negativos: {negativos}")
        print(f"Suma total: {suma_total}")

    elif opcion == 2:
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida")