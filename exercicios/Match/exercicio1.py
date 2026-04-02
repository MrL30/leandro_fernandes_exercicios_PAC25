print("\nDias da semana")
print("\nDomingo (1)")
print("Segunda (2)")
print("Terça   (3)")
print("Quarta  (4)")
print("Quinta  (5)")
print("Sexta   (6)")
print("Sábado  (7)")
dia_semana = int(input("\nQue dia é hoje? (números de 1 a 7): "))
def tipo_dia():
    match dia_semana:
        case 2 | 3 | 4 | 5 | 6:
            return print("É um dia útil\n")
        case 1 | 7:
            return print("É fim-de-semana\n")
        case _:
            return print("Erro...\n")
tipo_dia()