print("\n===Estado do servidor===")
status = input("Digite o status (ok/erro): ").lower()
tempo_resposta = int(input("Digite o tempo de resposta (ms): "))
match status:
    case "erro":
        print("Servidor indisponível")
    case "ok":
        if tempo_resposta > 200:
            print("Servidor lento\n")
        else:
            print("Servidor ativo\n")
    case _:
        print("Estado desconhecido\n")
