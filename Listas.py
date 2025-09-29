numCali = int(input("¿Cuántas calificaciones deseas capturar? "))
calificaciones = []

for x in range (0, numCali):
    calificacion = float(input(f"Calificación {x+1}: "))
    calificaciones.append(calificacion)
prom = 0
for x in range (0, numCali):
    prom = prom + calificaciones[x]
aprob = 0
for x in range(0, numCali):
    if calificaciones[x] >= 70:
        aprob += 1

prom = prom / numCali
maxCal = max(calificaciones)
minCal = min(calificaciones)

print("Lista de calificaciones: ", calificaciones)
print("Promedio: ", prom)
print("Calificación más alta: ", maxCal)
print("Calificación más baja: ", minCal)
print("Aprobados: ", aprob)
