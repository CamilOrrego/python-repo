monthly_incomes_expenses = [
    
]
# {"name":"my_expense_or_income", "amount": 1200, "category": "alimentos"}
categories = {"expenses": ["alimentos", "vivienda"],
              "incomes": ["salario", "freelance"]}
general_balance = 0


def add_record():
    global general_balance
    record_name = input("Ingrese el nombre del registro: ")
    record_name = record_name.lower()
    record_amount = int(input("Ingrese el monto del registro, positivo para ingreso o negativo para gasto: "))
    
    if record_amount == 0:
        return print("El monto del registro no puede ser igual a cero.")
    
    record_category = input("""
Ingrese la categoria del registro
(Ingreso: salario o freelance) (Gasto: alimentos o vivienda): """)
    record_category = record_category.lower()
    
    is_not_valid_category = record_category not in categories["expenses"] and record_category not in categories["incomes"]
    if is_not_valid_category:
        return print("Por favor ingrese una categoria valida.")
    
    new_record = {
        "name": record_name,
        "amount": record_amount,
        "category": record_category,
    }

    monthly_incomes_expenses.append(new_record)

    general_balance += record_amount
    print("Registro añadido exitosamente.")


def modify_record_amount():
    global general_balance
    record_name_to_modify = input(
        "Ingrese el nombre del registro que desea modificar: ")
    record_name_to_modify = record_name_to_modify.lower()
    record_to_modify = None
    for record in monthly_incomes_expenses:
        if record_name_to_modify == record["name"]:
            record_to_modify = record
    
    if not record_to_modify:
        return print("No existe un registro con ese nombre")
    
    if record_to_modify["amount"] > 0:
        return print("El registro no se puede modificar porque no es un gasto.")  
          
    new_amount = int(input("Ingrese el nuevo monto: "))
    old_record_amount = record_to_modify["amount"]
    record_to_modify["amount"] = new_amount
    
    difference = abs(old_record_amount) - abs(new_amount)
    general_balance += difference
    print("El registro se ha modificado con exito")
    print(general_balance)

def show_records_summary():
    global general_balance
    print()
    print("------------ Resumen de registros ------------")
    print()

    food_records = []
    for record in monthly_incomes_expenses:
        if record["category"] == "alimentos":
            food_records.append(record["amount"])
            print(f"Alimentos: {record['name']} = {record['amount']}")
        
    total_food_amounts = 0
    for record in food_records:
        total_food_amounts += record
    
    print("El total gastado en la categoria alimentos es: ", total_food_amounts)
    
    housing_records = []
    for record in monthly_incomes_expenses:
        if record["category"] == "vivienda":
            housing_records.append(record["amount"])
            print(f"Vivienda {record['name']} = {record['amount']}")
        
    total_housing_amounts = 0
    for record in housing_records:
        total_housing_amounts += record
    
    print("El total gastado en la categoria vivienda es: ", total_housing_amounts)
    
    salary_records = []
    for record in monthly_incomes_expenses:
        if record["category"] == "salario":
            salary_records.append(record["amount"])
            print(f"Salario: {record['name']} = {record['amount']}")
        
    total_salary_amounts = 0
    for record in salary_records:
        total_salary_amounts += record
    
    print("El total ingresado en la categoria salario es: ", total_salary_amounts)
    
    freelance_records = []
    for record in monthly_incomes_expenses:
        if record["category"] == "freelance":
            freelance_records.append(record["amount"])
            print(f"freelance: {record['name']} = {record['amount']}")
        
    total_freelance_amounts = 0
    for record in freelance_records:
        total_freelance_amounts += record
    
    print("El total ingresado en la categoria freelance es: ", total_freelance_amounts)
        
    print("Su balance general es: ", general_balance)      
    
def show_general_balance():
    global general_balance
    print(general_balance)
    if general_balance > 0:
        print("Tu balance es positivo. ¡Buen manejo de tus finanzas!")
    else:
        print("Tu balance es negativo. Considera revisar tus gastos.")
        
            

def show_menu():
    while True:
        print("""
Gestor de Presupuesto Personal

1. Añadir un ingreso o gasto
2. Modificar un registro
3. Visualizar todos los registros
4. Mostrar el balance general
5. Salir
""")
        try:
            action = int(input("Seleccione una opción: "))
            if action in [1, 2, 3, 4, 5]:
                
                if action == 5:
                    print("Hasta luego")
                    break
                
                if action == 1:
                    add_record()
                elif action == 2:
                    modify_record_amount()
                elif action == 3:
                    show_records_summary()
                elif action == 4:
                    show_general_balance()
            else:
                print("Acción inválida")
                    
        except ValueError:
            print("Error de tipo")



def main():
    show_menu()
main()
