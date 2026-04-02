import os

diretorio = os.path.dirname(__file__)
caminho = os.path.join(diretorio, 'dados.txt')

def ler_ficheiro(caminho_file):
    try:
        with open(caminho_file, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            print("\n--- Conteúdo do Ficheiro ---")
            print(f"\n{conteudo}")
            return conteudo
    except FileNotFoundError:
        print("Erro: O ficheiro 'dados.txt' não foi encontrado.")
        return ""

texto_completo = ler_ficheiro(caminho)