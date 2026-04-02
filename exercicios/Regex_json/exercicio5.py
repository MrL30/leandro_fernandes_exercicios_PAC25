import os
import json
import re

diretorio_atual = os.path.dirname(__file__)
caminho_entrada = os.path.join(diretorio_atual, 'dados.json')
caminho_saida = os.path.join(diretorio_atual, 'dados_validos.json')

with open(caminho_entrada, 'r', encoding='utf-8') as f:
    dados = json.load(f)

regex_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
regex_nif = r'^[123568]\d{8}$'
regex_tel = r'^\d{9}$' 

registos_filtrados = []

for pessoa in dados:
    email_ok = bool(re.match(regex_email, pessoa['email']))
    nif_ok = bool(re.match(regex_nif, pessoa['nif']))
    tel_limpo = re.sub(r'[\s-]', '', pessoa['telemovel'])
    tel_ok = bool(re.match(regex_tel, tel_limpo))
    
    if email_ok and nif_ok and tel_ok:
        registos_filtrados.append(pessoa)
        print(f"{pessoa['nome']} adicionado aos válidos.")
    else:
        print(f"{pessoa['nome']} descartado (dados inválidos).")

with open(caminho_saida, 'w', encoding='utf-8') as f:
    json.dump(registos_filtrados, f, indent=4, ensure_ascii=False)

print(f"\nFicheiro '{caminho_saida}' criado com sucesso!")