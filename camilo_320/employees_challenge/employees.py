# 1
from random import randrange
from json import load

file_json = "employees.json"

with open(file_json, "r") as file:
    employees = load(file)

# 2

employees_lenght = len(employees)
employee_index = randrange(0, employees_lenght)
employee_salary_revision = employees[employee_index]


# 3
employee_increase = 0
employee_years_service = employee_salary_revision["years_of_service"]

if employee_years_service == 1:
    percentage_salary_increase = 0
elif employee_years_service == 2:
    percentage_salary_increase = 10
elif employee_years_service == 3:
    percentage_salary_increase = 30
elif employee_years_service > 3:
    percentage_salary_increase = 50


#  4
employee_salary = employee_salary_revision["base_salary"]
employee_years_service = employee_salary_revision["years_of_service"]

if employee_years_service == 1:
    employee_salary_increase = int(employee_salary)
elif employee_years_service == 2:
    employee_salary_increase = int(employee_salary) * 0.10 + int(
        employee_salary)
elif employee_years_service == 3:
    employee_salary_increase = int(employee_salary) * 0.30 + int(
        employee_salary)
elif employee_years_service > 3:
    employee_salary_increase = int(employee_salary) * 0.50 + int(
        employee_salary)

# 5
print(
    f"--- Incremento {employee_salary_revision['name']}. Departamento: {employee_salary_revision['department']} ---")
print(f"Id del usuario: {employee_salary_revision['id']}")
print(f"Nombre: {employee_salary_revision['name']}")
print(f"Departamento: {employee_salary_revision['department']}")
print(f"Años De Servicio: {employee_salary_revision['years_of_service']}")
print(f"Salario Original: {employee_salary_revision['base_salary']} USD/YEAR")
print(f"Incremento Aplicado: {percentage_salary_increase}%")
print(f"Nuevo Salario: {employee_salary_increase} USD/YEAR")

# 6
updated_employees = [
    f"id del usuario={employee_salary_revision['id']}, name={employee_salary_revision['name']}, department={employee_salary_revision['department']}, years_of_service={employee_salary_revision['years_of_service']}"]

updated_salary = updated_employees.append(
    f"new_salary={employee_salary_increase}")
print(updated_employees)
