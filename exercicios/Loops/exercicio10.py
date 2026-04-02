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