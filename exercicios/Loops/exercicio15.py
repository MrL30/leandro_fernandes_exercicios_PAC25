def tabela_ascii_vinte():
    input("Pressione Enter para iniciar a listagem ASCII...") 
    for i in range(256):
        print(f"Código {i}: {chr(i)}") 
        if (i + 1) % 20 == 0: 
            opcao = input("Deseja continuar? (s/n): ") 
            if opcao.lower() != 's':
                break
tabela_ascii_vinte()