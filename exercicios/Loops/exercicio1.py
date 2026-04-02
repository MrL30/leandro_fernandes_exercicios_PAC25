def mostrar_pares_impares():
    input("Pressione Enter para ver os 30 primeiros números ímpares e pares...")
    pares = [i * 2 for i in range(30)]
    impares = [i * 2 + 1 for i in range(30)]
    print(f"Pares: {pares}")
    print(f"Ímpares: {impares}")
mostrar_pares_impares()