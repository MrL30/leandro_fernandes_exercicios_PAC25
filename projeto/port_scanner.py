import socket
import threading
import time
from datetime import datetime

SERVICOS_CONHECIDOS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 111: "RPC", 135: "RPC", 139: "NetBIOS-SSN",
    143: "IMAP", 443: "HTTPS", 445: "SMB", 993: "IMAPS", 995: "POP3S",
    3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL", 5900: "VNC",
    5985: "WinRM-HTTP", 5986: "WinRM-HTTPS", 6667: "IRC", 8080: "HTTP-Alt",
    1524: "Ingreslock", 2049: "NFS", 512: "exec", 513: "login", 514: "shell"
}

portas_abertas = []
lock = threading.Lock()

def verifica_porta(ip, porta, timeout=1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        inicio = time.time()
        resultado = s.connect_ex((ip, porta))
        tempo_resposta = time.time() - inicio
        s.close()
        
        if resultado == 0:
            servico = SERVICOS_CONHECIDOS.get(porta, "Desconhecido")
            with lock:
                portas_abertas.append((porta, servico, tempo_resposta))
            print(f"  [+] PORTA {porta} ABERTA - {servico} ({tempo_resposta:.3f}s)")
            return True
    except Exception:
        pass
    return False

def scan_portas_multithread(ip, portas, max_threads=50, timeout=1):
    print(f"\n[+] A iniciar scanner em {ip} com {max_threads} threads...")
    print(f"[+] Timeout: {timeout}s | Total de portas: {len(portas)}")
    print("-" * 60)
    
    inicio_total = time.time()
    
    threads = []
    
    semaforo = threading.Semaphore(max_threads)
    
    def scanner_thread(porta):
        with semaforo:
            verifica_porta(ip, porta, timeout)
    
    for porta in portas:
        t = threading.Thread(target=scanner_thread, args=(porta,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    tempo_total = time.time() - inicio_total
    
    print("-" * 60)
    print(f"\n[+] SCAN CONCLUÍDO em {tempo_total:.2f} segundos")
    print(f"[+] Total de portas abertas: {len(portas_abertas)}")
    
    if portas_abertas:
        print("\n[+] PORTAS ABERTAS (ordenadas):")
        print("    Porta | Serviço         | Tempo resposta")
        print("    " + "-" * 40)
        for porta, servico, tempo in sorted(portas_abertas):
            print(f"    {porta:5} | {servico:14} | {tempo:.3f}s")
    else:
        print("\n[-] Nenhuma porta aberta encontrada.")
    
    return portas_abertas

def main():
    print("="*60)
    print(" PORT SCANNER - Com Multithreading")
    print("="*60)
    
    ip_alvo = input("\n[*] IP do alvo: ").strip()
    
    portas_ftp = [21, 20]
    portas_ssh_telnet = [22, 23, 513, 514, 512]
    portas_windows = [135, 139, 445, 3389, 5985, 5986]
    portas_web = [80, 443, 8080, 990]
    portas_bd = [3306, 5432, 1524]
    portas_outros = [111, 2049, 5900, 6667, 25, 110, 143, 993, 995, 389, 636, 88]
    
    portas_a_testar = []
    for p in (portas_ftp + portas_ssh_telnet + portas_windows + 
              portas_web + portas_bd + portas_outros):
        if p not in portas_a_testar:
            portas_a_testar.append(p)
    
    print(f"\n[*] Portas a testar: {len(portas_a_testar)}")
    print(f"[*] Lista: {sorted(portas_a_testar)}")
    
    timeout_input = input("\n[*] Timeout em segundos (padrão=1): ").strip()
    timeout = float(timeout_input) if timeout_input else 1
    
    threads_input = input("[*] Número de threads (padrão=50): ").strip()
    max_threads = int(threads_input) if threads_input else 50
    
    input("\n[!] Pressione ENTER para iniciar o scan...")
    
    portas_abertas = scan_portas_multithread(ip_alvo, portas_a_testar, max_threads, timeout)
    
    print("\n" + "="*60)
    print("[+] Scanner de portas concluído!")
    print("="*60)

portas_a_testar = [21, 22, 23, 512, 513, 514, 139, 445, 2049, 111, 3306, 5432, 80, 8180, 1524, 5900, 6667, 443, 990, 22, 993, 995, 3389, 135, 5985, 5986, 88, 389, 636]

if __name__ == "__main__":
    main()
