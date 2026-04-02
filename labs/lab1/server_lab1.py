import socket
import threading
import re
from datetime import datetime
import os

DIRETORIO_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_LOGS = os.path.join(DIRETORIO_BASE, "logs")

if not os.path.exists(PASTA_LOGS):
    os.makedirs(PASTA_LOGS)

CAMINHO_FICHEIRO_LOG = os.path.join(PASTA_LOGS, "logs_gdpr.txt")
CAMINHO_FICHEIRO_AUDITORIA = os.path.join(PASTA_LOGS, "auditoria_scores.txt")

HOST = "127.0.0.1"
PORTA = 12340

clientes = {}
reputacao_utilizadores = {}

def transmitir_mensagem(mensagem, cliente_remetente):
    for cliente in list(clientes.keys()):
        if cliente != cliente_remetente:
            try:
                cliente.send(mensagem)
            except:
                remover_cliente(cliente)

def remover_cliente(cliente):
    if cliente in clientes:
        identidade = clientes[cliente]
        print(f"[-] Conexão perdida com: {identidade}")
        del clientes[cliente]
        cliente.close()

        msg_saida = f"O utilizador {identidade} saiu do chat."
        transmitir_mensagem(msg_saida.encode('utf-8'), cliente)

def lidar_cliente(cliente_socket, endereco):
    try:
        cliente_socket.send("NOME_REQ".encode('utf-8'))
        nome = cliente_socket.recv(1024).decode('utf-8')
        identidade_completa = f"{nome} ({endereco[0]})"
        clientes[cliente_socket] = identidade_completa
        
        print(f"[+] Nova conexão detetada: {identidade_completa}")
        transmitir_mensagem(f"[+] {nome} entrou na sala!".encode('utf-8'), cliente_socket)
    except:
        print(f"[-] Falha no handshake inicial com {endereco}")
        cliente_socket.close()
        return
    
    while True:
        try:
            mensagem = cliente_socket.recv(1024)
            if mensagem:
                mensagem_texto = mensagem.decode('utf-8')
                
                if mensagem_texto == "/status":
                    risco = reputacao_utilizadores.get(identidade_completa, 0)
                    cliente_socket.send(f"[SISTEMA] O teu score de risco atual é: {risco}".encode('utf-8'))
                    continue

                viola_gdpr = auditar_mensagem(mensagem_texto, identidade_completa)
                
                if reputacao_utilizadores.get(identidade_completa, 0) > 100:
                    aviso_ban = "[SISTEMA] Foste banido do servidor por violações de segurança repetidas."
                    cliente_socket.send(aviso_ban.encode('utf-8'))
                    transmitir_mensagem(f"[SISTEMA] {nome} foi banido do servidor.".encode('utf-8'), cliente_socket)
                    remover_cliente(cliente_socket)
                    break

                if viola_gdpr:
                    alerta = "[SISTEMA] ALERTA GDPR: A sua mensagem foi bloqueada por conter dados pessoais sensíveis."
                    cliente_socket.send(alerta.encode('utf-8'))
                else:
                    mensagem_final = f"{nome}: {mensagem_texto}"
                    print(f"[{identidade_completa}] enviou: {mensagem_texto}")
                    transmitir_mensagem(mensagem_final.encode('utf-8'), cliente_socket)
            else:
                remover_cliente(cliente_socket)
                break
        except:
            remover_cliente(cliente_socket)
            break

def auditar_mensagem(mensagem, identidade):
    padrao_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    padrao_telefone = r'\b\d{9}\b' 
    padrao_nome = r'(?i)(?:meu nome(?: real)? é|chamo[- ]me)\s+([A-Z][a-zÀ-ÿ]+(?:\s+[A-Z][a-zÀ-ÿ]+)*)'
    padrao_senha = r'(?i)(?:minha (?:senha|password|palavra[- ]passe).*? é)\s+([^\s]+)'
    
    gatilhos_es = [r'urgente', r'imediato', r'clica aqui', r'ganhaste', r'promoção', r'oferta']
    
    encontrou_gdpr = False
    dados_detetados = []
    infracoes_es = []
    score_risco = 0

    emails_apanhados = re.findall(padrao_email, mensagem)
    if emails_apanhados:
        encontrou_gdpr = True
        dados_detetados.append(f"Emails: {emails_apanhados}")

    telefones_apanhados = re.findall(padrao_telefone, mensagem)
    if telefones_apanhados:
        encontrou_gdpr = True
        dados_detetados.append(f"Telefones: {telefones_apanhados}")
    
    nomes_apanhados = re.findall(padrao_nome, mensagem)
    if nomes_apanhados:
        encontrou_gdpr = True
        dados_detetados.append(f"Nomes Reais: {nomes_apanhados}")

    senhas_apanhadas = re.findall(padrao_senha, mensagem)
    if senhas_apanhadas:
        encontrou_gdpr = True
        dados_detetados.append(f"Senhas Expostas: {senhas_apanhadas}")

    for gatilho in gatilhos_es:
        if re.search(gatilho, mensagem, re.IGNORECASE):
            infracoes_es.append(gatilho)
            score_risco += 20

    if identidade not in reputacao_utilizadores:
        reputacao_utilizadores[identidade] = 0
    reputacao_utilizadores[identidade] += score_risco

    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if encontrou_gdpr:
        registo_gdpr = f"[{agora}] ALVO: {identidade} | DADOS: {', '.join(dados_detetados)} | MSG ORIGINAL: '{mensagem}'\n"
        with open(CAMINHO_FICHEIRO_LOG, "a", encoding="utf-8") as ficheiro_log:
            ficheiro_log.write(registo_gdpr)
        print(f"[!] VIOLAÇÃO GDPR DETETADA de {identidade}. Registado no log.")

    if score_risco > 0:
        motivos = [f"Gatilho ES: {g}" for g in infracoes_es]
        registo_auditoria = f"[{agora}] USER: {identidade} | SCORE ADICIONADO: {score_risco} | TOTAL: {reputacao_utilizadores[identidade]} | MOTIVOS: MSG ORIGINAL: '{mensagem}' {', '.join(motivos)}\n"
        with open(CAMINHO_FICHEIRO_AUDITORIA, "a", encoding="utf-8") as ficheiro_auditoria:
            ficheiro_auditoria.write(registo_auditoria)

    return encontrou_gdpr

def iniciar_servidor():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORTA))
    server_socket.listen()

    print(f"[*] Servidor a escutar em {HOST}:{PORTA}...")

    while True:
        cliente_socket, endereco = server_socket.accept()
        thread_cliente = threading.Thread(target=lidar_cliente, args=(cliente_socket, endereco))
        thread_cliente.start()

if __name__ == "__main__":
    iniciar_servidor()