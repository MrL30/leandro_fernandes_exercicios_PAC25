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