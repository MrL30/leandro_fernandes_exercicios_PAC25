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

#Exercicio 4
import ast
def tipo_dado(dado):
    match dado:
        case int():
            return "Número Inteiro"
        case float():
            return "Número Decimal"
        case str():
            if dado.isdigit():
                return "String Numérica"
            else:
                return "String Textual"
        case list():
            return "Lista"
        case _:
            return "Tipo Desconhecido"
print("\n=== Testes de Tipos de Dados ===")
entrada_user = input("Entrada -> ")
try:
    dado_convertido = ast.literal_eval(entrada_user)
except (ValueError, SyntaxError):
    dado_convertido = entrada_user
resultado = tipo_dado(dado_convertido)
print(f"Saída -> {resultado}\n")

#Exericicio 5
def analise_mns(mensagem):
    mns_limpa = mensagem.lower().strip()
    match mensagem:
        case n if "olá" in mns_limpa or "bom dia" in mns_limpa:
            return "Saudação\n"
        case n if mns_limpa.endswith("?"):
            return "Pergunta\n"
        case n if "tchau" in mns_limpa or "adeus" in mns_limpa:
            return "Despedida\n"
        case _:
            return "Mensagem Genérica"
print("\n===Análise da Mensagem===")
mns = input("Entrada -> ")
resultado = analise_mns(mns)
print(f"Saida -> {resultado}")

#Exercicio 6
print("\n===Estado do servidor===")
status = input("Digite o status (ok/erro): ").lower()
tempo_resposta = int(input("Digite o tempo de resposta (ms): "))
match status:
    case "erro":
        print("Servidor indisponível")
    case "ok":
        if tempo_resposta > 200:
            print("Servidor lento\n")
        else:
            print("Servidor ativo\n")
    case _:
        print("Estado desconhecido\n")

#Exercicio 7
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

#Exercicio 8
print("\n===Operação matemática===")
operacao = input("Escolha a operação (soma, subtrai, multiplica, divide): ").lower()
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
match operacao:
    case "soma":
        print(f"Resultado: {n1 + n2}\n")
    case "subtrai":
        print(f"Resultado: {n1 - n2}\n")
    case "multiplica":
        print(f"Resultado: {n1 * n2}\n")
    case "divide":
        if n2 != 0:
            print(f"Resultado: {n1 / n2}\n")
        else:
            print("Erro: Não é possível dividir por zero!\n")
    case _:
        print("Operação inválida.\n")

#Exericio 9 
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

#Exercicio 10
print("\n===Jogo: Pedra, Papel ou Tesoura===")
j1 = input("Jogador 1 (pedra, papel, tesoura): ").lower().strip()
j2 = input("Jogador 2 (pedra, papel, tesoura): ").lower().strip()
if j1 == j2:
    print("Empate!\n")
else:
    match (j1, j2):
        case ("pedra", "tesoura") | ("tesoura", "papel") | ("papel", "pedra"):
            print("Jogador 1 venceu!\n")
        case ("tesoura", "pedra") | ("papel", "tesoura") | ("pedra", "papel"):
            print("Jogador 2 venceu!\n")
        case _:
            print("Jogada inválida! Escolha entre pedra, papel ou tesoura.\n")