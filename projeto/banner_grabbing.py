import socket               # Comunicação de rede (ligações TCP aos serviços)
import re                   # Expressões regulares (aqui usado para limpar espaços do banner)
from datetime import datetime  # Datas/horas (para medir a duração total do processo)

# Dicionário que associa versões específicas de software a vulnerabilidades conhecidas (CVEs).
# Serve para, ao ler o "banner" de um serviço, avisar se a versão tem falhas documentadas.
VULNERABILIDADES_CONHECIDAS = {
    "vsFTPd 2.3.4": "Vulneravel a CVE-2011-2523",
    "OpenSSH_4.7p1": "Vulnerável a CVE-2008-1657 (Debian OpenSSL flaw)",
    "Apache/2.2.8": "Várias CVEs (CVE-2008-0005, CVE-2007-6421)",
    "ProFTPD 1.3.1": "Vulnerável a CVE-2008-4242",
    "5.0.51a": "Vulnerável a CVE-2008-2079 (MySQL, criação de tabelas)",
    "Samba 3.0.20": "Vulnerável a CVE-2007-2447 (usermap_script)"
}


def identificar_vulnerabilidade(banner):
    """Compara o texto do banner com as versões conhecidas e devolve um alerta se houver correspondência."""
    for versao, descricao in VULNERABILIDADES_CONHECIDAS.items():
        # .lower() em ambos para a comparação ignorar maiúsculas/minúsculas.
        if versao.lower() in banner.lower():
            return f"ALERTA: {descricao}"
    return "Nenhuma vulnerabilidade conhecida detetada"


def tentar_enviar_comando(sock, comando="HELP\r\n"):
    """Envia um comando ao serviço e devolve a resposta (texto), ou None se algo falhar.
    Útil quando o serviço não envia banner automaticamente e é preciso 'provocá-lo'."""
    try:
        sock.send(comando.encode())          # Converte o texto em bytes e envia
        sock.settimeout(1.0)                 # Espera no máximo 1 segundo pela resposta
        resposta = sock.recv(1024)           # Lê até 1024 bytes da resposta
        # Converte os bytes em texto, ignorando caracteres inválidos, e remove espaços das pontas.
        return resposta.decode('utf-8', errors='ignore').strip()
    except:
        return None


def grab_banner(ip, porta, timeout=2.0):
    """Liga-se a uma porta, tenta obter o banner do serviço e verifica vulnerabilidades conhecidas."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Socket TCP/IPv4
    s.settimeout(timeout)                                  # Tempo máximo de espera
    
    try:
        s.connect((ip, porta))               # Estabelece a ligação à porta
        
        try:
            # Muitos serviços (FTP, SSH, SMTP...) enviam logo um banner ao ligar.
            banner_bytes = s.recv(1024)
            banner = banner_bytes.decode('utf-8', errors='ignore').strip()
        except socket.timeout:
            banner = ""                      # Se nada chegar dentro do tempo, fica vazio
        
        # Se não houve banner (ou é muito curto), tenta provocar uma resposta com um comando.
        if not banner or len(banner) < 5:
            if porta in [21, 25, 110]:       # FTP, SMTP, POP3 -> respondem ao comando HELP
                resposta = tentar_enviar_comando(s, "HELP\r\n")
            elif porta == 22:                # SSH não responde bem a comandos em texto simples
                resposta = None
            elif porta in [80, 443, 8080]:   # Serviços web -> envia um pedido HTTP básico
                resposta = tentar_enviar_comando(s, "GET / HTTP/1.0\r\n\r\n")
            else:
                resposta = tentar_enviar_comando(s, "\n")  # Outros: tenta um simples newline
            
            if resposta:
                linhas = resposta.split('\n')
                # Procura nas primeiras 5 linhas algo relevante (cabeçalho 'Server' ou código 220 do FTP).
                for linha in linhas[:5]:
                    if 'server' in linha.lower() or '220' in linha or '220-' in linha:
                        banner = linha.strip()
                        break
                # Se não encontrou nada específico, usa os primeiros 100 caracteres da resposta.
                if not banner:
                    banner = f"Resposta após comando: {resposta[:100]}..."
        
        if banner:
            banner = re.sub(r'\s+', ' ', banner)   # Substitui sequências de espaços/quebras por um só espaço
            banner = banner[:200]                  # Limita o banner a 200 caracteres
            
            print(f"\n[+] PORTA {porta}")
            print(f"    Banner: {banner}")
            
            # Verifica e mostra se a versão detetada tem vulnerabilidades conhecidas.
            alerta = identificar_vulnerabilidade(banner)
            print(f"    {alerta}")
        else:
            print(f"\n[*] PORTA {porta}")
            print("    Sem banner disponível (serviço pode exigir autenticação prévia)")
            
    except socket.timeout:
        # O serviço não respondeu dentro do tempo definido.
        print(f"\n[-] PORTA {porta}: Timeout - serviço não respondeu")
    except ConnectionRefusedError:
        # A porta está fechada/recusou a ligação — ignora em silêncio.
        pass
    except Exception as e:
        # Qualquer outro erro: mostra os primeiros 50 caracteres da mensagem.
        print(f"\n[!] PORTA {porta}: Erro - {str(e)[:50]}")
    finally:
        s.close()                            # Fecha sempre o socket, haja erro ou não


def main():
    """Fluxo principal: pede o IP, percorre uma lista de portas e tenta obter o banner de cada uma."""
    print("="*60)
    print(" BANNER GRABBING - Identificação de Serviços")
    print("="*60)
    
    ip_alvo = input("\n[*] IP do alvo: ").strip()  # Pede o IP ao utilizador
    
    # Lista fixa de portas a inspecionar (serviços comuns em redes/servidores).
    portas_alvo = [
        21, 22, 23, 25, 80, 110, 111, 135, 139, 143, 
        443, 445, 512, 513, 514, 993, 995, 1524, 2049, 
        3306, 3389, 5432, 5900, 5985, 5986, 6667, 8080, 8180
    ]
    
    print(f"\n[*] A testar {len(portas_alvo)} portas em {ip_alvo}")
    print("[*] A aguardar banners...\n")
    print("-" * 60)
    
    inicio = datetime.now()                  # Marca o instante de início
    
    # Percorre as portas uma a uma (de forma sequencial, sem threads).
    for porta in portas_alvo:
        grab_banner(ip_alvo, porta)
    
    # Calcula o tempo total decorrido em segundos.
    tempo = (datetime.now() - inicio).total_seconds()
    
    print("\n" + "="*60)
    print(f"[+] Banner grabbing concluído em {tempo:.2f} segundos")
    print("="*60)


# Corre main() apenas quando o ficheiro é executado diretamente (não quando é importado).
if __name__ == "__main__":
    main()