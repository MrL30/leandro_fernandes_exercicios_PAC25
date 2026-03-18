import socket
import threading
import sys

HOST = "127.0.0.1"
PORTA = 12340

nome_utilizador = input("Introduza o seu nome de utilizador: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect((HOST, PORTA))
except:
    print("[-] Erro: Não foi possível contactar o servidor base.")
    sys.exit()

def receber_mensagens():
    while True:
        try:
            mensagem = client_socket.recv(1024).decode('utf-8')
            if mensagem == "NOME_REQ":
                client_socket.send(nome_utilizador.encode('utf-8'))
            else:
                print(f"\n{mensagem}")
        except:
            print("\n[-] Conexão com o servidor perdida.")
            client_socket.close()
            break

def escrever_mensagens():
    while True:
        try:
            mensagem = input("")
            if mensagem.lower() == 'sair' or mensagem.lower() == 'exit':
                print("[*] A desconectar do servidor...")
                client_socket.close()
                break
            client_socket.send(mensagem.encode('utf-8'))
        except EOFError:
            break

thread_rececao = threading.Thread(target=receber_mensagens)
thread_rececao.start()

escrever_mensagens()