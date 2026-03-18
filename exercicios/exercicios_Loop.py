# Exercício 1
def mostrar_pares_impares():
    input("Pressione Enter para ver os 30 primeiros números ímpares e pares...")
    pares = [i * 2 for i in range(30)]
    impares = [i * 2 + 1 for i in range(30)]
    print(f"Pares: {pares}")
    print(f"Ímpares: {impares}")
mostrar_pares_impares()

# Exercício 2
def verificar_paridade_dez():
    print("Introduza 10 números para verificar se são pares ou ímpares:")
    for i in range(1, 11):
        n = int(input(f"Número {i}: "))
        if n % 2 == 0:
            print(f"{n} é Par")
        else:
            print(f"{n} é Ímpar")
verificar_paridade_dez()

# Exercício 3
def media_dez_alunos():
    print("Introduza a nota de 10 alunos:") 
    soma = 0
    for i in range(1, 11):
        nota = float(input(f"Nota do aluno {i}: "))
        soma += nota
    print(f"Média da turma: {soma / 10}")
media_dez_alunos()

# Exercício 4
def verificar_primo():
    try:
        n = int(input("Introduza um número inteiro para verificar se é primo: "))
        if n < 2:
            print("Não é primo")
            return
        primo = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                primo = False
                break
        print(f"O número {n} {'é primo' if primo else 'não é primo'}")
    except ValueError:
        print("Erro: Por favor, introduza um número inteiro válido.")
verificar_primo()

# Exercício 5
def escrever_dez_mil():
    input("Pressione Enter para escrever os primeiros 10.000 números inteiros...") 
    for i in range(1, 10001):
        print(i)
escrever_dez_mil()

# Exercício 6
def dez_primeiros_primos():
    input("Pressione Enter para ver os 10 primeiros números primos...") 
    def eh_primo(num):
        if num < 2: return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0: return False
        return True
    cont, num = 0, 2
    while cont < 10:
        if eh_primo(num):
            print(num)
            cont += 1
        num += 1
dez_primeiros_primos()

# Exercício 7
def gerar_serie_dez():
    input("Pressione Enter para gerar a série de 10 em 10 até 1000...") 
    for i in range(10, 1001, 10):
        print(i, end=", " if i < 1000 else "\n")
gerar_serie_dez()

# Exercício 8
def duas_series_especificas():
    input("Pressione Enter para executar os dois ciclos das séries...") 
    print("Série 1:")
    for i in range(10, 1001, 10):
        print(i, end=" ")
    print("\nSérie 2:")
    for j in range(15, 996, 10):
        print(j, end=" ")
    print()
duas_series_especificas()

#Exericico 9
def solicitar_entre_um_e_cem():
    print("--- Exercício 9: Validação de Intervalo ---")
    while True:
        try:
            n = int(input("Introduza um valor entre 1 e 100: "))
            if 1 <= n <= 100:
                print(f"Sucesso! O número {n} é válido.")
                break 
            else:
                print("Valor fora do intervalo. Tente novamente.")
        except ValueError:
            print("Erro: Por favor, introduza um número inteiro.")
solicitar_entre_um_e_cem()

#Exercicio 10
def contar_divisores():
    print("--- Exercício 10: Contagem de Divisores ---")
    try:
        n = int(input("Introduza um número inteiro para analisar: "))
        divisores = 0
        for i in range(1, n + 1):
            if n % i == 0:
                divisores += 1
                print(f"Divisor encontrado: {i}") 
        print(f"O número {n} possui no total {divisores} divisores.")
    except ValueError:
        print("Erro: Introduza um número inteiro válido.")
contar_divisores()

# Exercício 11
def contar_divisores_input():
    n = int(input("Introduza um número para saber quantos divisores possui: ")) 
    divisores = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisores += 1
    print(f"O número {n} tem {divisores} divisores.") 
contar_divisores_input()

# Exercício 12
def operacoes_acumuladas_input():
    try:
        num_base = int(input("Introduza o número base para as operações: "))
        acumulador = 0
        limite = max(num_base, 2) 
        for i in range(1, limite):
            print(f"--- Iteração {i} ---")
            print(f"{num_base} + {i} = {num_base + i}")
            print(f"{num_base} - {i} = {num_base - i}")
            print(f"{num_base} * {i} = {num_base * i}")
            if i != 0:
                print(f"{num_base} / {i} = {num_base / i:.2f}")
            acumulador += 4
        print(f"Total de operações efetuadas: {acumulador}")
    except ValueError:
        print("Entrada inválida.")

