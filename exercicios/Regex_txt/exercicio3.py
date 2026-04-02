import os
import re

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

regex_telemovel = r'\d(?:[\s-]?\d){8}'

def extrair_telemoveis(texto):
    telemoveis = re.findall(regex_telemovel, texto)
    print("\n--- Números de Telemóvel Encontrados ---")
    for tel in telemoveis:
        print(tel)
    return telemoveis

lista_telemoveis = extrair_telemoveis(texto_completo)