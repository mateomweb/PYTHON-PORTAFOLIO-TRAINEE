print("ENCUENTRE EL NUMERO SECRETO")
numero_secreto = 67


numero_usuario=int(input("ingrese un numero: "))

while numero_usuario!=numero_secreto:
    

    if numero_usuario>numero_secreto:
        print("el numero que eligio es mayor que el numero secreto sigua intentando!!")

    elif numero_usuario<numero_secreto:
        print("el numero que eligio es menor sigua intentando!!")

    numero_usuario = int(input("ingrese un numero: "))
    
print("¡CORRECTO! Encontraste el número secreto")