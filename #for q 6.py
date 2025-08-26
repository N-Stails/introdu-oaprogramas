#for q 6

mm = 10
ma = 0
ap = 0
rp = 0

for i in range(10):
    n1 = int(input("Digite sua nota do primeiro bimestre: "))
    n2 = int(input("Digite sua nota do segundo bimestre: "))
    n3 = int(input("Digite sua nota do terceiro bimestre: "))
    m = (n1+n2+n3)
    print("Sua média é:",m/3)
    if m < mm:
        mm = m
    else:
        ma = m
    if m < 6:
        rp += 1
    else:
        ap += 1

print("A maior média é:",ma)
print("A menor média é:",mm)
print("A quantidade de alunos aprovados é:",ap)
print("A quantidade de alunos reprovados é:",rp)
