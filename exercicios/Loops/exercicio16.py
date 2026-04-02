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