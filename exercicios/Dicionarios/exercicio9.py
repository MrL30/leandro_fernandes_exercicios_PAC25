notas = {
    'João': [7, 8, 9],
    'Maria': [10, 9, 8],
    'Ana': [6, 7, 8]
}

for nome, lista_notas in notas.items():
    media = sum(lista_notas) / len(lista_notas)
    print(f"{nome}: {media}")
