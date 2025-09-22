basica = 700
estandar = 900
deLujo = 1500

clientesFrecuentes = 0.20
cleinteNormD = 0.10
clienteNormV = 0.15

tipoSilla = input("Ingrese el tipo de silla (basica(B), estandar(E), deLujo(L)): ").lower()
clienteTipo = input("¿Es cliente frecuente(F) o normal(N)?").lower()
cantidadSillas = int(input("Ingrese la cantidad de sillas a comprar: "))

def clienteFrecuente(total):
    descuento = total * clientesFrecuentes
    total = total - (total*clientesFrecuentes)
    return total, descuento
    

def clienteNormal(total):
    if (total >= 10000 and total < 20000):
        descuento = total * .10
        total = total - (total*.10)
    elif (total >= 20000):
        descuento = total * .15
        total = total - (total*.15)
    return total, descuento
        
if (tipoSilla == "b"):
    total = cantidadSillas * basica
elif (tipoSilla == "e"):
    total = cantidadSillas * estandar
elif (tipoSilla == "l"):
    total = cantidadSillas * deLujo

print(total)

if (clienteTipo == "f"):
    total, descuento = clienteFrecuente(total)
elif (clienteTipo == "n"):
    total, descuento = clienteNormal(total)
    
print(descuento)
print(total)
print("Gracias por su compra, vuelva pronto :) ")
