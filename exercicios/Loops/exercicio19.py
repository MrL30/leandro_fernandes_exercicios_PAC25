def bonacci_sessenta_input():
    input("Pressione Enter para ver os 60 primeiros números de bonacci...") 
    a, b = 1, 1
    for i in range(60):
        print(a, end=", ") 
        a, b = b, a + b 
    print()
bonacci_sessenta_input()