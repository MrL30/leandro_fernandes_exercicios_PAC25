def contar_divisores_input():
    n = int(input("Introduza um número para saber quantos divisores possui: ")) 
    divisores = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisores += 1
    print(f"O número {n} tem {divisores} divisores.") 
contar_divisores_input()
