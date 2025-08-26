#for q 8

n = int(input("Digite seu número: "))
f = 1

for i in range(1,n+1):
    f *= i
print("O fatorial de",n,"é:",f)