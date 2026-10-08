tickets = [

]

id_tickets = 1

def registrar_tickets(tickets,id_tickets):

  nombre=input("ingrese su nombre: ")
  problema=input("describa su problema: ")
  prioridad=input("prioridad baja/media/alta: ")

  ticket ={
     "id" : id_tickets,
     "nombre": nombre,
     "problema": problema,
     "prioridad": prioridad,
     "estado": "pendiente"
  }
  tickets.append(ticket)

  id_tickets+=1

  return id_tickets




def mostrar_tickets(tickets):
   for ticket_actual in tickets:
   
    print("id :" ,ticket_actual["id"])
    print("nombre :" ,ticket_actual["nombre"])
    print("problema :" ,ticket_actual["problema"])
    print("prioridad :" ,ticket_actual["prioridad"])
    print("estado :" ,ticket_actual["estado"])
    


def buscar_tickets(tickets):

    buscador_id=int(input("ingrese el ID del ticket que desea buscar: "))

    for ticket in tickets:
       if ticket["id"] == buscador_id:
            return ticket



    return None



def resolver_ticket(tickets):

    usuario_ticket = int(input("ingrese el ID del ticket que quiere resolver: "))

    for ticket in tickets:
       if ticket["id"] == usuario_ticket:
          ticket["estado"] = "resuelto"
          return True


    return False

while True:

    print("=== SISTEMA DE SOPORTE DE TICKETS==")

    print("1. registrar ticket")
    print("2. Mostrar tickets")
    print("3. Buscar ticket")
    print("4. Resolver ticket")
    print("5. salir")

    op_usuario = int(input("ingrese su eleccion del menu: "))


    if op_usuario == 1 :

       id_tickets = registrar_tickets(tickets, id_tickets)


    elif op_usuario == 2:

       mostrar_tickets(tickets)


    elif op_usuario == 3:

       buscador = buscar_tickets(tickets)

       if  buscador is not None:
          print(buscador)

       else:
          print("ticket que ingreso no Encontrado.")


    elif op_usuario == 4:

       result = resolver_ticket(tickets)

       if result == True:

          print(" === TICKET RESULTO CORRECTAMENTE ===")

       else:
             print(" ==TICKET NO ENCONTRADO ====") 


    elif op_usuario == 5:
       print("==== SALIENDO DEL PROGRAMA....")
       break