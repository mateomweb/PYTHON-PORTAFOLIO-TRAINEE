print(" SISTEMA DE NOTAS")

nombre_estudiante=input("ingrese su nombre:  ")

nota_1=float(input("ingrese su primera nota:  "))

nota_2=float(input("ingrese su segunda nota:  "))

nota_3=float(input("ingrese su tercera nota:  "))


promedio_notas=(nota_1+nota_2+nota_3) / 3



if promedio_notas >= 6.0:
    print(f" nombre:{nombre_estudiante}")
    print(f"nota 1: {nota_1}")
    print(f"nota 2: {nota_2}")
    print(f"nota 3: {nota_3}") 

    print(f"promedio final es: {promedio_notas}")
    print("estado: aprobado ")
    print("excelente promedio")

elif promedio_notas >=5.0:
    print(f" nombre: {nombre_estudiante}")
    print(f"nota 1: {nota_1}")
    print(f"nota 2: {nota_2}")
    print(f"nota 3: {nota_3}") 

    print(f"promedio final es: {promedio_notas}")
    print("estado: aprobado ")
    print("buen promedio")

elif promedio_notas >=4.0:
    print(f" nombre: {nombre_estudiante}")
    print(f"nota 1: {nota_1}")
    print(f"nota 2: {nota_2}")
    print(f"nota 3: {nota_3}") 
    
    print(f"promedio final es: {promedio_notas}")
    print("estado: aprobado ")
    print(" un suficiente promedio")

else:
    print(f" nombre: {nombre_estudiante}")
    print(f"nota 1: {nota_1}")
    print(f"nota 2: {nota_2}")
    print(f"nota 3: {nota_3}") 
        
    print(f"promedio final es: {promedio_notas}")
    print("estado: reprobado ")
    print(" un insuficiente promedio")
    print("lamentablemente reprobaste.")