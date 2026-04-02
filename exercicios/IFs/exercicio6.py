print("\n===Desconto de Compra===")
nome = input("Digite o nome do cliente: ")
valor_compra = float(input("Digite o valor da compra (€): "))
if valor_compra <= 200:
    percentagem = 0.10  
elif valor_compra <= 500:
    percentagem = 0.15  
else:
    percentagem = 0.20  
valor_desconto = valor_compra * percentagem
total_pagar = valor_compra - valor_desconto
print(f"\nNome: {nome}")
print(f"Compra: {valor_compra:.2f}€")
print(f"Desconto: {valor_desconto:.2f}€")
print(f"Total a pagar: {total_pagar:.2f}€\n")
