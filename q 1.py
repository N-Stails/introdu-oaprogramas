#Arthur, Erick, Nicollas

n = int(input("insira seu número: "))
p = "resultado = "
for i in range (1, n+1):
    str(i)
    p += f"{i}!"
    if i != n:
        p += " + "

print(f"a soma dos fatoriais de todos os números entre 1 e esse número é: {p}")