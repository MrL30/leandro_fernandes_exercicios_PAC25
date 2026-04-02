import re
import os
from datetime import datetime

diretorio = os.path.dirname(__file__)
caminho = os.path.join(diretorio, 'registos.txt')

try:
    with open(caminho, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    print("--- Registos com data anterior a 2025 ---")
    print("-" * 45)

    for linha in linhas:
        if not linha.strip(): continue
        busca_data = re.search(r'(\d{2})/(\d{2})/(\d{4})', linha)
        
        if busca_data:
            data_str = busca_data.group(0) 
            
            data_objeto = datetime.strptime(data_str, "%d/%m/%Y")
            
            if data_objeto.year < 2025:
                nome = re.search(r'Nome: ([^|]+)', linha).group(1).strip()
                print(f"{nome} | Data: {data_str} (Anterior a 2025)")

except FileNotFoundError:
    print("Erro: O ficheiro 'registos.txt' não foi encontrado.")