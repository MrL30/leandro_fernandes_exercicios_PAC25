print("\n===Classificação de produto===")
categoria = input("Digite a categoria (eletrônico/alimento): ").lower()
preco = float(input("Digite o preço do produto: "))
match categoria: 
    case "eletrônico":
        if preco > 1000:
            print("Produto de luxo\n")
        else:
            print("Produto comum\n")
    case "alimento":
        print("Produto alimentar\n") 
    case _:
        print("Categoria desconhecida\n")