def solicitar_datos():
    num_bombillas = int(input("Número de bombillas cambiadas: "))
    uso_diario = float(
        input("Uso diario promedio en horas (12 por defecto): ") or 12)
    costo_kWh = float(input("Costo por kWh (150 por defecto): ") or 150)
    return num_bombillas, uso_diario, costo_kWh


def calcular_ahorro(num_bombillas, uso_diario, costo_kWh):
    Vi = 230  # Voltaje de bombillas incandescentes
    Vl = 3.5  # Voltaje de bombillas LED
    Hd = 12  # Promedio de horas por día que la bombilla está encendida
    D = 365  # Cantidad de días que la bombilla está encendida
    CWh = costo_kWh  # Costo por kilovatio hora

    ahorro = (Vi - Vl) * Hd * D * CWh * num_bombillas
    return ahorro


def main():
    num_bombillas, uso_diario, costo_kWh = solicitar_datos()
    ahorro_anual = calcular_ahorro(num_bombillas, uso_diario, costo_kWh)
    print(f"Ahorro anual estimado: {ahorro_anual} kWh")


main()
