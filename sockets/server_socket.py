import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
porta = 12340

serverSocket.bind((host, porta))

serverSocket.listen(1)
print(f"Servidor ligado em {host}:{porta}")
print("A aguardar conexão de cliente...")

clientSocket, enderecoCliente = serverSocket.accept()
print(f"Conexão estabelecida em {enderecoCliente}")

while True:
    mensagem = clientSocket.recv(1024).decode()
    if not mensagem or mensagem.lower() == "sair":
        print("Cliente desconectou.")
        break
    print(f"Cliente: {mensagem}")
    resposta = input("Resposta (ou 'sair'): ")
    clientSocket.send(resposta.encode())
    if resposta.lower() == "sair":
        break
    

clientSocket.close()
serverSocket.close()

print("Conexões fechadas.")