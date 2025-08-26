#for q 1
p = 0
n = 0
for i in range(20):
    a = int(input("insira seu número:"))
    if a > 0:
        p += a
    else:
        n += 1
print("soma dos positivos:", p,"quantidade de negativos:",n)