# Exercício 13
def tabuada_simples():
    n = int(input("Introduza um número para ver a sua tabuada: "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}") 
tabuada_simples()

# Exercício 14
def todas_tabuadas_cem():
    input("Pressione Enter para ver todas as tabuadas de 1 a 100...") 
    for i in range(1, 101):
        print(f"--- Tabuada do {i} ---")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
todas_tabuadas_cem()

# Exercício 15
def tabela_ascii_vinte():
    input("Pressione Enter para iniciar a listagem ASCII...") 
    for i in range(256):
        print(f"Código {i}: {chr(i)}") 
        if (i + 1) % 20 == 0: 
            opcao = input("Deseja continuar? (s/n): ") 
            if opcao.lower() != 's':
                break
tabela_ascii_vinte()

# Exercício 16
def media_pares_validados():
    soma = 0
    cont = 0
    print("Introduza números pares entre 1 e 50:") 
    while cont < 30:
        n = int(input(f"Número {cont + 1}/30: "))
        if 1 <= n <= 50 and n % 2 == 0:
            soma += n
            cont += 1
        else:
            print("Número inválido. Deve ser par e estar entre 1 e 50.")
    print(f"Média dos 30 números: {soma / 30}") 
media_pares_validados()

# Exercício 17
def multiplos_especificos_mil():
    input("Pressione Enter para ver múltiplos de 5 que não são de 3 (1 a 1000)...") 
    for i in range(1, 1001):
        if i % 5 == 0 and i % 3 != 0: 
            print(i, end=" ")
    print()
multiplos_especificos_mil()

# Exercício 18
def contar_perfeitos_input():
    limite = int(input("Diga até que valor quer procurar números perfeitos: ")) 
    def eh_perfeito(n):
        soma = sum(i for i in range(1, n) if n % i == 0) 
        return soma == n 
    encontrados = 0
    for i in range(1, limite + 1):
        if eh_perfeito(i):
            print(f"Número perfeito encontrado: {i}")
            encontrados += 1
    print(f"Total de números perfeitos: {encontrados}")
contar_perfeitos_input()

# Exercício 19
def fibonacci_sessenta_input():
    input("Pressione Enter para ver os 60 primeiros números de Fibonacci...") 
    a, b = 1, 1
    for i in range(60):
        print(a, end=", ") 
        a, b = b, a + b 
    print()
fibonacci_sessenta_input()

# Teste Final 1 
def teste_final_analise():
    while True:
        val = int(input("Introduza um valor entre 1 e 30.000 para análise: ")) 
        if 1 <= val <= 30000: break
    def info_numero(n):
        divs = [i for i in range(1, n + 1) if n % i == 0] 
        eh_primo = len(divs) == 2
        eh_perfeito = sum(divs[:-1]) == n 
        return eh_primo, len(divs), eh_perfeito
    for i in range(val, 0, -1):
        primo, num_divs, perfeito = info_numero(i)
        print(f"Nº {i}: Primo: {primo}, Divisores: {num_divs}, Perfeito: {perfeito}")
        if (val - i + 1) % 10 == 0: 
            if input("Continuar? (s/n): ").lower() != 's': break 
teste_final_analise()

# Teste Final 2 
def calculadora_completa():
    print("--- MENU CALCULADORA ---") 
    while True:
        op = input("Operação (+, -, *, /, t=tabuada, s=sair): ") 
        if op == 's': break
        num = int(input("Introduza um valor (1 a 1000): "))
        if not (1 <= num <= 1000): continue
        if op == 't': 
            for i in range(1, num + 1):
                print(f"Tabuada do {i}:")
                for j in range(1, 11):
                    print(f"{i} x {j} = {i*j}")
                if i % 20 == 0: 
                    if input("Parar tabuada? (s/n): ") == 's': break
        else:
            n2 = float(input("Segundo número: "))
            if op == '+': print(f"Resultado: {num + n2}")
            elif op == '-': print(f"Resultado: {num - n2}")
            elif op == '*': print(f"Resultado: {num * n2}")
            elif op == '/': print(f"Resultado: {num / n2}")
calculadora_completa()

# Teste Final 3 
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