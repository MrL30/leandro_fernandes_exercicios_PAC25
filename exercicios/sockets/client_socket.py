import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
porta = 12340
clientSocket.connect((host, porta))
print("Ligado ao servidor!")

while True:
    mensagem = input("Mensagem ou 'sair': ")
    clientSocket.send(mensagem.encode())
    if mensagem.lower() == "sair":
        break
    resposta = clientSocket.recv(1024).decode()
    if not resposta or resposta == "sair":
        print("O servidor encerrou a conexão.")
        break
    print("Resposta do servidor:", resposta)

clientSocket.close()
print("Conexão fechada.")