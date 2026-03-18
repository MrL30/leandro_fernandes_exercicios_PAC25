#Exercicio 1
nome = input("O seu nome: ")
idade = input("A sua idade: ")
curso = input("O seu curso: ")
alunos = {"nome":nome, "idade":idade, "curso":curso}

print(f"\nnome: {alunos["nome"]}")
print(f"idade: {alunos["idade"]}")
print(f"curso: {alunos["curso"]}")

#Exercicio 2
carro = {'marca': 'Toyota', 'modelo': 'Corolla', 'ano': 2020}

print(f"\nModelo do carro: {carro['modelo']}\n")

#Exercicio 3
produto = {}
produto['nome'] = "Telemóvel"
produto['preço'] = 1500
produto['stock'] = 30
print(produto)

del produto['stock'] 
print(produto)

#Exercicio 4
utilizador = {'nome': 'Carlos', 'idade': 28}

if 'email' in utilizador:
    print(utilizador['email'])
else:
    print("Email não encontrado.")

#Exercicio 5
palavra = input("Introduza uma palavra: ")
contagem = {}

for letra in palavra:
    contagem[letra] = contagem.get(letra, 0) + 1
print(contagem)

#Exercicio 6
vendas = {'Janeiro': 1000, 'Fevereiro': 1500, 'Março': 1200}
total = sum(vendas.values())
print(f"Total de vendas: {total}")

#Exercicio 7
d = {'a': 1, 'b': 2, 'c': 3}
invertido = {valor: chave for chave, valor in d.items()}
print(invertido)

#Exercicio 8
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

d3 = d1 | d2 
print(d3)

#Exercicio 9
notas = {
    'João': [7, 8, 9],
    'Maria': [10, 9, 8],
    'Ana': [6, 7, 8]
}

for nome, lista_notas in notas.items():
    media = sum(lista_notas) / len(lista_notas)
    print(f"{nome}: {media:.1f}")

#Exercicio 10
frase = input("Introduza uma frase: ")
palavras = frase.split()
contagem_palavras = {}

for p in palavras:
    contagem_palavras[p] = contagem_palavras.get(p, 0) + 1

print(contagem_palavras)