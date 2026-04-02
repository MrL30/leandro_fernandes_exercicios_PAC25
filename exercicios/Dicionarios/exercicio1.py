def inserir():
    nome = input("\nO seu nome: ")
    idade = input("A sua idade: ")
    curso = input("O seu curso: ")
    return nome, idade, curso

def criar_dicionario(nome, idade, curso):
    alunos = {"nome":nome, "idade":idade, "curso":curso}
    return alunos

def listar(dados_aluno):
    if not dados_aluno:
        print("\nNenhum aluno cadastrado!")
        return
    print(f"\nnome: {dados_aluno["nome"]}")
    print(f"idade: {dados_aluno["idade"]}")
    print(f"curso: {dados_aluno["curso"]}")

aluno_atual = None

def main():
    global aluno_atual
    try:
        escolha = int(input("\n1 Inserir\n2 Listar\n3 Sair\nEscolha: "))
    except ValueError:
        print("Escolha inválida, por favor digite um número...")
        return True
    if escolha == 1:
        n, i, c = inserir()
        aluno_atual = criar_dicionario(n, i, c)
        print("Cadastrado com sucesso!")
        return True
    elif escolha == 2:
        listar(aluno_atual)
        return True
    elif escolha == 3:
        return False
    else:
        print("Escolha inválida...")
        return True

loop = True
while loop:
    loop = main()