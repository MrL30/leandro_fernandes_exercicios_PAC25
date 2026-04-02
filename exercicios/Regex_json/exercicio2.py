import os
import json
import re

diretorio_atual = os.path.dirname(__file__)
caminho_ficheiro = os.path.join(diretorio_atual, 'dados.json')

def ler_dados(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        return json.load(f)

dados = ler_dados(caminho_ficheiro)

regex_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

print("--- Verificação de Emails ---")

for pessoa in dados:
    email = pessoa['email']
    nome = pessoa['nome']
    
    if re.match(regex_email, email):
        print(f"Válido: {nome} ({email})")
    else:
        print(f"Inválido: {nome} ({email})")