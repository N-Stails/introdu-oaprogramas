#Arthur, Erick, Nicollas

n = int(input("insira seu número: "))
s = 0
while n != 0:
    s += n%10
    n = n//10

print(f"a soma dos algorismos inseridos é: {s}")