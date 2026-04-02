import os
import json

diretorio_atual = os.path.dirname(__file__)
caminho_entrada = os.path.join(diretorio_atual, 'dados.json')
caminho_txt = os.path.join(diretorio_atual, 'lista_contactos.txt')

with open(caminho_entrada, 'r', encoding='utf-8') as f:
    dados = json.load(f)

with open(caminho_txt, 'w', encoding='utf-8') as f:
    f.write("Lista de Contactos\n")
    f.write("-" * 30 + "\n")
    
    for pessoa in dados:
        nome = pessoa['nome']   
        email = pessoa['email'] 
        linha = f"Nome: {nome} | Email: {email}\n"
        f.write(linha)

print(f"Sucesso! O ficheiro '{caminho_txt}' foi gerado.")