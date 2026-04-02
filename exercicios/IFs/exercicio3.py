def ordenar_crescente(a, b):
    if a > b:
        return f"Crescente: {b}, {a}"
    else:
        return f"Crescente: {a}, {b}"
def ordenar_decrescente(a, b):
    if a > b:
        return f"Decrescente: {a}, {b}" 
    else:
        return f"Decrescente: {b}, {a}" 
print("\n===Ordenar números===")
num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
crescente = ordenar_crescente(num1, num2)
decrescente = ordenar_decrescente(num1, num2)
print(crescente)
print(decrescente)