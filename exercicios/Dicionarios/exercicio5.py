palavra = input("Introduza uma palavra: ")
contagem = {}

for letra in palavra:
    contagem[letra] = contagem.get(letra, 0) + 1
print(contagem)