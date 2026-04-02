import re
import os

diretorio = os.path.dirname(__file__)
caminho = os.path.join(diretorio, 'dados.txt')

def ler_ficheiro(caminho_file):
    try:
        with open(caminho_file, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            return conteudo
    except FileNotFoundError:
        print("Erro: O ficheiro 'dados.txt' não foi encontrado.")
        return ""

texto_completo = ler_ficheiro(caminho)

regex_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

def extrair_emails(texto):
    emails = re.findall(regex_email, texto)
    print("\n--- Emails Encontrados ---")
    for email in emails:
        print(email)
    return emails

lista_emails = extrair_emails(texto_completo)