print("\n===Calcular a Média===")
notas = []
for i in range(1, 11):
    nota = float(input(f"Digite a nota do aluno {i} (0-20): "))
    notas.append(nota)
media = sum(notas) / len(notas)
acima_da_media = 0
for n in notas:
    if n >= media:
        acima_da_media += 1
print(f"\nMédia da turma: {media:.2f}")
print(f"Alunos com nota igual ou acima da média: {acima_da_media}\n")