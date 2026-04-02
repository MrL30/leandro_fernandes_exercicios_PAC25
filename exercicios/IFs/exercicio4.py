print("\n===Calculadora de Saldo===")
saldo = float(input("Digite o saldo inicial: "))
cheque = float(input("Digite o valor do cheque: "))
if cheque <= saldo:
    saldo = saldo - cheque
    print(f"Cheque descontado, saldo: {saldo}\n")
else:
    print("O cheque não pode ser descontado: saldo insuficiente.\n")