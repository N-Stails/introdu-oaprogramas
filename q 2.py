#Arthur, Erick, Nicollas

s = 0
for i in range (1, 201):
    if i % 3 == 0:
        s += i

print(f"a soma de todos os múltiplos de 3 entre 1 e 200 é: {s}")