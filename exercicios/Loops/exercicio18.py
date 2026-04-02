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