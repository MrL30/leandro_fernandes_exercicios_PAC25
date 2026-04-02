def dez_primeiros_primos():
    input("Pressione Enter para ver os 10 primeiros números primos...") 
    def eh_primo(num):
        if num < 2: return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0: return False
        return True
    cont, num = 0, 2
    while cont < 10:
        if eh_primo(num):
            print(num)
            cont += 1
        num += 1
dez_primeiros_primos()
