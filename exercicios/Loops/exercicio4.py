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