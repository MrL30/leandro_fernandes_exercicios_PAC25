def gerar_serie_dez():
    input("Pressione Enter para gerar a série de 10 em 10 até 1000...") 
    for i in range(10, 1001, 10):
        print(i, end=", " if i < 1000 else "\n")
gerar_serie_dez()
