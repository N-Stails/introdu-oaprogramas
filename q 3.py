#Arthur, Erick, Nicollas

n = int(input("insira seu número: "))
m = 0
while n != 0:
    na = n%10
    if na > m:
        m = na
    n = n//10
    n%10

print(f"o maior entre os algorismos inseridos é: {m}")