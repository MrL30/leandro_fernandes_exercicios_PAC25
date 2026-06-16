import subprocess
import sys
import re

def get_my_ip():
    try:
        resultado = subprocess.run(["ip", "-4", "addr", "show"], capture_output=True, text=True, check=True)
        padrao_ip = r'inet (\d+\.\d+\.\d+\.\d+)/\d+'
        matches = re.findall(padrao_ip, resultado.stdout)

        for ip in matches:
            if not ip.startswith('127.'):
                return ip
        return None

    except Exception as e:
        print(f"Erro ao obter o IP: {e}", file=sys.stderr)
        return None

def scan_with_nbtscan(rede):
    try:
        comando = ["nbtscan", "-r", rede]
        resultado = subprocess.run(comando, capture_output=True, text=True, timeout=10)
        return resultado.stdout

    except FileNotFoundError:
        return None

    except subprocess.TimeoutExpired:
        print("[-] nbtscan demorou muito tempo")
        return None

def scan_with_arp_scan(rede):
    try:
        comando = ["arp-scan", "--localnet"]
        resultado = subprocess.run(comando, capture_output=True, text=True, timeout=15)

        linhas_validas = []
        for linha in resultado.stdout.split('\n'):
            if re.match(r'\d+\.\d+\.\d+\.\d+\s+[0-9a-fA-F:]{17}', linha):
                linhas_validas.append(linha)
        return '\n'.join(linhas_validas)

    except FileNotFoundError:
        print("[-] arp-scan não instalado. Instalar com: sudo apt install arp-scan")
        return None

    except subprocess.TimeoutExpired:
        print("[-] arp-scan demorou muito tempo: Timeout")
        return None

def main():
    print("\n" + "="*60)
    print(" NETWORK SCANNER")
    print("="*60)

    meu_ip = get_my_ip()
    if not meu_ip:
        print("\n[!] Não foi possível determinar o IP da máquina. Rede padrão: 10.0.2.0/24")
        rede = "10.0.2.0/24"
    else:
        print(f"\n[+] O IP da máquina foi detectado: {meu_ip}")
        partes_ip = meu_ip.split('.')
        rede = f"{partes_ip[0]}.{partes_ip[1]}.{partes_ip[2]}.0/24"
        print(f"[+] A fazer um scan à rede: {rede}")

    print("-" * 60)

    resultados = None
    print("[*] A tentar o nbtscan...")
    resultados = scan_with_nbtscan(rede)

    if not resultados or resultados.strip() == "":
        print("[*] nbtscan sem resultados. A tentar arp-scan...")
        resultados = scan_with_arp_scan(rede)

    if resultados and resultados.strip():
        print("\n[+] Hosts encontrados:")
        print("-" * 60)

        linhas = resultados.split('\n')
        for linha in linhas:
            if linha.strip():

                if meu_ip and meu_ip in linha:
                    continue
                print(f"  {linha}")
    else:
        print("\n[-] Nenhum host encontrado. Verifique:")
        print("    1. A ligação à rede")
        print("    2. Instale nbtscan ou arp-scan: sudo apt install nbtscan arp-scan")

    print("-" * 60)
    print("\n[+] Scan concluído!\n")

if __name__ != "__main__":
    pass
else:
    main()
