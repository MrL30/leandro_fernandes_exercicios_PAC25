import ast
def tipo_dado(dado):
    match dado:
        case int():
            return "Número Inteiro"
        case float():
            return "Número Decimal"
        case str():
            if dado.isdigit():
                return "String Numérica"
            else:
                return "String Textual"
        case list():
            return "Lista"
        case _:
            return "Tipo Desconhecido"
print("\n=== Testes de Tipos de Dados ===")
entrada_user = input("Entrada -> ")
try:
    dado_convertido = ast.literal_eval(entrada_user)
except (ValueError, SyntaxError):
    dado_convertido = entrada_user
resultado = tipo_dado(dado_convertido)
print(f"Saída -> {resultado}\n")