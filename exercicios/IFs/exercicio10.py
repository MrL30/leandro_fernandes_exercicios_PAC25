print("\n===Loop===")
pares = 0
impares = 0
for i in range(1, 11):
    num = int(input(f"Digite o {i}º número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"\nPares: {pares}")
print(f"Ímpares: {impares}\n")