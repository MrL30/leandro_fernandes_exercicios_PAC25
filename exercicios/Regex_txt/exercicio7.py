import re
import os

diretorio = os.path.dirname(__file__)
caminho = os.path.join(diretorio, 'registos.txt')

try:
    with open(caminho, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    regex_nif = r'\b\d{9}\b'
    nifs_encontrados = re.findall(regex_nif, conteudo)

    print("--- NIFs Extraídos (9 dígitos) ---")
    for nif in nifs_encontrados:
        print(nif)

except FileNotFoundError:
    print("Erro: O ficheiro 'registos.txt' não foi encontrado.")