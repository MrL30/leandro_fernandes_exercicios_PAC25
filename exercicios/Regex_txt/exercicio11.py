import re
import os

diretorio = os.path.dirname(__file__)
caminho = os.path.join(diretorio, 'registos.txt')

try:
    with open(caminho, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    regex_nif_pt = r'^[123568]\d{8}$'

    print("--- Validação de NIFs Portugueses ---")
    print("-" * 35)

    for linha in linhas:
        busca_nif = re.search(r'NIF: (\d+)', linha)
        
        if busca_nif:
            nif = busca_nif.group(1)
            if re.match(regex_nif_pt, nif):
                print(f"NIF {nif}: Válido")
            else:
                print(f"NIF {nif}: Inválido (Dígito inicial incorreto)")

except FileNotFoundError:
    print("Erro: O ficheiro 'registos.txt' não foi encontrado.")