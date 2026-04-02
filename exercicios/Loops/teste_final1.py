import os

def limpar_tela():
    input("\nPressione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')

def analisar_numero(n):
    divisores = [i for i in range(1, n + 1) if n % i == 0]
    qtd_divisores = len(divisores)
    e_primo = "Sim" if qtd_divisores == 2 else "Não"
    
    # Número perfeito: soma dos divisores próprios (exclui o próprio n) é igual a n
    soma_proprios = sum(divisores[:-1])
    e_perfeito = "Sim" if soma_proprios == n and n != 0 else "Não"
    
    return e_primo, qtd_divisores, e_perfeito

def calculadora():
    print("\n--- CALCULADORA ---")
    try:
        n1 = float(input("Número 1: "))
        op = input("Operação (+, -, *, /, tab): ").lower()
        
        if op == 'tab':
            val = int(input("Até que valor deseja a tabuada (1-1000): "))
            if 1 <= val <= 1000:
                for i in range(1, val + 1):
                    print(f"{int(n1)} x {i} = {int(n1 * i)}")
                    if i % 20 == 0:
                        cont = input("Pausar (s/n)? ")
                        if cont.lower() == 's': break
            else:
                print("Valor fora do intervalo.")
        else:
            n2 = float(input("Número 2: "))
            if op == '+': print(f"Resultado: {n1 + n2}")
            elif op == '-': print(f"Resultado: {n1 - n2}")
            elif op == '*': print(f"Resultado: {n1 * n2}")
            elif op == '/': print(f"Resultado: {n1 / n2}" if n2 != 0 else "Erro: Divisão por zero")
    except ValueError:
        print("Entrada inválida.")

def main():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Analisar Números (Primos, Divisores, Perfeitos)")
        print("2. Calculadora / Tabuada")
        print("3. Sair")
        
        opcao = input("Escolha: ")
        
        if opcao == '1':
            try:
                limite = int(input("Introduza um valor (1 a 30.000): "))
                if 1 <= limite <= 30000:
                    contagem = 0
                    for i in range(limite, 0, -1):
                        primo, divs, perf = analisar_numero(i)
                        print(f"Num: {i:5} | Primo: {primo:3} | Divisores: {divs:3} | Perfeito: {perf}")
                        
                        contagem += 1
                        if contagem % 10 == 0:
                            parar = input("\nParar aqui? (s/n): ").lower()
                            if parar == 's': break
                else:
                    print("Valor fora do intervalo permitido.")
            except ValueError:
                print("Por favor, digite um número inteiro.")
            limpar_tela()

        elif opcao == '2':
            calculadora()
            limpar_tela()
            
        elif opcao == '3':
            print("A encerrar...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()