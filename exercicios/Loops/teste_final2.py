clientes = []
def gestao_clientes():
    while True:
        menu = input("\n1-Inserir, 2-Listar, 3-Busca Direta, 4-Sair: ") 
        if menu == '4': break
        if menu == '1':
            nome = input("Nome: ") 
            morada = input("Morada: ")
            nif = input("NIF: ") 
            compra = float(input("Valor da compra: ")) 
            if 100 <= compra <= 200: desc = 0.05 
            elif 200 < compra <= 500: desc = 0.10 
            elif compra > 500: desc = 0.15
            else: desc = 0
            divida = compra * (1 - desc) 
            clientes.append({"id": len(clientes)+1, "nome": nome, "divida": divida}) 
            print(f"Cliente inserido com ID {len(clientes)}")
        elif menu == '2':
            for c in clientes: 
                print(c)
                input("Pressione Enter para o próximo cliente...") 
        elif menu == '3':
            id_b = int(input("ID do cliente: ")) 
            encontrado = next((c for c in clientes if c["id"] == id_b), "Não encontrado")
            print(encontrado)
gestao_clientes()