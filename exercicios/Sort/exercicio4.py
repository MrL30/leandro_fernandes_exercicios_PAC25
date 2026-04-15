palavras = ["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]

def contar_minusculas(p):
    count = 0
    for char in p:
        if 'a' <= char <= 'z':
            count += 1
    return count

n = len(palavras)
for i in range(n):
    for j in range(0, n - i - 1):
        if contar_minusculas(palavras[j]) > contar_minusculas(palavras[j + 1]):
            palavras[j], palavras[j + 1] = palavras[j + 1], palavras[j]

print(palavras)