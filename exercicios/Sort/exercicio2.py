palavras = ["Python", "inteligência", "Aprender", "dados", "Rede"]

n = len(palavras)
for i in range(n):
    for j in range(0, n - i - 1):
        if palavras[j].lower() < palavras[j + 1].lower():
            palavras[j], palavras[j + 1] = palavras[j + 1], palavras[j]

print(palavras)