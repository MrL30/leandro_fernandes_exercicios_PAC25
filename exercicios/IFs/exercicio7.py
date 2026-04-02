print("\n===Calcular a Média===")
n1 = float(input("Digite a Nota 1 (Peso 2): "))
n2 = float(input("Digite a Nota 2 (Peso 3): "))
n3 = float(input("Digite a Nota 3 (Peso 5): "))
media = (n1 * 2 + n2 * 3 + n3 * 5) / 10
print(f"Média: {media:.1f}")
if media >= 6:
    print("Aprovado\n")
else:
    print("Reprovado\n")
