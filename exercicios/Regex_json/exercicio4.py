import os
import json
import re

diretorio_atual = os.path.dirname(__file__)
caminho_ficheiro = os.path.join(diretorio_atual, 'dados.json')

with open(caminho_ficheiro, 'r', encoding='utf-8') as f:
    dados = json.load(f)

regex_nif = r'^[123568]\d{8}$'

print(f"{'Nome':<15} | {'NIF':<12} | {'Estado'}")
print("-" * 40)

for pessoa in dados:
    nif = pessoa['nif']
    nome = pessoa['nome']
    
    if re.match(regex_nif, nif):
        estado = "Válido"
    else:
        estado = "Inválido"
        
    print(f"{nome:<15} | {nif:<12} | {estado}")