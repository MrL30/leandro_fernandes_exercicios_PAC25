palavra = "algoritmo"
letras = list(palavra)

n = len(letras)
for i in range(n):
    for j in range(0, n - i - 1):
        if ord(letras[j]) > ord(letras[j + 1]):
            letras[j], letras[j + 1] = letras[j + 1], letras[j]

resultado = "".join(letras)
print(resultado)