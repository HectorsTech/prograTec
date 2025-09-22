promedio = int(input("Cuantos numeros promediaras? : "))
print("Mete los ", promedio, " a promediar")
contador = 0
sumProm = 0

while contador < promedio:
    contador += 1
    numProm = float(input(""))
    sumProm = sumProm + numProm

sumProm = sumProm / promedio
print(sumProm)
