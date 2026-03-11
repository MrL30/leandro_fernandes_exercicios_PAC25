import os

lista1 = []
lista2 = []
lista3 = []

def menu ():
    while True:
        print("1. Inserir dados")
        print("2. Listar dados")
        print("3. Guardar no ficheiro")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            inserir_dados()
        elif opcao == "2":
            listar_dados()
        elif opcao == "3":
            guardar_ficheiro()
        elif opcao == "4":
            print("Saindo do programa...")
            guardar_ficheiro()
            break
        else:
            print("Opção inválida. Tente novamente.")

    
    
def inserir_dados ():
    lista1.append (input("Nome: "))
    lista2.append (input("Idade: "))
    lista3.append (input("Morada: "))

       
def listar_dados ():
    if os.path.exists("dados.txt"):
        with open ("dados.txt", "r") as f:
            conteudo = f.read()
            print(conteudo)
    for i in range (len(lista1)):
        print (f"Nome: {lista1[i]}, Idade: {lista2[i]}, Morada: {lista3[i]}")
            
            
def guardar_ficheiro ():
    with open ("dados.txt", "w") as f:
        for i in range (len(lista1)):
            f.write (f"Nome: {lista1[i]}, Idade: {lista2[i]}, Morada: {lista3[i]}\n")
    print("Dados guardados no ficheiro 'dados.txt' com sucesso.")
            
def ler_ficheiro ():

    if os.path.exists("dados.txt"):
        with open("dados.txt", "r") as f:
            conteudo = f.read()
        
        
            


    

ler_ficheiro()
menu()