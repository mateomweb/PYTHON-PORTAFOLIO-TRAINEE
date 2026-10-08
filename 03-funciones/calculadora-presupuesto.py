print(" ===== CALCULADORA DE PRESUPUESTO ======")

ingreso=int(input("indique sus ingresos mensuales:  "))

gastos_comida=int(input("ingrese sus gastos en comida: "))

gastos_transporte=int(input("ingrese sus gastos en transporte: "))

gastos_entretenimiento=int(input("ingrese sus gastos en entretenimiento: "))

otros_gastos = int(input("ingrese los gastos que tiene en otras cosas: "))

def calcular_gastos(comida, transporte, entretenimiento, otros):
    total_sumado = comida + transporte + entretenimiento + otros
    return total_sumado

gastos_totales=calcular_gastos(gastos_comida, gastos_transporte, gastos_entretenimiento, otros_gastos)


def calcular_restante(ingresos , gastos):
    total_sobrado = ingresos -  gastos
    return total_sobrado
    

total = calcular_restante(ingreso, gastos_totales)

if total < 0:
    print("gastaste mas dinero de el que ingresaste")

elif total == 0:
    print("no te quedo dinero este mes. ")

else:
   print(f"su dinero restante es de: ${total}")

print(f"sus gastos totales son de: ${gastos_totales}")
