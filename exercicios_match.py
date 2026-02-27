#Exercicio 1
print("\nDias da semana")
print("\nDomingo (1)")
print("Segunda (2)")
print("Terça   (3)")
print("Quarta  (4)")
print("Quinta  (5)")
print("Sexta   (6)")
print("Sábado  (7)")
dia_semana = int(input("\nQue dia é hoje? (números de 1 a 7): "))
def tipo_dia():
    match dia_semana:
        case 2 | 3 | 4 | 5 | 6:
            return print("É um dia útil\n")
        case 1 | 7:
            return print("É fim-de-semana\n")
        case _:
            return print("Erro...\n")
tipo_dia()

#Exercicio 2
print("\n===Calculo de avaliação da nota===")
nota = float(input("Nota final (De 0 a 100): "))
def classificacao():
    match nota:
        case n if n >= 90:
            return print("Classificação: Excelente\n")
        case n if 90 > n >= 70:
            return print("Classificação: Bom\n")
        case n if 70 > n >= 50:
            return print("Classificação: Suficiente\n")
        case _:
            return print("Classificação: Insuficiente\n")
classificacao()

#Exercicio 3
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