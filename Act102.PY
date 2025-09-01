def areaRect(largo, ancho):
    area = largo * ancho
    return area
def perimetroRect(largo, ancho):
    perimetro = 2 * (largo + ancho)
    return perimetro
def main():
    largo = float(input("Ingrese el largo del rectángulo: "))
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    calculate = input("¿Desea calcular el área o el perímetro? (a/p): ").lower()
    if calculate == 'a':
        print(f"El área del rectángulo es: {areaRect(largo, ancho)}")
    elif calculate == 'p':
        print(f"El perímetro del rectángulo es: {perimetroRect(largo, ancho)}")
    else:
        print("Opción no válida.")
main()