import socket
import re
from datetime import datetime

VULNERABILIDADES_CONHECIDAS = {
    "vsFTPd 2.3.4": "Vulneravel a CVE-2011-2523",
    "OpenSSH 4.7p1": "Vulnerável a CVE-2008-1657 (Debian OpenSSL flaw)",
    "Apache/2.2.8": "Várias CVEs (CVE-2008-0005, CVE-2007-6421)",
    "ProFTPD 1.3.1": "Vulnerável a CVE-2008-4242",
    "mysql 5.0.51a": "Vulnerável a CVE-2008-2079 (criação de tabelas)",
    "Samba 3.0.20": "Vulnerável a CVE-2007-2447 (usermap_script)"
}

def identificar_vulnerabilidade(banner):
    for versao, descricao in VULNERABILIDADES_CONHECIDAS.items():
        if versao.lower() in banner.lower():
            return f"ALERTA: {descricao}"
    return "Nenhuma vulnerabilidade conhecida detetada"

def tentar_enviar_comando(sock, comando="HELP\r\n"):
    try:
        sock.send(comando.encode())
        sock.settimeout(1.0)
        resposta = sock.recv(1024)
        return resposta.decode('utf-8', errors='ignore').strip()
    except:
        return None

def grab_banner(ip, porta, timeout=2.0):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    
    try:
        s.connect((ip, porta))
        
        banner_bytes = s.recv(1024)
        banner = banner_bytes.decode('utf-8', errors='ignore').strip()
        
        if not banner or len(banner) < 5:
            if porta in [21, 25, 110]:
                resposta = tentar_enviar_comando(s, "HELP\r\n")
            elif porta == 22:
                resposta = None
            elif porta in [80, 443, 8080]:
                resposta = tentar_enviar_comando(s, "GET / HTTP/1.0\r\n\r\n")
            else:
                resposta = tentar_enviar_comando(s, "\n")
            
            if resposta:
                linhas = resposta.split('\n')
                for linha in linhas[:5]:
                    if 'server' in linha.lower() or '220' in linha or '220-' in linha:
                        banner = linha.strip()
                        break
                if not banner:
                    banner = f"Resposta após comando: {resposta[:100]}..."
        
        if banner:
            banner = re.sub(r'\s+', ' ', banner)
            banner = banner[:200]
            
            print(f"\n[+] PORTA {porta}")
            print(f"    Banner: {banner}")
            
            alerta = identificar_vulnerabilidade(banner)
            print(f"    {alerta}")
        else:
            print(f"\n[*] PORTA {porta}")
            print("    Sem banner disponível (serviço pode exigir autenticação prévia)")
            
    except socket.timeout:
        print(f"\n[-] PORTA {porta}: Timeout - serviço não respondeu")
    except ConnectionRefusedError:
        pass
    except Exception as e:
        print(f"\n[!] PORTA {porta}: Erro - {str(e)[:50]}")
    finally:
        s.close()

def main():
    print("="*60)
    print(" BANNER GRABBING - Identificação de Serviços")
    print("="*60)
    
    ip_alvo = input("\n[*] IP do alvo: ").strip()
    
    portas_alvo = [
        21, 22, 23, 25, 80, 110, 111, 135, 139, 143, 
        443, 445, 512, 513, 514, 993, 995, 1524, 2049, 
        3306, 3389, 5432, 5900, 5985, 5986, 6667, 8080, 8180
    ]
    
    print(f"\n[*] A testar {len(portas_alvo)} portas em {ip_alvo}")
    print("[*] A aguardar banners...\n")
    print("-" * 60)
    
    inicio = datetime.now()
    
    for porta in portas_alvo:
        grab_banner(ip_alvo, porta)
    
    tempo = (datetime.now() - inicio).total_seconds()
    
    print("\n" + "="*60)
    print(f"[+] Banner grabbing concluído em {tempo:.2f} segundos")
    print("="*60)

if __name__ == "__main__":
    main()
