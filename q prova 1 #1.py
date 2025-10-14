n = str(input("insira seu número:"))
p = 0
for i in n:
    d = 0
    i = int(i)
    for e in range (1, i+1):
        if i%e == 0:
            d += 1
    if d == 2:
        p += i

print("o número de primos presentes no seu número é:", p)