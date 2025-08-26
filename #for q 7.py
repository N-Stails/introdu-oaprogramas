#for q 7

anos = 0
at = 150
ah = 110

for i in range(100):
    anos += 1
    at += 2
    ah += 3
    if ah > at:
        print ("Serão necessários",anos,"anos para que a altura do Homem-Aranha seja maior que a altura do Thanos.")
        break
