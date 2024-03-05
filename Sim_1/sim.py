tables = []
for i in range(10):
    table = {"name": f"mesa {i+1}", "state": "disponible"}
    tables.append(table)
bookings = []


def reserve_table(name):
    available_tables = []
    for table in tables:
        if table["state"] == "disponible":
            available_tables.append(table)
    if not available_tables:
        print("No hay mesas disponibles.")
        return
    table_name = available_tables[0]["name"]
    for table in tables:
        if table["name"] == table_name:
            table["state"] = "reservada"
            bookings.append({"table": table_name, "name": name})
            print(f"Reserva realizada para {name} en {table_name}")
            break


def cancel_reservation(name):
    for booking in bookings:
        if booking["name"] == name:
            for table in tables:
                if table["name"] == booking["table"]:
                    table["state"] = "disponible"
                    bookings.remove(booking)
                    print(
                        f"Reserva cancelada para {name} en {booking['table']}")
                    break
            break
    else:
        print("No se encontró una reserva con ese nombre.")


def show_tables():
    available_tables = []
    for table in tables:
        if table["state"] == "disponible":
            available_tables.append(table)
    reserved_tables = []
    for booking in bookings:
        reserved_tables.append(booking)
    print("\nMesas disponibles:")
    for table in available_tables:
        print(table["name"])
    print("\nMesas reservadas:")
    for booking in reserved_tables:
        print(f"{booking['name']} - {booking['table']}")


def main():
    while True:
        print("\nMenú:")
        print("1. Realizar reserva")
        print("2. Cancelar reserva")
        print("3. Mostrar resumen de mesas")
        print("4. Salir")
        option = input("Seleccione una opción: ")
        if option == "1":
            name = input("Ingrese el nombre del cliente: ")
            reserve_table(name)
        elif option == "2":
            name = input(
                "Ingrese el nombre del cliente para cancelar la reserva: ")
            cancel_reservation(name)
        elif option == "3":
            show_tables()
        elif option == "4":
            print("Gracias por utilizar nuestro portal de reservas.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


main()
