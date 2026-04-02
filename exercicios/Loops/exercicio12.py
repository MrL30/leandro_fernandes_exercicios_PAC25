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