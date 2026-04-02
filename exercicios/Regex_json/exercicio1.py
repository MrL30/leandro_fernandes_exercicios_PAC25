import os
import json

diretorio_atual = os.path.dirname(__file__)
caminho_ficheiro = os.path.join(diretorio_atual, 'dados.json')

def ler_dados(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        return json.load(f)

dados = ler_dados(caminho_ficheiro)
print(dados)