saldo_inicial = 1000000

def cajero_automatico(saldo_inicial):

    total=saldo_inicial-retiro_usuario

    if saldo_inicial >= retiro_usuario:
        return f"su retiro  fue de: {retiro_usuario}, y le sobro: {total}"

    else:
            return "saldo insuficiente"


while True:
    try:

        retiro_usuario=int(input("ingrese el retiro deseado: "))

        resultado = cajero_automatico(saldo_inicial)
        print(resultado)
        break
    except ValueError:
        print("porfavor ingrese numeros")
        continue



