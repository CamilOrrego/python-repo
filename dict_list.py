tables = [
    {"name": "mesa1", "state": "available"},
    {"name": "mesa3", "state": "booked"},
    {"name": "mesa4", "state": "available"},
    {"name": "mesa2", "state": "available"},
]

# Como cambiar el estado de una mesa en la lista de diccionarios
user_input = "2"
index_table_to_remove = None
for index, table in enumerate(tables):
    if table["name"] == f"mesa{user_input}":
        table["state"] = "booked"
# Como eliminar un diccionario de la lista
        index_table_to_remove = index
tables.pop(index_table_to_remove)   

print(tables)
