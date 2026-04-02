import re
import os

diretorio = os.path.dirname(__file__)
caminho_entrada = os.path.join(diretorio, 'dados.txt')
caminho_saida = os.path.join(diretorio, 'extraidos.txt')

try:
    with open(caminho_entrada, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    with open(caminho_saida, 'w', encoding='utf-8') as f_out:
        for linha in linhas:
            if not linha.strip():
                continue
            busca_nome = re.search(r'Nome: ([^,]+)', linha)
            busca_email = re.search(r'Email: ([^,]+)', linha)
            busca_tel = re.search(r'Telemóvel: (.+)', linha)
            if busca_nome and busca_email and busca_tel:
                nome = busca_nome.group(1).strip()
                email = busca_email.group(1).strip()
                tel = busca_tel.group(1).strip()
                f_out.write(f"{nome} | {email} | {tel}\n")
                print(f"Processado: {nome}")
            else:
                print(f"Linha ignorada por formato inválido: {linha.strip()}")

    print(f"\nConcluído! Verifica o ficheiro '{caminho_saida}'.")

except FileNotFoundError:
    print("Erro: Ficheiro 'dados.txt' não encontrado.")