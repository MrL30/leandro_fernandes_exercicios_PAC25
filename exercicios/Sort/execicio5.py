palavras = ["banana", "bola", "abacaxi", "arroz", "uva", "urso"]
grupos = {}

# Agrupamento
for p in palavras:
    inicial = p[0]
    if inicial not in grupos:
        grupos[inicial] = []
    grupos[inicial].append(p)

# Ordenação manual de cada grupo
for letra in grupos:
    lista = grupos[letra]
    n_lista = len(lista)
    for i in range(n_lista):
        for j in range(0, n_lista - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(grupos)