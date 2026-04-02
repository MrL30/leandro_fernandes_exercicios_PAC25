print("\n===Operação matemática===")
operacao = input("Escolha a operação (soma, subtrai, multiplica, divide): ").lower()
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
match operacao:
    case "soma":
        print(f"Resultado: {n1 + n2}\n")
    case "subtrai":
        print(f"Resultado: {n1 - n2}\n")
    case "multiplica":
        print(f"Resultado: {n1 * n2}\n")
    case "divide":
        if n2 != 0:
            print(f"Resultado: {n1 / n2}\n")
        else:
            print("Erro: Não é possível dividir por zero!\n")
    case _:
        print("Operação inválida.\n")
