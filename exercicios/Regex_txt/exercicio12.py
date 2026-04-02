import re
import os

diretorio = os.path.dirname(__file__)
caminho_entrada = os.path.join(diretorio, 'registos.txt')
caminho_saida = os.path.join(diretorio, 'resumo.txt')

try:
    with open(caminho_entrada, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    with open(caminho_saida, 'w', encoding='utf-8') as f_out:
        for linha in linhas:
            if not linha.strip(): continue

            nome = re.search(r'Nome: ([^|]+)', linha).group(1).strip()
            nif = re.search(r'NIF: (\d{9})', linha).group(1).strip()
            data = re.search(r'\d{2}/\d{2}/\d{4}', linha).group(0)
            cp = re.search(r'\d{4}-\d{3}', linha).group(0)
            
            site_busca = re.search(r'https?://(?:www\.)?([^|\s\n]+)', linha)
            dominio = site_busca.group(1).strip() if site_busca else ""

            f_out.write(f"{nome} | {nif} | {data} | {cp} | {dominio}\n")

    print(f"Sucesso! O ficheiro '{caminho_saida}' foi gerado.")

except FileNotFoundError:
    print("Erro: O ficheiro 'registos.txt' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")