def verificar_maior(a, b, c):
    if a >= b and a >= c:
        return f"Maior número: {a}"
    elif b >= a and b >= c:
        return f"Maior número: {b}"
    else:
        return f"Maior número: {c}"
def verificar_menor(a, b, c):
    if a <= b and a <= c:
        return f"Menor número: {a}"
    elif b <= a and b <= c:
        return f"Menor número: {b}"
    else:
        return f"Menor número: {c}"
print("\n===Maior e Menor número===")
num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
num3 = int(input("Terceiro número: "))
maior = verificar_maior(num1, num2, num3)
menor = verificar_menor(num1, num2, num3)
print(maior)
print(menor)