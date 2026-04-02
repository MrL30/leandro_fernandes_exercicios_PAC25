frase = input("Introduza uma frase: ")
palavras = frase.split()
contagem_palavras = {}

for p in palavras:
    contagem_palavras[p] = contagem_palavras.get(p, 0) + 1

print(contagem_palavras)