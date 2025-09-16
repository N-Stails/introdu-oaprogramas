#operações

print("escolha dentre as seguintes operações e escreva abaixo sua escolhida: \n soma \n subtração \n multiplicação \n divisão \n par ou ímpar \n número primo \n fatorial \n para encerrar, digite sair.")

t = str(input("insira aqui sua escolha: "))
t.lower()

if t == "sair":
    print("obrigado pela preferência! Até a próxima!")

while t != "sair":
    if t == "soma":
        n1 = int(input("insira seu primeiro número:"))
        n2 = int(input("insira seu segundo número:"))
        print("o resultado é:", n1 + n2)
    if t == "subtração":
        n1 = int(input("insira seu primeiro número:"))
        n2 = int(input("insira seu segundo número:"))
        print("o resultado é:", n1 - n2)
    if t == "multiplicação":
        n1 = int(input("insira seu primeiro número:"))
        n2 = int(input("insira seu segundo número:"))
        print("o resultado é:", n1 * n2)
    if t == "divisão":
        n1 = int(input("insira seu primeiro número:"))
        n2 = int(input("insira seu segundo número:"))
        print("o resultado é:", n1 / n2)
    if t == "par ou ímpar":
        n1 = int(input("insira seu número:"))
        if n1 % 2 != 0:
            print("este número é ímpar!")
        else:
            print("este número é par!")
    if t == "número primo":
        n = int(input("insira seu número: "))
        s = 0
        for i in range(1,n+1):
            if n%i == 0:
                s+=1
        if s ==2:
            print("é primo.")
        else:
            print("não é primo.")
    if t == "fatorial":
        n = int(input("insira seu número: "))
        f = 1
        for i in range(1,n+1):
            f *= i
        print("O fatorial de",n,"é:",f)
    t = str(input("insira aqui sua escolha: "))
    t.lower()

