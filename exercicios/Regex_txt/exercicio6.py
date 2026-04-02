import re
import os

diretorio = os.path.dirname(__file__)
caminho = os.path.join(diretorio, 'dados.txt')

try:
    with open(caminho, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    regex_pt = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.pt\b'
    emails_portugueses = re.findall(regex_pt, conteudo)

    print("--- Emails terminados em .pt ---")
    if emails_portugueses:
        for email in emails_portugueses:
            print(email)
    else:
        print("Nenhum email .pt encontrado.")

except FileNotFoundError:
    print("Erro: O ficheiro 'dados.txt' não foi encontrado.")