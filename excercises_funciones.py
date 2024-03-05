# Ejercicio 1: Concatenar Texto de Lista
# Crea una función que tome una lista de cadenas de texto y las concatene en una sola cadena, separadas por espacios.
# - Ejemplo de Entrada: ["Hola", "mundo", "Python"]
# - Salida esperada: "Hola mundo Python"

# def conctenate_strings(str_list):
#     concatenated_text = " ".join(str_list)
#     return concatenated_text


# str_list = ["Hola", "mundo", "estoy", "aprendiendo", "Python"]
# concatenated_text = conctenate_strings(str_list)
# print(concatenated_text)


# Ejercicio 2: Suma de Números hasta N
# Crea una función que sume todos los números hasta n usando un bucle while.

# - Ejemplo de Entrada: 5
# - Salida esperada: 15 (porque 1+2+3+4+5=15)

# def num_sum(n):
#     sum = 0
#     i = 0
#     while i <= n:
#         sum += i
#         i += 1
#     return sum

# n = 5
# resultado = num_sum(n)
# print(resultado)


# Ejercicio 3: Contar Ocurrencias en Lista (metodo count)
# Crea una función que cuente cuántas veces aparece un elemento en una lista.

# - Ejemplo de Entrada: Lista: [1, 2, 3, 2, 4, 2, 5], Elemento: 2
# - Salida esperada: 3 (el número 2 aparece 3 veces)


# def element_counter(num_list):
#     count = num_list.count()
#     return count


# num_list = [1, 2, 3, 2, 4, 2, 5]
# n = 2
# count = num_list.count(n)
# print(count)


# Ejercicio 4: Invertir Diccionario
# Crea una función que invierta las llaves y valores de un diccionario. Asume que los valores son únicos.

# - Ejemplo de Entrada: {'a': 1, 'b': 2, 'c': 3}
# - Salida esperada: {1: 'a', 2: 'b', 3: 'c'}


# def reverse_dict(my_dict):
#     new_dict = {}
#     for key, value in my_dict.items():
#         new_dict[value] = key
#     return new_dict


# my_dict = {1: 'a', 2: 'b', 3: 'c'}
# new_dict = reverse_dict(my_dict)
# print(new_dict)


# Ejercicio 5: Filtrar Números Pares
# Crea una función que devuelva solo los números pares de una lista.

# - Ejemplo de Entrada: [1, 2, 3, 4, 5, 6]
# - Salida esperada: [2, 4, 6]

# def even_num(my_list):
#     new_list = []
#     for int in my_list:
#         if int % 2 == 0:
#             new_list.append(int)
#     return new_list


# my_list = [1, 2, 3, 4, 5, 6]
# new_list = even_num(my_list)
# print(new_list)


# Ejercicio 6: Mayor y Menor en Lista
# Crea una función que encuentre el número mayor y menor en una lista y los devuelva.

# - Ejemplo de Entrada: [50, 20, 65, 30]
# - Salida esperada: (65, 20) (65 es el mayor, 20 es el menor)


# def higher_lower(num_list):
#     higher = lower = num_list[0]

#     for num in num_list:
#         if num > higher:
#             higher = num
#         elif num < lower:
#             lower = num
#     return higher, lower


# num_list = [40, 50, 95, 35]
# higher, lower = higher_lower(num_list)
# print(f"({higher},{lower})({higher} es el mayor, {lower} es el menor)")

# Ejercicio 7: Generar Diccionario de Conteos
# Crea una función que tome una cadena de texto y devuelva un diccionario con el conteo de cada carácter.

# - Ejemplo de Entrada: "banana"
# - Salida esperada: {'b': 1, 'a': 3, 'n': 2}

# def dict_counter(my_str):
#     new_dict = {}
#     for character in my_str:
#         if character in new_dict:
#             new_dict[character] += 1
#         else:
#             new_dict[character] = 1
#     return new_dict


# my_str = "banana"
# new_dict = dict_counter(my_str)
# print(new_dict)


# Ejercicio 9: Eliminar Duplicados de Lista
# Crea una función que elimine los elementos duplicados de una lista y devuelva una nueva lista.

# - Ejemplo de Entrada: [1, 2, 2, 3, 3, 3, 4]
# - Salida esperada: [1, 2, 3, 4]

# def duplicate_remover(my_list):
#     new_list = []
#     for num in my_list:
#         if num not in new_list:
#             new_list.append(num)
#     return new_list


# my_list = [1, 2, 2, 3, 3, 3, 4]
# new_list = duplicate_remover(my_list)
# print(new_list)

# Ejercicio 10: Contar Palabras
# Crea una función que tome una cadena de texto y devuelva un diccionario con el conteo de palabras que aparecen en ella.

# - Ejemplo de Entrada: "este es un texto este texto"
# - Salida esperada: {'este': 2, 'es': 1, 'un': 1, 'texto': 2}

# def dict_counter(my_str):
#     new_str = my_str.split(" ")
#     new_dict = {}
#     for word in new_str:
#         if word in new_dict:
#             new_dict[word] += 1
#         else:
#             new_dict[word] = 1
#     return new_dict


# my_str = "este es un texto este texto"
# new_dict = dict_counter(my_str)
# print(new_dict)
