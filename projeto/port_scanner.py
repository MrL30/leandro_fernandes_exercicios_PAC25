import socket               # Comunicação de rede (criar ligações TCP às portas)
import threading            # Execução em paralelo (várias portas testadas ao mesmo tempo)
import time                 # Medir tempos (duração das ligações e do scan)
from datetime import datetime 

# Dicionário que associa um número de porta ao nome do serviço que costuma correr nela.
# É usado só para mostrar uma descrição legível quando uma porta está aberta.
SERVICOS_CONHECIDOS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 111: "RPC", 135: "RPC", 139: "NetBIOS-SSN",
    143: "IMAP", 443: "HTTPS", 445: "SMB", 993: "IMAPS", 995: "POP3S",
    3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL", 5900: "VNC",
    5985: "WinRM-HTTP", 5986: "WinRM-HTTPS", 6667: "IRC", 8080: "HTTP-Alt",
    1524: "Ingreslock", 2049: "NFS", 512: "exec", 513: "login", 514: "shell"
}

portas_abertas = []          # Lista partilhada onde se vão guardando as portas abertas encontradas
lock = threading.Lock()      # "Cadeado" para evitar que várias threads escrevam na lista ao mesmo tempo


def verifica_porta(ip, porta, timeout=1):
    """Testa uma única porta TCP num IP.
    Devolve True se a porta estiver aberta, False caso contrário."""
    try:
        # Cria um socket TCP/IPv4 (AF_INET = IPv4, SOCK_STREAM = TCP).
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)            # Define quanto tempo espera antes de desistir
        inicio = time.time()             # Marca o instante inicial (para medir o tempo de resposta)
        # connect_ex devolve 0 se a ligação teve sucesso (porta aberta); outro valor se falhou.
        resultado = s.connect_ex((ip, porta))
        tempo_resposta = time.time() - inicio  # Calcula quanto tempo a ligação demorou
        s.close()                        # Fecha o socket (liberta o recurso)
        
        if resultado == 0:               # 0 = porta aberta
            # Procura o nome do serviço no dicionário; se não existir, fica "Desconhecido".
            servico = SERVICOS_CONHECIDOS.get(porta, "Desconhecido")
            # Usa o lock para garantir que só uma thread escreve na lista de cada vez.
            with lock:
                portas_abertas.append((porta, servico, tempo_resposta))
            print(f"  [+] PORTA {porta} ABERTA - {servico} ({tempo_resposta:.3f}s)")
            return True
    except Exception:
        # Qualquer erro (host inacessível, etc.) é ignorado — considera-se a porta como não aberta.
        pass
    return False


def scan_portas_multithread(ip, portas, max_threads=50, timeout=1):
    """Testa várias portas em paralelo usando threads.
    Imprime os resultados e devolve a lista de portas abertas."""
    print(f"\n[+] A iniciar scanner em {ip} com {max_threads} threads...")
    print(f"[+] Timeout: {timeout}s | Total de portas: {len(portas)}")
    print("-" * 60)
    
    inicio_total = time.time()   # Marca o início do scan completo
    
    threads = []                 # Lista para guardar todas as threads criadas
    
    # Semáforo: limita quantas threads podem estar ativas ao mesmo tempo (no máximo max_threads).
    semaforo = threading.Semaphore(max_threads)
    
    def scanner_thread(porta):
        # "with semaforo" ocupa um lugar; se já houver max_threads ativas, espera pela sua vez.
        with semaforo:
            verifica_porta(ip, porta, timeout)
    
    # Cria e arranca uma thread para cada porta a testar.
    for porta in portas:
        t = threading.Thread(target=scanner_thread, args=(porta,))
        threads.append(t)
        t.start()                # Inicia a thread (começa a correr em paralelo)
    
    # Espera que todas as threads terminem antes de continuar.
    for t in threads:
        t.join()
    
    tempo_total = time.time() - inicio_total   # Tempo total do scan
    
    print("-" * 60)
    print(f"\n[+] SCAN CONCLUÍDO em {tempo_total:.2f} segundos")
    print(f"[+] Total de portas abertas: {len(portas_abertas)}")
    
    if portas_abertas:
        # Mostra uma tabela com as portas abertas, ordenadas por número de porta.
        print("\n[+] PORTAS ABERTAS (ordenadas):")
        print("    Porta | Serviço         | Tempo resposta")
        print("    " + "-" * 40)
        # sorted ordena os tuplos (porta, servico, tempo) pelo primeiro elemento (a porta).
        for porta, servico, tempo in sorted(portas_abertas):
            # {porta:5} alinha em 5 espaços; {servico:14} alinha em 14 espaços (formatação da tabela).
            print(f"    {porta:5} | {servico:14} | {tempo:.3f}s")
    else:
        print("\n[-] Nenhuma porta aberta encontrada.")
    
    return portas_abertas


def main():
    """Fluxo principal: pede dados ao utilizador, monta a lista de portas e corre o scan."""
    print("="*60)
    print(" PORT SCANNER - Com Multithreading")
    print("="*60)
    
    # Pede o IP do alvo; .strip() remove espaços no início/fim.
    ip_alvo = input("\n[*] IP do alvo: ").strip()
    
    # Vários grupos de portas organizados por categoria (apenas para legibilidade).
    portas_ftp = [21, 20]
    portas_ssh_telnet = [22, 23, 513, 514, 512]
    portas_windows = [135, 139, 445, 3389, 5985, 5986]
    portas_web = [80, 443, 8080, 990]
    portas_bd = [3306, 5432, 1524]
    portas_outros = [111, 2049, 5900, 6667, 25, 110, 143, 993, 995, 389, 636, 88]
    
    # Junta todos os grupos numa só lista, evitando portas repetidas.
    portas_a_testar = []
    for p in (portas_ftp + portas_ssh_telnet + portas_windows + 
              portas_web + portas_bd + portas_outros):
        if p not in portas_a_testar:   # Só adiciona se ainda não estiver na lista
            portas_a_testar.append(p)
    
    print(f"\n[*] Portas a testar: {len(portas_a_testar)}")
    print(f"[*] Lista: {sorted(portas_a_testar)}")
    
    # Pede o timeout; se o utilizador não escrever nada, usa 1 segundo por omissão.
    timeout_input = input("\n[*] Timeout em segundos (padrão=1): ").strip()
    timeout = float(timeout_input) if timeout_input else 1
    
    # Pede o número de threads; valor por omissão = 50.
    threads_input = input("[*] Número de threads (padrão=50): ").strip()
    max_threads = int(threads_input) if threads_input else 50
    
    # Pausa até o utilizador carregar ENTER (confirmação antes de começar).
    input("\n[!] Pressione ENTER para iniciar o scan...")
    
    # Executa o scan com os parâmetros recolhidos.
    portas_abertas = scan_portas_multithread(ip_alvo, portas_a_testar, max_threads, timeout)
    
    print("\n" + "="*60)
    print("[+] Scanner de portas concluído!")
    print("="*60)


# Variável definida ao nível do módulo (fora de qualquer função).
# Nota: a função main() cria a sua própria lista local com o mesmo nome, por isso esta
# versão global acaba por não ser usada durante a execução normal do programa.
portas_a_testar = [21, 22, 23, 512, 513, 514, 139, 445, 2049, 111, 3306, 5432, 80, 8180, 1524, 5900, 6667, 443, 990, 22, 993, 995, 3389, 135, 5985, 5986, 88, 389, 636]

# Corre main() apenas quando o ficheiro é executado diretamente (não quando é importado).
if __name__ == "__main__":
    main()