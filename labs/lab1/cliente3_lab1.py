import socket
import threading

HOST = "127.0.0.1"
PORTA = 12340

def receber_mensagens(sock):
    while True:
        try:
            dados = sock.recv(1024)
            if not dados:
                print("\n[SISTEMA] A conexão com o servidor foi encerrada.")
                sock.close()
                break 

            msg = dados.decode('utf-8')
            if msg == "NOME_REQ":
                sock.send(nome_user.encode('utf-8'))
            else:
                print(f"\n{msg}\n> ", end="")
        except:
            print("\n[!] Ocorreu um erro ou a conexão foi perdida.")
            sock.close()
            break

def iniciar_cliente():
    global nome_user
    nome_user = input("Nome de utilizador: ")
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((HOST, PORTA))
    except:
        print("[-] Erro: Servidor offline.")
        return

    threading.Thread(target=receber_mensagens, args=(sock,), daemon=True).start()

    print("[INFO] Digite 'sair' para sair ou '/status' para ver o seu risco.")
    
    while True:
        try:
            msg = input("> ")
            if msg.lower() == "sair": 
                sock.close()
                break
            sock.send(msg.encode('utf-8'))
        except EOFError:
            break

if __name__ == "__main__":
    iniciar_cliente()