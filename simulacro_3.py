def convertir_temperatura(temperatura, unidad_objetivo):
    if unidad_objetivo.upper() == 'C':
        temperatura_convertida = (temperatura * (9/5)) + 32
        unidad_convertida = 'Fahrenheit'
    elif unidad_objetivo.upper() == 'F':
        temperatura_convertida = (temperatura - 32) * (5/9)
        unidad_convertida = 'Celsius'
    else:
        print("Unidad de temperatura no reconocida. Por favor, ingrese 'C' para Celsius o 'F' para Fahrenheit.")
        return None
    return temperatura_convertida, unidad_convertida


def main():
    temperatura = float(input("Introduce la temperatura: "))
    unidad_original = input(
        "Introduce la unidad original (C para Celsius, F para Fahrenheit): ")

    resultado = convertir_temperatura(temperatura, unidad_original)
    if resultado is not None:
        temperatura_convertida, unidad_convertida = resultado
        print(
            f"La temperatura convertida es {temperatura_convertida} {unidad_convertida}.")
    else:
        print("No se pudo realizar la conversión. Por favor, verifica la unidad de temperatura ingresada.")


if __name__ == "__main__":
    main()
