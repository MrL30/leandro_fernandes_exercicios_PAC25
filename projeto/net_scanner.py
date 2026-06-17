import subprocess  # Permite executar comandos externos do sistema (ip, nbtscan, arp-scan)
import sys          # Acesso ao sistema; aqui usado para escrever no canal de erros (stderr)
import re           # Expressões regulares; usado para procurar padrões em texto (ex.: IPs)


def get_my_ip():
    """Descobre o endereço IPv4 da máquina (ignorando o loopback 127.x.x.x).
    Devolve o IP como string, ou None se não conseguir determinar."""
    try:
        # Executa "ip -4 addr show" e captura a saída como texto.
        # check=True faz lançar um erro se o comando falhar.
        resultado = subprocess.run(["ip", "-4", "addr", "show"], capture_output=True, text=True, check=True)

        # Padrão que procura linhas tipo "inet 192.168.1.5/24" e captura só o IP.
        padrao_ip = r'inet (\d+\.\d+\.\d+\.\d+)/\d+'
        # Devolve uma lista com todos os IPs encontrados na saída.
        matches = re.findall(padrao_ip, resultado.stdout)

        # Percorre os IPs e devolve o primeiro que NÃO seja loopback (127.x.x.x).
        for ip in matches:
            if not ip.startswith('127.'):
                return ip
        return None  # Nenhum IP válido encontrado

    except Exception as e:
        # Em caso de qualquer erro, escreve no stderr e devolve None.
        print(f"Erro ao obter o IP: {e}", file=sys.stderr)
        return None


def scan_with_nbtscan(rede):
    """Varre a rede com o nbtscan (procura nomes NetBIOS, típico de máquinas Windows).
    Devolve o texto da saída, ou None em caso de erro/timeout/programa em falta."""
    try:
        # Monta o comando "nbtscan -r <rede>".
        comando = ["nbtscan", "-r", rede]
        # Executa, captura a saída e cancela se demorar mais de 10 segundos.
        resultado = subprocess.run(comando, capture_output=True, text=True, timeout=10)
        return resultado.stdout

    except FileNotFoundError:
        # O nbtscan não está instalado no sistema.
        return None

    except subprocess.TimeoutExpired:
        # Ultrapassou os 10 segundos definidos.
        print("[-] nbtscan demorou muito tempo")
        return None


def scan_with_arp_scan(rede):
    """Varre a rede local com o arp-scan (descobre dispositivos via pedidos ARP: IP + MAC).
    Devolve apenas as linhas válidas (IP + endereço MAC), ou None em caso de erro."""
    try:
        # "--localnet" deteta a rede local automaticamente (o parâmetro 'rede' não é usado aqui).
        comando = ["arp-scan", "--localnet"]
        # Executa com timeout de 15 segundos.
        resultado = subprocess.run(comando, capture_output=True, text=True, timeout=15)

        linhas_validas = []
        # Percorre cada linha da saída.
        for linha in resultado.stdout.split('\n'):
            # Mantém só as linhas que começam por IP + espaços + MAC (ex.: 192.168.1.5  aa:bb:cc:dd:ee:ff).
            # [0-9a-fA-F:]{17} corresponde aos 17 caracteres de um endereço MAC.
            if re.match(r'\d+\.\d+\.\d+\.\d+\s+[0-9a-fA-F:]{17}', linha):
                linhas_validas.append(linha)
        # Junta as linhas válidas novamente com quebras de linha.
        return '\n'.join(linhas_validas)

    except FileNotFoundError:
        # O arp-scan não está instalado; mostra a forma de o instalar.
        print("[-] arp-scan não instalado. Instalar com: sudo apt install arp-scan")
        return None

    except subprocess.TimeoutExpired:
        # Ultrapassou os 15 segundos definidos.
        print("[-] arp-scan demorou muito tempo: Timeout")
        return None


def main():
    """Fluxo principal: deteta o IP/rede, faz o scan e mostra os hosts encontrados."""
    print("\n" + "="*60)
    print(" NETWORK SCANNER")
    print("="*60)

    # Tenta descobrir o IP da máquina.
    meu_ip = get_my_ip()
    if not meu_ip:
        # Se não conseguir, usa uma rede por omissão.
        print("\n[!] Não foi possível determinar o IP da máquina. Rede padrão: 10.0.2.0/24")
        rede = "10.0.2.0/24"
    else:
        # Se conseguir, constrói o endereço da sub-rede a partir do IP.
        print(f"\n[+] O IP da máquina foi detectado: {meu_ip}")
        partes_ip = meu_ip.split('.')  # Ex.: "192.168.1.5" -> ['192','168','1','5']
        # Usa os 3 primeiros blocos + ".0/24" -> ex.: "192.168.1.0/24" (toda a sub-rede).
        rede = f"{partes_ip[0]}.{partes_ip[1]}.{partes_ip[2]}.0/24"
        print(f"[+] A fazer um scan à rede: {rede}")

    print("-" * 60)

    resultados = None
    # Primeira tentativa: nbtscan.
    print("[*] A tentar o nbtscan...")
    resultados = scan_with_nbtscan(rede)

    # Se o nbtscan não devolver nada útil, recorre ao arp-scan (estratégia de fallback).
    if not resultados or resultados.strip() == "":
        print("[*] nbtscan sem resultados. A tentar arp-scan...")
        resultados = scan_with_arp_scan(rede)

    # Se houver resultados, mostra os hosts encontrados.
    if resultados and resultados.strip():
        print("\n[+] Hosts encontrados:")
        print("-" * 60)

        linhas = resultados.split('\n')
        for linha in linhas:
            if linha.strip():  # Ignora linhas vazias

                # Salta a própria máquina (não interessa listar o nosso IP).
                if meu_ip and meu_ip in linha:
                    continue
                print(f"  {linha}")  # Imprime o host com um pequeno avanço
    else:
        # Sugestões de diagnóstico de erro.
        print("\n[-] Nenhum host encontrado. Verifique:")
        print("    1. A ligação à rede")
        print("    2. Instale nbtscan ou arp-scan: sudo apt install nbtscan arp-scan")

    print("-" * 60)
    print("\n[+] Scan concluído!\n")


# __name__ vale "__main__" quando o ficheiro é executado diretamente,
# e tem outro valor se for importado como módulo.
if __name__ != "__main__":
    pass        # Se for importado, não faz nada.
else:
    main()      # Se for executado diretamente, corre o programa.