#for q 4

nj = int(input("Digite o número de jogadores do time: "))
am = 0

for i in range(nj):
    a = int(input("Digite a altura do jogador: "))
    am += a
print("A altura média do time é:",am/nj)