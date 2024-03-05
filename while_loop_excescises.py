# Ejercicio 1: Potencia de dos hasta un limite.
# Imprime las potencias de 2 hasta un 100.

# result = 2

# while result <= 100:
#     print(result)
#     result *= 2


# Ejercicio 2: Longitud de un número
# Calcula la longitud de un número entero dado en una variable externa (cuántos dígitos tiene).

# num = 12345
# digits = 0

# while digits < len(str(num)):
#     digits += 1

# print(digits)


# Ejercicio 3: Patrón de asteriscos inverso
# Imprime un patrón de asteriscos en orden inverso, comenzando con n asteriscos y disminuyendo a 1.

# asterisks = 5

# while asterisks >= 1:
#     print(f"*" * (asterisks))
#     asterisks -= 1


# Ejercicio 4: Juego de multiplicar
# Pregunta al usuario el resultado de multiplicar dos números aleatorios (creados por ti) hasta que responda correctamente.

# from random import randint


# while True:

#     num_1 = randint(0, 10)
#     num_2 = randint(0, 10)

#     product = num_1 * num_2

#     answer = int(input(f"Cuanto es {num_1} multiplicado por {num_2}?: "))

#     if product == answer:
#         print("correcto!")

#     else:
#         print("Incorrecto!")
#         break

# Ejercicio 5: Contador de palabras
# Dado el siguiente string, cuenta cuántas palabras contiene.

my_string = "El Arzobispo de Constantinopla se quiere desarzobispoconstantinoplanizar, el desarzobispoconstantiplanizador que lo desarzobispoconstantinoplanice, buen desarzobispoconstantinoplanizador será."

counter = 0
new_string = my_string.split(" ")
while counter < len(new_string):
    counter += 1
print(counter)


# Ejercicio 6: Divisores de un número
# Imprime todos los divisores de un número n dado (crear variable externa).
