print("\n===Processamento de requisição===")
metodo = input("Digite o método (GET/POST): ").upper()
conteudo = input("Digite o conteúdo da requisição (pode deixar vazio): ")
match metodo:
    case "GET":
        print("Requisição GET recebida\n")
    case "POST":
        if conteudo: 
            print("Requisição POST com dados válidos\n")
        else:
            print("Requisição POST sem dados\n")
    case _:
        print("Método não suportado\n")