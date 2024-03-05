categories = {"expenses": ["alimentos", "vivienda"],
              "income": ["work", "freelance"]}
monthly_income_expenses = []
general_balance = 0


def display_menu():
    print("Gestor de Presupuesto Personal")
    print("1. Añadir un ingreso o gasto")
    print("2. Modificar un registro")
    print("3. Visualizar todos los registros")
    print("4. Mostrar el balance general")
    print("5. Salir")
    return int(input("Seleccione una opción: "))


def add_record():
    global monthly_income_expenses, general_balance
    name = input("Nombre del registro: ")
    amount = float(input("Cantidad: "))
    category = input("Categoría: ")
    if category in categories["expenses"]:
        amount = -amount
    monthly_income_expenses.append(
        {"name": name, "amount": amount, "category": category})
    general_balance += amount
    print("Registro añadido exitosamente.")


def modify_record():
    global monthly_income_expenses, general_balance
    name = input("Nombre del registro a modificar: ")
    for record in monthly_income_expenses:
        if record["name"] == name:
            print(
                f"Registro actual: {record['name']}, {record['amount']}, {record['category']}")
            new_amount = float(input("Nueva cantidad: "))
            if record["category"] in categories["expenses"]:
                new_amount = -new_amount
            difference = new_amount - record["amount"]
            record["amount"] = new_amount
            general_balance += difference
            print("Registro modificado exitosamente.")
            return
    print("Registro no encontrado.")


def view_records():
    print("Registros:")
    for record in monthly_income_expenses:
        print(f"{record['name']}, {record['amount']}, {record['category']}")
    print(f"Balance general: {general_balance}")


def display_balance_message():
    if general_balance > 0:
        print("Tu balance es positivo. ¡Buen manejo de tus finanzas!")
    elif general_balance < 0:
        print("Tu balance es negativo. Considera revisar tus gastos.")


def main():
    while True:
        option = display_menu()
        if option == 1:
            add_record()
        elif option == 2:
            modify_record()
        elif option == 3:
            view_records()
        elif option == 4:
            print(f"Balance general: {general_balance}")
            display_balance_message()
        elif option == 5:
            break
        else:
            print("Opción inválida. Intente de nuevo.")


main()
