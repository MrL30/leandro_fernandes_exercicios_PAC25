import re
import os

diretorio = os.path.dirname(__file__)
caminho = os.path.join(diretorio, 'registos.txt')

try:
    with open(caminho, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    regex_dominio = r'https?://(?:www\.)?([^|\s\n]+)'
    dominios = re.findall(regex_dominio, conteudo)

    print("--- Domínios Extraídos ---")
    for dom in dominios:
        print(dom.strip())

except FileNotFoundError:
    print("Erro: O ficheiro 'registos.txt' não foi encontrado.")