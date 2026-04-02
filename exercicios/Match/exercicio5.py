def analise_mns(mensagem):
    mns_limpa = mensagem.lower().strip()
    match mensagem:
        case n if "olá" in mns_limpa or "bom dia" in mns_limpa:
            return "Saudação\n"
        case n if mns_limpa.endswith("?"):
            return "Pergunta\n"
        case n if "tchau" in mns_limpa or "adeus" in mns_limpa:
            return "Despedida\n"
        case _:
            return "Mensagem Genérica"
print("\n===Análise da Mensagem===")
mns = input("Entrada -> ")
resultado = analise_mns(mns)
print(f"Saida -> {resultado}")