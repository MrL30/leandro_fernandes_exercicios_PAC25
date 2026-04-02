import os
import json
import re

diretorio_atual = os.path.dirname(__file__)
caminho_ficheiro = os.path.join(diretorio_atual, 'dados.json')

with open(caminho_ficheiro, 'r', encoding='utf-8') as f:
    dados = json.load(f)

regex_dominio = r'https?://(?:www\.)?([^/]+)'

print(f"{'nome':<15} | {'dominio extraido'}")
print("-" * 35)

for pessoa in dados:
    site = pessoa['site']
    nome = pessoa['nome']
    
    resultado = re.search(regex_dominio, site)
    
    if resultado:
        dominio = resultado.group(1) 
        print(f"{nome:<15} | {dominio}")