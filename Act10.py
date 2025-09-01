
def equivalente(horas, minutos, segundos):
    total_segundos = horas * 3600 + minutos * 60 + segundos
    return total_segundos

def main():
    cont = 0
    while cont < 2:
        horas = int(input("Ingrese las horas: "))
        minutos = int(input("Ingrese los minutos: "))
        segundos = int(input("Ingrese los segundos: "))
        cont += 1
        total_segundos = equivalente(horas, minutos, segundos)
        print(f"El tiempo equivalente en segundos es: {total_segundos} segundos")


main()
