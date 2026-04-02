import re
import os

diretorio = os.path.dirname(__file__)
caminho = os.path.join(diretorio, 'dados.txt')

try:
    with open(caminho, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    nomes = re.findall(r'Nome: ([^,]+)', conteudo)

    print("--- Nomes Extraídos ---")
    for n in nomes:
        print(n.strip())

except FileNotFoundError:
    print(f"Erro: O ficheiro não foi encontrado em: {caminho}")