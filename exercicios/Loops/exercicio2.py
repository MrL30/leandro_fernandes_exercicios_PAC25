def verificar_paridade_dez():
    print("Introduza 10 números para verificar se são pares ou ímpares:")
    for i in range(1, 11):
        n = int(input(f"Número {i}: "))
        if n % 2 == 0:
            print(f"{n} é Par")
        else:
            print(f"{n} é Ímpar")
verificar_paridade_dez()
