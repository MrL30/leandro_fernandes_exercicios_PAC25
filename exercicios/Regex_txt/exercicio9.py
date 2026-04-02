import re
import os

diretorio = os.path.dirname(__file__)
caminho = os.path.join(diretorio, 'registos.txt')

try:
    with open(caminho, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    regex_cp = r'\d{4}-\d{3}'
    cp_encontrados = re.findall(regex_cp, conteudo)

    print("--- Códigos Postais Extraídos ---")
    for cp in cp_encontrados:
        print(cp)

except FileNotFoundError:
    print("Erro: O ficheiro 'registos.txt' não foi encontrado.")