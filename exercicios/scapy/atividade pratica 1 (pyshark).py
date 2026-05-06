import pyshark

INTERFACE = "wlan0"
REDE = "192.168.1.0/24"  

def analisa_pacote(pacote):
    try:
        protocolo = pacote.highest_layer
        origem = pacote.ip.src if hasattr(pacote, 'ip') else "N/A"
        destino = pacote.ip.dst if hasattr(pacote, 'ip') else "N/A"
        
        print(f"[{protocolo}] {origem} -> {destino}")
    except AttributeError:
        pass

def monitorizar_trafego(interface, total_pacotes):
    print(f"\n--- Monitorizando tráfego em {interface} ({total_pacotes} pacotes) ---")
    
    captura = pyshark.LiveCapture(interface=interface)
    
    for i, pacote in enumerate(captura.sniff_continuously(packet_count=total_pacotes)):
        analisa_pacote(pacote)

if __name__ == "__main__":
    print(f"Iniciando monitorização na rede: {REDE}")
    
    try:
        monitorizar_trafego(INTERFACE, 50)
    except Exception as e:
        print(f"Erro: {e}")

