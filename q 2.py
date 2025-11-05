#Arthur, Erick, Nicollas

n = int(input("insira seu número: "))
f = 0
while n != 0:
    v = n%16
    if v == 0:
        f += v
    if v == 1:
        f += v
    if v == 2:
        f += v
    if v == 3:
        f += v
    if v == 4:
        f += v
    if v == 5:
        f += v
    if v == 6:
        f += v
    if v == 7:
        f += v
    if v == 8:
        f += v
    if v == 9:
        f += v
    if v == 10:
        f += v
    if v == 11:
        f += v
    if v == 12:
        f += v
    if v == 13:
        f += v
    if v == 14:
        f += v
    if v == 15:
        f += v
    if v == 16:
        f += v
    n //= 16

print(f"a conversão de decimal para hexadecimal de seu número é: {f}")