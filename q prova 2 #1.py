n = int(input("insira seu número:"))
im = 0
while n//10 != 0:
    if (n % 10)%2 > 0:
        im += 1
    n = n//10
if (n % 10)%2 > 0:
    im += 1
f = 1
for i in range(1,im+1):
    f *= i

print("o fatorial da soma da quantidade de números ímpares do seu número é:", f)