print("\n===Jogo: Pedra, Papel ou Tesoura===")
j1 = input("Jogador 1 (pedra, papel, tesoura): ").lower().strip()
j2 = input("Jogador 2 (pedra, papel, tesoura): ").lower().strip()
if j1 == j2:
    print("Empate!\n")
else:
    match (j1, j2):
        case ("pedra", "tesoura") | ("tesoura", "papel") | ("papel", "pedra"):
            print("Jogador 1 venceu!\n")
        case ("tesoura", "pedra") | ("papel", "tesoura") | ("pedra", "papel"):
            print("Jogador 2 venceu!\n")
        case _:
            print("Jogada inválida! Escolha entre pedra, papel ou tesoura.\n")