'''
numero = int(input("Ingrese un numero: "))
contador =0 
while numero > 0:
    contador += 1
    print(contador)
    numero -= 1
'''
'''

num = int(input("Numero a sumar, el 0 termina la suma: "))
sum = 0

while num != 0:
    num = int(input("Numero a sumar, el 0 termina la suma: "))
    sum = sum + num

print(sum)
'''


'''


num = int(input('Escribe un numero para sumar,'))
sum = 0
while num > 0:
    sum = sum + num
    num -= 1
print(sum)
'''
'''
a = 120 
b = 250
c = 360

clave = str(input("Ingresa la clave de compra: ")).lower()
sum = 0
while clave != 'x':
    if clave == 'a':
        sum = sum + a
    if clave == 'b':
        sum = sum + b
    if clave == 'c':
        sum = sum + c
    clave = str(input("Ingresa la clave de compra: ")).lower()

print(sum)
'''

