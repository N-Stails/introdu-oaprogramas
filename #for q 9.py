#for q 9

n = int(input("Digite seu número: "))
s = 0

for i in range(1,n+1):
    if n%i == 0:
        s+=1

if s ==2:
    print(n,"é primo.")
else:
    print(n,"não é primo.")