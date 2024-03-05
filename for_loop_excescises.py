# # Ejercicio 1: Impresión de números impares
# # Imprime todos los números impares del 1 al 20.

for i in range(1, 21):
    if i % 2 != 0:
        print(i)

# # Ejercicio 2: Suma de números negativos
# # Dada una lista de números que incluye tanto positivos como negativos, calcula la suma de todos los números negativos.

num_list = [1, 2, 3, 4, -4, -3, -2, -1]
negatives_sum = 0
a = 0

for i in num_list:
    if num_list[a] < 0:
        negatives_sum = num_list[a] + negatives_sum
    a += 1

print(negatives_sum)


# # Ejercicio 3: Multiplicación de elementos en una lista
# # Dada una lista de números definidos por ti, calcula el producto de todos los números utilizando un bucle for.

num_list = [1, 2, 3, 4, 5]
multi = 1

for i in num_list:
    multi *= i
print(multi)


# # Ejercicio 4: Concatenación de cadenas
# # Dada una lista de cadenas (strings) definida por ti, concaténalas todas en una sola cadena utilizando un bucle for.

str_list = ["hello ", "world ", "python!"]
chain = ""

for i in str_list:
    chain += i


# # Ejercicio 5: Contar elementos específicos. Hacer metodo count.
# # Dada una lista de numeros o de cadenas, cuenta cuántas veces aparece un elemento en la lista.

list_num = [3, 2, 3, 4, 3, 6, 3, 8, 3, 10]
item = 3


def count(list, item):
    count = 0
    a = 0
    for item in list_num:
        if list[a] == item:
            count += 1
    a += 1
    return count


print(f"el elemento {item} aparece {count(list_num, item)} veces")

# # Ejercicio 6: Filtrar divisibles
# # Dada una lista de números, imprime solo aquellos que son divisibles por un número n definido por ti en una variable externa.

list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
div_in = 2
num = 0

for num in list_num:
    if num % div_in == 0:
        print(num)


# # Ejercicio 7: Crear una lista de tuplas
# # Utilizando un bucle for, crea una lista de tuplas donde el primer elemento sea el índice y el segundo elemento sea el valor cuadrado del índice. El tamaño es de tu eleccion.

tuple_list = []
size = 10

for i in range(size):
    tuple = (i, i**2)
    tuple_list.append(tuple)
print("tuple list:", tuple_list)


# # Ejercicio 8: Intersección de listas
# # Dados dos listas, utiliza un bucle for para encontrar los elementos comunes a ambas listas.

first_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
second_list = [2, 4, 6, 8, 10, 23, 45, 67]
common_items = []

for item1 in first_list:
    for item2 in second_list:
        if item1 == item2:
            if item1 not in common_items:
                common_items.append(item1)
print("Common items:", common_items)


# # Ejercicio 9: Patrón de números
# # Imprime el siguiente patrón de números utilizando bucles for. Cada línea debe contener números del 1 al número de línea (inclusive).

# # 1
# # 12
# # 123
# # 1234
# # 12345

lines_amount = 5

for i in range(1, lines_amount + 1):
    for n in range(1, i + 1):
        print(n, end="")
    print()

# # # Ejercicio 10: Eliminar duplicados
# # # Dada la siguiente lista, utiliza un bucle for para eliminar los elementos duplicados y conservar una lista con elementos únicos.

# # lista_strings = ["manzana", "banana", "cereza", "manzana", "durazno", "plátano", "cereza", "manzana", "durazno", "banana"]

fruits_list = ["manzana", "banana", "cereza", "manzana",
               "durazno", "plátano", "cereza", "manzana", "durazno", "banana"]
new_list = []

for str in fruits_list:
    if str not in new_list:
        new_list.append(str)

print(new_list)


# # # Ejercicio 11: Factorial de un numero
# # # Calcula el factorial de un número n (crear variable n) utilizando un bucle for.

n = 5
f = 1

for i in range(1, n + 1):
    f *= i
print(f)

# # # Ejercicio 12: Números Fibonacci
# # # Genera e imprime los primeros n números de la secuencia Fibonacci.
# # ## Secuencia Fibonnacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

n = 10
fibonacci = [0, 1]

for i in range(2, n):
    next_number = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(next_number)

for number in fibonacci:
    print(number, end=" ")

# # Ejercicio 13: Tablas de multiplicar
# # Imprime las tablas de multiplicar del 1 al 10 utilizando bucles for anidados.

for i in range(1, 11):
    for number in range(1, 11):
        product = i * number
        print(f"{i} * {number} = {product}")
print()
