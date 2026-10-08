lista= ["mateo","elias","victoria","pavel","sofia"]

while  True:

    print("=== LISTA DE NOMBRES ====")

    print("1. agregar nombres")

    print("2. buscar nombre ")

    print("3. mostrar lista")

    print("4. salir  ")



    op_usuario=int(input("ingrese una opcion: "))

    if op_usuario == 1:
        print("eligio agregar nombres a la lista")

        agregado_lista=input("ingrese el nombre que desea agregar: ")

        lista.append(agregado_lista)

        print(lista)

    elif op_usuario == 2 :
        print("decidio buscar un nombre en la lista")

        buscado=input("ingrese el nombre que desea buscar:  ")

        if buscado in lista :
            print(" el  nombre que busco esta en la lista")
            
        else: 
            print("su nombre no se encuentra en la  lista")

    elif op_usuario == 3:
        print("eligio la opcion de mostrar la lista")

        print(lista)

    elif op_usuario == 4:
        print("decicio salir del programa")
        break