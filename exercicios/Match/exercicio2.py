print("\n===Calculo de avaliação da nota===")
nota = float(input("Nota final (De 0 a 100): "))
def classificacao():
    match nota:
        case n if n >= 90:
            return print("Classificação: Excelente\n")
        case n if 90 > n >= 70:
            return print("Classificação: Bom\n")
        case n if 70 > n >= 50:
            return print("Classificação: Suficiente\n")
        case _:
            return print("Classificação: Insuficiente\n")
classificacao()