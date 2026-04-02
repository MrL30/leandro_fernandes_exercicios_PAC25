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