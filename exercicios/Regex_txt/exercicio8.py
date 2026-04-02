import re
import os

diretorio = os.path.dirname(__file__)
caminho = os.path.join(diretorio, 'registos.txt')

try:
    with open(caminho, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    regex_data = r'\d{2}/\d{2}/\d{4}'
    datas_encontradas = re.findall(regex_data, conteudo)

    print("--- Datas Extraídas (DD/MM/AAAA) ---")
    for data in datas_encontradas:
        print(data)

except FileNotFoundError:
    print("Erro: O ficheiro 'registos.txt' não foi encontrado.")