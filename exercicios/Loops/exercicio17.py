def multiplos_especificos_mil():
    input("Pressione Enter para ver múltiplos de 5 que não são de 3 (1 a 1000)...") 
    for i in range(1, 1001):
        if i % 5 == 0 and i % 3 != 0: 
            print(i, end=" ")
    print()
multiplos_especificos_mil()