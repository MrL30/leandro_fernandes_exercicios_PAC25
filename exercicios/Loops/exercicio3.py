def media_dez_alunos():
    print("Introduza a nota de 10 alunos:") 
    soma = 0
    for i in range(1, 11):
        nota = float(input(f"Nota do aluno {i}: "))
        soma += nota
    print(f"Média da turma: {soma / 10}")
media_dez_alunos()