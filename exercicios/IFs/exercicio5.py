print("\n===Ordem Crescente e Decrescente===")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
numeros = [n1, n2, n3]
numeros.sort()
print(f"Crescente: {numeros[0]}, {numeros[1]}, {numeros[2]}")
numeros.reverse()
print(f"Decrescente: {numeros[0]}, {numeros[1]}, {numeros[2]}")
