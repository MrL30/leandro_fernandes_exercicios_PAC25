print("\n===Tipo de pedido===")
tipo = int(input("Pretende vender(1) ou comprar(2) (1/2): "))
valor = int(input("Preço do produto (em euros): "))
def tp(escolha):
    match escolha:
        case 1:
            return "venda"
        case 2:
            return "compra"
        case _:
            return print("Erro...")
resultado_tipo = tp(tipo)
escolha = {"tipo":resultado_tipo, "valor":valor}
print(f"A sua escolha: {escolha}")
print(f"Quer fazer uma {resultado_tipo} de {valor}€\n")