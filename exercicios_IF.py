#Exercicio 1
def calculadora(total_segundos):
    if total_segundos >= 3600:
        horas = total_segundos // 3600 
        segundos_restantes = total_segundos % 3600
        if segundos_restantes >=60:
            minutos = segundos_restantes // 60
            segundos_finais = segundos_restantes % 60
            return f"Horas: {horas}, Minutos: {minutos}, Segundos: {segundos_finais}\n"
        else:
            return f"Horas: {horas}, Segundos: {segundos_restantes}\n"
    elif 3600 > total_segundos >= 60:
        minutos = total_segundos // 60
        segundos_restantes = total_segundos % 60
        return f"Minutos: {minutos}, Segundos: {segundos_restantes}\n"
    else:
        return f"Segundos: {total_segundos}\n"
print("\n===Conversor de segundos para horas===")
segundos = int(input("Número total de segundos: "))
resultado = calculadora(segundos)
print(resultado)

#Exercicio 2 
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

#Exercicio 3
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

#Exercicio 4
print("\n===Calculadora de Saldo===")
saldo = float(input("Digite o saldo inicial: "))
cheque = float(input("Digite o valor do cheque: "))
if cheque <= saldo:
    saldo = saldo - cheque
    print(f"Cheque descontado, saldo: {saldo}\n")
else:
    print("O cheque não pode ser descontado: saldo insuficiente.\n")

#Exercicio 5
print("\n===Ordem Crescente e Decrescente===")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
numeros = [n1, n2, n3]
numeros.sort()
print(f"Crescente: {numeros[0]}, {numeros[1]}, {numeros[2]}")
numeros.reverse()
print(f"Decrescente: {numeros[0]}, {numeros[1]}, {numeros[2]}")

#Exercicio 6
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

#Exercicio 7
print("\n===Calcular a Média===")
n1 = float(input("Digite a Nota 1 (Peso 2): "))
n2 = float(input("Digite a Nota 2 (Peso 3): "))
n3 = float(input("Digite a Nota 3 (Peso 5): "))
media = (n1 * 2 + n2 * 3 + n3 * 5) / 10
print(f"Média: {media:.1f}")
if media >= 6:
    print("Aprovado\n")
else:
    print("Reprovado\n")

#Exercicio 8
print("\n===Calcular a Média===")
notas = []
for i in range(1, 11):
    nota = float(input(f"Digite a nota do aluno {i} (0-20): "))
    notas.append(nota)
media = sum(notas) / len(notas)
acima_da_media = 0
for n in notas:
    if n >= media:
        acima_da_media += 1
print(f"\nMédia da turma: {media:.2f}")
print(f"Alunos com nota igual ou acima da média: {acima_da_media}\n")

#Exercicio 9
print("\n===Switch===")
mes = int(input("Digite um número de 1 a 12: "))
match mes:
    case 1: print("Janeiro\n")
    case 2: print("Fevereiro\n")
    case 3: print("Março\n")
    case 4: print("Abril\n")
    case 5: print("Maio\n")
    case 6: print("Junho\n")
    case 7: print("Julho\n")
    case 8: print("Agosto\n")
    case 9: print("Setembro\n")
    case 10: print("Outubro\n")
    case 11: print("Novembro\n")
    case 12: print("Dezembro\n")
    case _: 
        print("Erro: Número inválido! Digite um valor entre 1 e 12.\n")

#Exercicio 10
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