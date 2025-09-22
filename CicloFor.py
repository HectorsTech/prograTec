""""
num = int(input("Un numero positivo n"))

for i in range(num):
    print(i+1)
    num -= 1
"""
num = int(input("Un numero positivo n: "))
sum = 0
for i in range(1,num+1,3):
    sum = sum +i
print(sum)

